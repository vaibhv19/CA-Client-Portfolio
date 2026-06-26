This `APPFLOW.md` document serves as the structural logic map for the decoupled architecture. It provides autonomous AI coding agents with the routing, state management, and data-fetching logic required to implement the executive portfolio for CA Priyam Gupta.

---

# APPFLOW.md: User Journey & Navigation Architecture

## 1. NAVIGATION HIERARCHY TREE

```text
[ROOT /]
├── (Public Frontend - Next.js)
│   ├── / (Home) ──────────────────> [Executive Summary + Core Metrics]
│   ├── /journey ──────────────────> [Dynamic Career Timeline /api/experience/]
│   ├── /competencies ─────────────> [Categorized Skill Grid /api/skills/]
│   └── /contact ──────────────────> [Networking Form /api/networking-inquiries/]
│
└── (Private Backend - Django CMS)
    └── /secure-ca-vault-789/ ─────> [Secure Staff Challenge/Auth]
        ├── /dashboard/ ───────────> [Message Inbox (Encrypted)]
        ├── /experience/manage/ ───> [Timeline CRUD]
        ├── /education/manage/ ────> [Credential CRUD]
        └── /skills/manage/ ───────> [Competency CRUD]
```

---

## 2. SCREEN-BY-SCREEN FUNCTIONAL INTERACTIONS

### **A. Home Screen (`/`)**
*   **Initial Render:** 
    *   Static SEO-optimized metadata (Title: "CA Priyam Gupta | Chartered Accountant").
    *   Hydrate `Executive Summary` from `/api/profile/`.
*   **Visual Priority:**
    *   Hero section displays "CA Priyam Gupta" and "CS Professional (G1)".
    *   Immediate high-impact rendering of **Core Metrics**: "80+ Statutory & Tax Audits", "3+ Years Corporate Experience".
*   **Compliance Check:** No "Hire Me" buttons. CTAs are limited to "View Journey" and "Contact for Networking".

### **B. Professional Journey Screen (`/journey`)**
*   **Data Hydration Flow:**
    1.  **State [Loading]:** Render `SkeletonCard` components in a vertical line.
    2.  **Action:** `GET /api/experience/`.
    3.  **State [Success]:** Map the JSON array into a vertical timeline. 
        *   *Sort Logic:* `start_date` descending (most recent first).
        *   *Highlight:* "Himanshu Tibrewal & Associates" (Current/Latest).
    4.  **State [Error]:** Render fallback message "Timeline documentation currently unavailable."
*   **Interaction:** Clicking a timeline node expands detailed bullet points regarding audit types and compliance filings (Forms 3CD, 10B, etc.).

### **C. Competencies Screen (`/competencies`)**
*   **Interaction Pattern:** Categorized "Grid View".
*   **Logic:** Frontend iterates through the `skills` array and filters by the `category` attribute:
    *   *Auditing:* Statutory, Bank, Internal.
    *   *Taxation:* GST, TDS/TCS, ITR.
    *   *Analysis:* Credit Facility, Ratio Analysis.
*   **Visual Style:** Pills or badge components with corporate slate/navy accents.

### **D. Networking Contact Screen (`/contact`)**
*   **The State Machine:**
    1.  **[Idle State]:** Display input fields. Footer displays LinkedIn and Corporate Email anchor nodes.
    2.  **[Validation State]:** On `onSubmit`, trigger Zod schema validation (Email format check, non-empty fields).
    3.  **[Submitting State]:**
        *   Action: `POST /api/networking-inquiries/`.
        *   UI: Button shows a loading spinner; all inputs set to `disabled=true`.
    4.  **[Success State]:**
        *   UI: Reset form fields. Render "Success Banner": *“Professional inquiry successfully routed. Your message has been encrypted and sent to the practitioner for verification.”*
    5.  **[Error State]:** Toast notification: *“System temporarily unable to process inquiry. Please connect via LinkedIn.”*

---

## 3. PRIVATE DASHBOARD & VAULT LIFECYCLE

### **Access Control Guard Rails**
*   **Middleware Logic:** 
    *   Backend `admin.py` and `urls.py` must enforce `IsStaff` or `IsSuperuser` status.
    *   Any unauthenticated request to `/secure-ca-vault-789/` must trigger a `404 Not Found` or a hard redirect to the home page to prevent fingerprinting of the login screen.

### **Administrative Workflow**
1.  **Staff Challenge:** Priyam authenticates via the custom Django Admin login.
2.  **Dashboard Entry:** Redirects to the Obscured Vault.
3.  **Data Management:**
    *   *Inquiry Review:* Reads incoming recruiter messages (Decrypted on-the-fly).
    *   *Career Update:* Adds a new record to the `Experience` table upon promotion or job change.
    *   *Instant Update:* Upon clicking "Save", the Next.js site reflects changes on the next fetch (or via ISR revalidation).

---

## 4. GLOBAL LAYOUT FRAMEWORK (THE "NAV-SHELL")

*   **Adaptive Theme:** Strictly corporate. Dark mode defaults with Slate-900 backgrounds and Zinc-400 text for readability. No vibrant/flashy colors.
*   **Sticky Header:**
    *   [Left]: "CA Priyam Gupta" (Home Link).
    *   [Right]: Journey | Competencies | Contact.
*   **Permanent Legal Footer:**
    *   *Requirement:* Standardized text: *"This digital portfolio is a professional biographical record for corporate networking and verification of professional standing as a Chartered Accountant in Service. In compliance with the ICAI Code of Ethics, no public solicitation or commercial services are offered through this platform."*
    *   *Hyperlinks:* LinkedIn Profile (External), ICSI/ICAI Verification Links (Optional).

---

**AI AGENT IMPLEMENTATION NOTE:**
When generating code for the `/journey` and `/competencies` pages, ensure the frontend utilizes **Next.js Server Components (RSC)** for the initial fetch to ensure the biographical data is SEO-indexable before hydration.