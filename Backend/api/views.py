from rest_framework import viewsets, generics, status, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, BasePermission
from rest_framework.exceptions import PermissionDenied
from rest_framework.throttling import AnonRateThrottle

from .models import (
    ExecutiveProfile,
    ExperienceTimeline,
    EducationAndCredential,
    ProfessionalSkill,
    ContactMessage
)
from .serializers import (
    ExecutiveProfileSerializer,
    ExperienceTimelineSerializer,
    EducationAndCredentialSerializer,
    ProfessionalSkillSerializer,
    ContactMessageSerializer
)

class ExecutiveProfileView(generics.RetrieveAPIView):
    """
    Read-only view for the single ExecutiveProfile.
    Returns the first ExecutiveProfile found or a default one if none exists.
    """
    serializer_class = ExecutiveProfileSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        profile = ExecutiveProfile.objects.first()
        if not profile:
            # Seed a default profile if database is currently empty
            profile = ExecutiveProfile.objects.create(
                name="CA Priyam Gupta",
                designation="Chartered Accountant (ICAI) & CS Professional (G1)",
                bio="Objective-driven statement focusing on transition to corporate roles."
            )
        return profile


class ExperienceTimelineViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only ViewSet for ExperienceTimeline objects.
    """
    queryset = ExperienceTimeline.objects.all()
    serializer_class = ExperienceTimelineSerializer
    permission_classes = [AllowAny]


class EducationAndCredentialViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only ViewSet for EducationAndCredential objects.
    """
    queryset = EducationAndCredential.objects.all()
    serializer_class = EducationAndCredentialSerializer
    permission_classes = [AllowAny]


class ProfessionalSkillViewSet(APIView):
    """
    Read-only view that groups ProfessionalSkill objects by their category.
    Fulfills the format required by TECHSTACK: Categorized object (Tax, Audit, Tools).
    """
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        skills = ProfessionalSkill.objects.all()
        categorized_skills = {}
        for skill in skills:
            cat = skill.category
            if cat not in categorized_skills:
                categorized_skills[cat] = []
            categorized_skills[cat].append(skill.skill_name)
        return Response(categorized_skills, status=status.HTTP_200_OK)


class ContactMessageWriteOnlyPermission(BasePermission):
    """
    Custom permission that explicitly raises PermissionDenied (returns 403)
    if the request method is GET.
    """
    def has_permission(self, request, view):
        if request.method == 'GET':
            raise PermissionDenied("GET requests are not allowed on this secure endpoint.")
        return True


class ContactMessageViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Write-only ViewSet for submitting ContactMessages.
    Only POST requests are mapped. GET requests return a 403 Forbidden.
    Throttled using a contact-specific AnonRateThrottle (5 per day).
    """
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [ContactMessageWriteOnlyPermission]
    throttle_classes = [AnonRateThrottle]
    throttle_scope = 'contact'

    def list(self, request, *args, **kwargs):
        raise PermissionDenied("GET requests are not allowed on this secure endpoint.")

    def retrieve(self, request, *args, **kwargs):
        raise PermissionDenied("GET requests are not allowed on this secure endpoint.")
