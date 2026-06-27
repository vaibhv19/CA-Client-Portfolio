from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import (
    ExecutiveProfile,
    ExperienceTimeline,
    EducationAndCredential,
    ProfessionalSkill,
    ContactMessage
)

class PortfolioAPITests(APITestCase):

    def setUp(self):
        # Seed test data
        self.profile = ExecutiveProfile.objects.create(
            name="CA Priyam Gupta",
            designation="Chartered Accountant (ICAI) & CS Professional (G1)",
            bio="Test executive bio statement focusing on transition to corporate roles.",
            profile_image_url="http://example.com/headshot.jpg",
            metric1_value="80+",
            metric1_label="Statutory Audits",
            metric2_value="3+",
            metric2_label="Years Experience",
            metric3_value="Dual",
            metric3_label="CA & CS"
        )
        
        self.experience = ExperienceTimeline.objects.create(
            role_title="Article Assistant",
            company_name="Gaurav G Agrawal & Co.",
            period="Dec 2022 – July 2025",
            location="Gorakhpur",
            key_responsibilities=["Statutory audits", "Tax filings"],
            is_executive=False,
            order=1
        )
        
        self.education = EducationAndCredential.objects.create(
            degree="Chartered Accountant",
            institution="ICAI",
            year="Qualified May 2026",
            order=1
        )
        
        self.skill_audit = ProfessionalSkill.objects.create(
            category="Auditing & Assurance",
            skill_name="Statutory Audit"
        )
        self.skill_tax = ProfessionalSkill.objects.create(
            category="Taxation & Compliance",
            skill_name="GST"
        )

    def test_get_profile(self):
        """
        Verify that GET requests to the profile endpoint return a single profile object directly.
        """
        url = reverse('profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "CA Priyam Gupta")
        self.assertEqual(response.data['designation'], "Chartered Accountant (ICAI) & CS Professional (G1)")
        self.assertEqual(response.data['metric1_value'], "80+")
        
    def test_get_profile_fallback(self):
        """
        Verify that GET requests to the profile endpoint return a default profile if the DB is empty.
        """
        ExecutiveProfile.objects.all().delete()
        url = reverse('profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "CA Priyam Gupta")
        self.assertTrue(len(response.data['bio']) > 0)

    def test_get_experience(self):
        """
        Verify that GET requests to experience endpoint return a list of experience items.
        """
        url = reverse('experience-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['role_title'], "Article Assistant")

    def test_get_education(self):
        """
        Verify that GET requests to education endpoint return a list of education items.
        """
        url = reverse('education-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['degree'], "Chartered Accountant")

    def test_get_skills_categorized(self):
        """
        Verify that GET requests to skills endpoint return a categorized object.
        """
        url = reverse('skills')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Auditing & Assurance", response.data)
        self.assertIn("Taxation & Compliance", response.data)
        self.assertEqual(response.data["Auditing & Assurance"], ["Statutory Audit"])
        self.assertEqual(response.data["Taxation & Compliance"], ["GST"])

    def test_post_networking_inquiry_success(self):
        """
        Verify that valid POST submissions to networking-inquiries succeed, sanitizing HTML
        and validating inputs, and are correctly persisted.
        """
        url = reverse('networking-inquiries-list')
        data = {
            "name": "<p>Jane Doe</p>",
            "organization": "<b>Acme Corp</b>",
            "email": "jane.doe@example.com",
            "subject": "Recruitment",
            "message": "Hello, this is a <i>test message</i>."
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Check DB persistence and encryption decryption fallback/integrity
        inquiry = ContactMessage.objects.get(email="jane.doe@example.com")
        self.assertEqual(inquiry.name, "Jane Doe") # HTML tag removed
        self.assertEqual(inquiry.organization, "Acme Corp") # HTML tag removed
        self.assertEqual(inquiry.message, "Hello, this is a test message.") # HTML tag removed

    def test_post_networking_inquiry_invalid_email(self):
        """
        Verify that submitting an invalid email returns 400 Bad Request.
        """
        url = reverse('networking-inquiries-list')
        data = {
            "name": "Jane Doe",
            "organization": "Acme Corp",
            "email": "invalid-email-format",
            "subject": "Networking",
            "message": "Valid message"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_post_networking_inquiry_too_long_message(self):
        """
        Verify that submitting a message longer than 1000 characters returns 400 Bad Request.
        """
        url = reverse('networking-inquiries-list')
        data = {
            "name": "Jane Doe",
            "organization": "Acme Corp",
            "email": "jane@example.com",
            "subject": "Networking",
            "message": "A" * 1001
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('message', response.data)

    def test_get_networking_inquiry_forbidden(self):
        """
        Verify that GET requests to the write-only networking-inquiries endpoint return 403 Forbidden.
        """
        # Test list endpoint
        url_list = reverse('networking-inquiries-list')
        response = self.client.get(url_list)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Create message manually and test detail endpoint
        msg = ContactMessage.objects.create(
            name="Manual Name",
            organization="Manual Org",
            email="manual@example.com",
            subject="Recruitment",
            message="Secret message"
        )
        url_detail = reverse('networking-inquiries-detail', kwargs={'pk': msg.pk})
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
