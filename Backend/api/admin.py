from django.contrib import admin
from .models import (
    ExecutiveProfile,
    ExperienceTimeline,
    EducationAndCredential,
    ProfessionalSkill,
    ContactMessage
)

@admin.register(ExecutiveProfile)
class ExecutiveProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'metric1_value', 'metric2_value', 'metric3_value')
    fieldsets = (
        ('General Info', {
            'fields': ('name', 'designation', 'bio', 'profile_image_url')
        }),
        ('Impact Metrics', {
            'fields': (
                ('metric1_value', 'metric1_label'),
                ('metric2_value', 'metric2_label'),
                ('metric3_value', 'metric3_label'),
            )
        }),
    )

    def has_add_permission(self, request):
        # Allow only one profile instance to exist
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(ExperienceTimeline)
class ExperienceTimelineAdmin(admin.ModelAdmin):
    list_display = ('role_title', 'company_name', 'period', 'location', 'is_executive', 'order')
    list_filter = ('is_executive', 'location')
    search_fields = ('role_title', 'company_name', 'location')
    list_editable = ('order', 'is_executive')
    ordering = ('order', '-id')


@admin.register(EducationAndCredential)
class EducationAndCredentialAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'year', 'order')
    search_fields = ('degree', 'institution')
    list_editable = ('order',)
    ordering = ('order', '-id')


@admin.register(ProfessionalSkill)
class ProfessionalSkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'category')
    list_filter = ('category',)
    search_fields = ('skill_name',)
    ordering = ('category', 'skill_name')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'email', 'subject', 'created_at')
    list_filter = ('subject', 'created_at')
    search_fields = ('name', 'organization', 'email', 'message')
    readonly_fields = ('name', 'organization', 'email', 'subject', 'message', 'created_at')
    ordering = ('-created_at',)

    def has_add_permission(self, request):
        # Inquiries should only be created via the frontend API
        return False

    def has_change_permission(self, request, obj=None):
        # Inquiries should be read-only in the admin panel
        return False
