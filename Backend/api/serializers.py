from rest_framework import serializers
from django.utils.html import strip_tags
import re
from .models import (
    ExecutiveProfile,
    ExperienceTimeline,
    EducationAndCredential,
    ProfessionalSkill,
    ContactMessage
)

class ExecutiveProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutiveProfile
        fields = [
            'id', 'name', 'designation', 'bio', 'profile_image_url',
            'metric1_value', 'metric1_label',
            'metric2_value', 'metric2_label',
            'metric3_value', 'metric3_label'
        ]


class ExperienceTimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceTimeline
        fields = [
            'id', 'role_title', 'company_name', 'period',
            'location', 'key_responsibilities', 'is_executive', 'order'
        ]


class EducationAndCredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationAndCredential
        fields = ['id', 'degree', 'institution', 'year', 'order']


class ProfessionalSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalSkill
        fields = ['id', 'category', 'skill_name']


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'organization', 'email', 'subject', 'message', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_name(self, value):
        # Sanitize HTML tags
        clean_value = strip_tags(value).strip()
        if len(clean_value) < 1:
            raise serializers.ValidationError("Name cannot be empty.")
        return clean_value

    def validate_organization(self, value):
        # Sanitize HTML tags
        return strip_tags(value).strip()

    def validate_email(self, value):
        # Sanitize HTML tags
        clean_value = strip_tags(value).strip()
        # Regex validation for email matching TECHSTACK requirements
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, clean_value):
            raise serializers.ValidationError("Enter a valid email address.")
        return clean_value

    def validate_message(self, value):
        # Sanitize HTML tags
        clean_value = strip_tags(value).strip()
        if len(clean_value) > 1000:
            raise serializers.ValidationError("Message content cannot exceed 1000 characters.")
        if len(clean_value) < 1:
            raise serializers.ValidationError("Message cannot be empty.")
        return clean_value
