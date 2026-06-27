from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ExecutiveProfileView,
    ExperienceTimelineViewSet,
    EducationAndCredentialViewSet,
    ProfessionalSkillViewSet,
    ContactMessageViewSet
)

# Using DefaultRouter to wire up the ViewSets automatically.
router = DefaultRouter()
router.register(r'experience', ExperienceTimelineViewSet, basename='experience')
router.register(r'education', EducationAndCredentialViewSet, basename='education')
router.register(r'networking-inquiries', ContactMessageViewSet, basename='networking-inquiries')

# Combined URL patterns
urlpatterns = [
    # Router urls for /experience/, /education/, /networking-inquiries/
    path('', include(router.urls)),
    
    # Custom API endpoint paths
    path('profile/', ExecutiveProfileView.as_view(), name='profile'),
    path('skills/', ProfessionalSkillViewSet.as_view(), name='skills'),
]
