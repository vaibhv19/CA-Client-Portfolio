import os
from django.core.management.base import BaseCommand
from api.models import (
    ExecutiveProfile, 
    ExperienceTimeline, 
    ProfessionalSkill, 
    EducationAndCredential
)

class Command(BaseCommand):
    help = 'Seeds the database with precise resume data for CA Priyam Gupta'

    def handle(self, *args, **options):
        self.stdout.write('Clearing old database entries...')
        ExecutiveProfile.objects.all().delete()
        ExperienceTimeline.objects.all().delete()
        ProfessionalSkill.objects.all().delete()
        EducationAndCredential.objects.all().delete()

        # 1. Seed Executive Profile
        self.stdout.write('Seeding Executive Profile...')
        ExecutiveProfile.objects.create(
            name="Priyam Gupta",
            designation="Chartered Accountant",
            bio="Newly qualified Chartered Accountant and CS Professional (G1) with 3+ years of intensive experience in Statutory Audits, Tax Compliance, and Financial Analysis. Proven track record of independently executing 80+ audit engagements for corporate and non-corporate entities.",
            profile_image_url="",
            metric1_value="80+",
            metric1_label="Audit Engagements Executed",
            metric2_value="3+ Yrs",
            metric2_label="Intensive Audit & Compliance Experience",
            metric3_value="Dual",
            metric3_label="Professional Focus (CA & CS G1)"
        )

        # 2. Seed Experience Timelines
        self.stdout.write('Seeding Experience Timelines...')
        
        # Job 1: Himanshu Tibrewal & Associates
        ExperienceTimeline.objects.create(
            role_title="Executive",
            company_name="Himanshu Tibrewal & Associates",
            period="Sep 2025 – Oct 2025",
            location="Gorakhpur, India",
            key_responsibilities=[
                "Spearheaded Statutory and Tax Audits for mid-sized corporate entities, ensuring 100% adherence to ICAI accounting standards and regulatory timelines.",
                "Conducted detailed compliance verification assessments, identifying and mitigating potential tax exposure risks for clients."
            ],
            is_executive=True,
            order=1
        )
        
        # Job 2: Gaurav G Agrawal & Co.
        ExperienceTimeline.objects.create(
            role_title="Article Assistant",
            company_name="Gaurav G Agrawal & Co.",
            period="Dec 2022 – July 2025",
            location="Gorakhpur, India",
            key_responsibilities=[
                "Independently executed 80+ end-to-end statutory and tax audit engagements across diverse industries, including manufacturing, retail, and non-profit societies.",
                "Managed full audit lifecycles and accurate filings for Forms 3CA, 3CB, 3CD, 10B, and 10BB, ensuring error-free submissions and zero penalty incidences.",
                "Facilitated Credit Facility Renewals by performing rigorous balance sheet analysis and ratio computations; assisted in Central and Statutory Bank Audits.",
                "Selected to mentor a team of 5+ junior articles on modern tax filing updates and evolving regulatory frameworks."
            ],
            is_executive=False,
            order=2
        )

        # Job 3: Agrawal Saraf & Company
        ExperienceTimeline.objects.create(
            role_title="Article Assistant",
            company_name="Agrawal Saraf & Company",
            period="Aug 2022 – Nov 2022",
            location="Gorakhpur, India",
            key_responsibilities=[
                "Streamlined TDS/TCS compliance operations, managing data validation and precise tax computation for quarterly return filings.",
                "Optimized foundational accounting systems for clients, reducing manual data entry errors by implementing standardized Tally protocols.",
                "Assisted in the internal audit of a listed company in the chemical industry as part of a 5-member team, reviewing and analyzing significant classes of transactions."
            ],
            is_executive=False,
            order=3
        )

        # 3. Seed Professional Skills matching Category Choices exactly
        self.stdout.write('Seeding Professional Skills...')
        skills_data = [
            # Auditing & Assurance
            ('Auditing & Assurance', 'Statutory Audits'),
            ('Auditing & Assurance', 'Tax Audits (Income Tax & GST)'),
            ('Auditing & Assurance', 'Bank Audits'),
            ('Auditing & Assurance', 'Internal Audits'),
            # Taxation & Compliance
            ('Taxation & Compliance', 'Corporate Taxation'),
            ('Taxation & Compliance', 'TDS/TCS & GST Return Filing'),
            ('Taxation & Compliance', 'Forms 3CD / 10B / 10BB'),
            ('Taxation & Compliance', 'ITR Filings'),
            # Financial Analysis
            ('Financial Analysis', 'Credit Facility Renewal'),
            ('Financial Analysis', 'Ratio Analysis'),
            ('Financial Analysis', 'Cash Flow Forecasting & CMA Data'),
            # Tools & Software
            ('Tools & Software', 'Advanced MS Excel (VLOOKUP, Pivots)'),
            ('Tools & Software', 'Tally Prime'),
            ('Tools & Software', 'CompuOffice')
        ]
        for cat, name in skills_data:
            ProfessionalSkill.objects.create(category=cat, skill_name=name)

        # 4. Seed Education & Credentials
        self.stdout.write('Seeding Education & Credentials...')
        
        # ICAI
        EducationAndCredential.objects.create(
            degree="Chartered Accountant (CA Final)",
            institution="Institute of Chartered Accountants of India (ICAI)",
            year="Cleared May 2026",
            order=1
        )
        # ICSI
        EducationAndCredential.objects.create(
            degree="Company Secretary (CS Professional G1)",
            institution="Institute of Company Secretaries of India (ICSI)",
            year="Cleared Group 1 Dec 2025",
            order=2
        )
        # Post Graduation
        EducationAndCredential.objects.create(
            degree="Master of Commerce (M.Com)",
            institution="Deen Dayal Upadhyaya Gorakhpur University",
            year="Mar 2021",
            order=3
        )
        # Graduation
        EducationAndCredential.objects.create(
            degree="Bachelor of Commerce (B.Com)",
            institution="Deen Dayal Upadhyaya Gorakhpur University",
            year="Mar 2019",
            order=4
        )

        self.stdout.write(self.style.SUCCESS('Successfully automated data loading! Resume data is 100% accurate.'))