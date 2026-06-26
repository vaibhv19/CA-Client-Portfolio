# Product Requirements Document (PRD): Executive Portfolio for CA Priyam Gupta

## 1. PRODUCT NAME & EXECUTIVE TAGLINE
*   **Product Name:** CA Priyam Gupta Executive Digital Portfolio
*   **Executive Tagline:** Chartered Accountant (ICAI) & CS Professional (G1) | Corporate Finance & Statutory Compliance Specialist.
*   **Status Statement:** A strictly biographical professional record documenting the corporate journey, academic credentials, and core competencies of a newly qualified Chartered Accountant in Service.

---

## 2. TARGET USER PERSONAS
| Persona | Goals |
| :--- | :--- |
| **Executive Headhunter** | To validate CA/CS credentials, review audit volume (80+ engagements), and assess technical tool proficiency for MNC placements. |
| **Corporate HR Director** | To evaluate the candidate’s progression from Article Assistant to Executive and confirm geographical mobility/academic consistency. |
| **Senior Finance Leader** | To assess the depth of "hands-on" experience in Statutory Audits, Tax Compliance, and Credit Facility renewals. |
| **Professional Peer** | To facilitate industry networking and knowledge exchange within the ICAI/ICSI community. |

---

## 3. CORE PAGE ARCHITECTURE

### A. Home Page (Executive Summary)
*   **Hero Section:** High-resolution professional headshot, name, and designation (Chartered Accountant).
*   **Executive Bio:** A 150-word objective-driven statement focusing on the transition from training to corporate executive roles.
*   **Dynamic Metric Grid (The "Quantified Impact" Bar):**
    *   *Metric 1:* 80+ Statutory & Tax Audits Executed.
    *   *Metric 2:* 3+ Years Intensive Corporate Experience.
    *   *Metric 3:* Dual Professional Focus (CA & CS G1).
*   **Dynamic Highlight Grid:** A curated feed of the three most recent professional milestones pulled from the CMS.

### B. Professional Journey Page (Dynamic Timeline)
*   **Component:** Vertical loopable timeline.
*   **Data Source:** Django `Experience` Model.
*   **Fields:** Role Title, Organization Name, Period, Location, Key Responsibilities (Bulleted).
*   **Visual Logic:** Distinct visual separation between "Executive Experience" and "Article Assistant Milestones."

### C. Core Competencies Page (Categorized Grid)
*   **Component:** 4-column dynamic grid.
*   **Data Source:** Django `SkillCategory` Model.
*   **Categories:**
    1.  **Auditing & Assurance:** (e.g., Statutory, Tax, Bank, Internal).
    2.  **Taxation & Compliance:** (e.g., Corporate Tax, GST, TDS/TCS).
    3.  **Financial Analysis:** (e.g., Credit Renewals, Ratio Analysis, CMA Data).
    4.  **Tools & Software:** (e.g., MS Excel Advanced, Tally Prime, CompuOffice).

### D. Professional Networking Page (Contact)
*   **Constraint:** No "Inquiry for Services."
*   **Input Fields:** Name, Organization, Professional Email, Subject (Dropdown: Recruitment, Networking, Industry Query), Message.
*   **Footer:** LinkedIn Hyperlink (Clean URL) and professional domain email.

---

## 4. SECURE INQUIRY & ADMINISTRATIVE VAULT SPECIFICATION

### Backend & CMS Framework (Django)
*   **Dynamic Data Models:**
    *   `class Experience(models.Model)`: Fields for Company, Role, Tenure, and Achievement JSON.
    *   `class Education(models.Model)`: Fields for Degree, Institution, and Year.
    *   `class ProfessionalSkill(models.Model)`: Fields for Category and Skill Name.
    *   `class ContactMessage(models.Model)`: Secure storage for incoming networking inquiries.

### Administrative Vault (Access Control)
*   **Obscured Path:** The admin panel must be routed to `/secure-ca-vault-789/` to prevent brute-force discovery.
*   **Encryption:** The `ContactMessage` model must use `django-cryptography` or similar to encrypt "Message" fields at rest.
*   **Functionality:** Full CRUD (Create, Read, Update, Delete) capabilities for Priyam Gupta to update her CV data without touching the frontend code.

---

## 5. STRICT "OUT OF SCOPE" BOUNDARIES (ICAI COMPLIANCE)
To ensure 100% compliance with the **ICAI Code of Ethics (13th Edition)** for members in service, the following are **EXPLICITLY PROHIBITED** and blocked from development:
*   **NO Service Catalogs:** Do not use headers like "Services I Offer" or "Hire Me for Tax Filing."
*   **NO Commercial Call-to-Actions (CTAs):** Buttons like "Get a Quote" or "Book Consultation" are strictly banned.
*   **NO Testimonials:** Client reviews/testimonials are prohibited for CAs.
*   **NO Self-Laudatory Marketing:** Terms like "Best Auditor in Gorakhpur," "Expert," or "Leading Professional" must be replaced with factual equivalents like "Chartered Accountant" or "Practitioner."
*   **NO Client Logos:** Do not display logos of entities audited during her tenure at the firms; only the logos/names of the *employing* CA firms are permitted.

---

## 6. USER STORIES (AI AGENT INSTRUCTION)

### Recruiter Verification Story
> *As a Corporate Recruiter, I want to view a chronological, factual timeline of Priyam's 80+ audit engagements so that I can verify her technical depth in Statutory Audits before scheduling an interview.*

### Self-Service Update Story
> *As the Practitioner (Priyam), I want to log into my secure vault and update my CS Professional status from "Group 1" to "Qualified" once my results are declared, so that my public profile remains accurate without requiring a developer.*

### Secure Networking Story
> *As a Senior Finance Leader, I want to send a secure networking inquiry via the contact form so that I can discuss a potential corporate leadership opening without her personal email being exposed to public scrapers.*

---

## 7. DATA MAPPING (FOR MODEL INITIALIZATION)

### Experience Table:
1.  **Executive** | Himanshu Tibrewal & Associates | Sep 2025 – Oct 2025
2.  **Article Assistant** | Gaurav G Agrawal & Co. | Dec 2022 – July 2025
3.  **Article Assistant** | Agrawal Saraf & Company | Aug 2022 – Nov 2022

### Education Table:
*   **Chartered Accountant** | ICAI | Qualified May 2026
*   **CS Professional (G1)** | ICSI | Dec 2025
*   **M.Com** | DDU Gorakhpur University | 2021
*   **B.Com** | DDU Gorakhpur University | 2019

### Technical Stack Requirement:
*   **Frontend:** React.js or Tailwind CSS (Static-generated for speed).
*   **Backend:** Django (Headless CMS).
*   **Database:** PostgreSQL (Production) / SQLite (Development).
*   **Deployment:** Vercel (Frontend) & Railway/Render (Backend).