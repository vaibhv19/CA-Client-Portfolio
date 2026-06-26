from django.db import models
from django.conf import settings
from cryptography.fernet import Fernet
import base64
import hashlib

class EncryptedTextField(models.TextField):
    """
    A custom field that encrypts text values at rest using symmetric key cryptography (Fernet).
    Key is derived securely from django SECRET_KEY.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._fernet = None

    @property
    def cipher(self):
        if self._fernet is None:
            # Derive 32-byte key from Django's SECRET_KEY
            key_hash = hashlib.sha256(settings.SECRET_KEY.encode()).digest()
            self._fernet = Fernet(base64.urlsafe_b64encode(key_hash))
        return self._fernet

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value is None or value == "":
            return value
        # Encrypt the string
        encrypted = self.cipher.encrypt(value.encode())
        return encrypted.decode()

    def from_db_value(self, value, expression, connection):
        if value is None or value == "":
            return value
        try:
            # Decrypt the string
            decrypted = self.cipher.decrypt(value.encode())
            return decrypted.decode()
        except Exception:
            # Fallback if decryption fails (e.g. if the value was stored unencrypted)
            return value

    def to_python(self, value):
        if value is None or isinstance(value, str):
            return value
        return self.from_db_value(value, None, None)


class ExecutiveProfile(models.Model):
    name = models.CharField(max_length=100, default="CA Priyam Gupta")
    designation = models.CharField(max_length=200, default="Chartered Accountant (ICAI) & CS Professional (G1)")
    bio = models.TextField(help_text="A 150-word objective-driven statement focusing on transition to corporate roles.")
    profile_image_url = models.CharField(max_length=500, blank=True, help_text="URL or path to the professional headshot.")
    
    # Quantified Impact Metrics
    metric1_value = models.CharField(max_length=50, default="80+", help_text="e.g., 80+")
    metric1_label = models.CharField(max_length=100, default="Statutory & Tax Audits Executed")
    
    metric2_value = models.CharField(max_length=50, default="3+", help_text="e.g., 3+")
    metric2_label = models.CharField(max_length=100, default="Years Intensive Corporate Experience")
    
    metric3_value = models.CharField(max_length=50, default="Dual", help_text="e.g., Dual")
    metric3_label = models.CharField(max_length=100, default="Professional Focus (CA & CS G1)")

    class Meta:
        verbose_name = "Executive Profile"
        verbose_name_plural = "Executive Profiles"

    def __str__(self):
        return f"{self.name} - {self.designation}"


class ExperienceTimeline(models.Model):
    role_title = models.CharField(max_length=150, help_text="e.g., Executive or Article Assistant")
    company_name = models.CharField(max_length=150, help_text="e.g., Himanshu Tibrewal & Associates")
    period = models.CharField(max_length=100, help_text="e.g., Sep 2025 – Oct 2025")
    location = models.CharField(max_length=100, help_text="e.g., Gorakhpur")
    key_responsibilities = models.JSONField(help_text="A list (JSON array) of bullet points representing responsibilities.")
    is_executive = models.BooleanField(default=False, help_text="Check if this is an Executive role vs. Article Assistant.")
    order = models.IntegerField(default=0, help_text="Used to manually order timeline entries.")

    class Meta:
        verbose_name = "Experience Timeline"
        verbose_name_plural = "Experience Timelines"
        ordering = ['order', '-id']

    def __str__(self):
        return f"{self.role_title} at {self.company_name} ({self.period})"


class EducationAndCredential(models.Model):
    degree = models.CharField(max_length=150, help_text="e.g., Chartered Accountant or B.Com")
    institution = models.CharField(max_length=150, help_text="e.g., ICAI or DDU Gorakhpur University")
    year = models.CharField(max_length=50, help_text="e.g., Qualified May 2026 or 2019")
    order = models.IntegerField(default=0, help_text="Used to manually order education entries.")

    class Meta:
        verbose_name = "Education and Credential"
        verbose_name_plural = "Education and Credentials"
        ordering = ['order', '-id']

    def __str__(self):
        return f"{self.degree} from {self.institution} ({self.year})"


class ProfessionalSkill(models.Model):
    CATEGORY_CHOICES = [
        ('Auditing & Assurance', 'Auditing & Assurance'),
        ('Taxation & Compliance', 'Taxation & Compliance'),
        ('Financial Analysis', 'Financial Analysis'),
        ('Tools & Software', 'Tools & Software'),
    ]
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    skill_name = models.CharField(max_length=100, help_text="e.g., Statutory Audit or Tally Prime")

    class Meta:
        verbose_name = "Professional Skill"
        verbose_name_plural = "Professional Skills"
        ordering = ['category', 'skill_name']

    def __str__(self):
        return f"{self.skill_name} ({self.category})"


class ContactMessage(models.Model):
    SUBJECT_CHOICES = [
        ('Recruitment', 'Recruitment'),
        ('Networking', 'Networking'),
        ('Industry Query', 'Industry Query'),
    ]
    name = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
    message = EncryptedTextField(help_text="This field is encrypted at rest in the database.")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} ({self.organization}) - {self.subject} at {self.created_at}"

