This `TECHSTACK.md` is designed as a technical blueprint for autonomous AI coding agents (like Claude Engineer, GitHub Copilot Workspace, or GPT-4o-Dev) to initialize and build the decoupled architecture for CA Priyam Gupta’s executive portfolio.

---

# TECHSTACK.md: High-Performance Decoupled Architecture Blueprint

## 1. DECOUPLED CORE LAYER MATRIX

### **Frontend: Next.js Web Application**
*   **Framework:** Next.js 14/15+ (App Router Architecture).
*   **Language:** TypeScript (Strict Mode).
*   **Styling:** Tailwind CSS + Shadcn/UI (for accessible, corporate-grade components).
*   **Data Fetching:** Server-side Fetch API with `next: { revalidate: 3600 }` (ISR - Incremental Static Regeneration).
*   **Why this stack?** 
    *   **Recruiter Experience:** Next.js ensures near-instant page loads (LCP < 1.2s) and high SEO visibility for search queries related to "CA Priyam Gupta" or "Chartered Accountant Gorakhpur."
    *   **Type Safety:** TypeScript ensures that the data structures returned by the Django API (Experience, Education) are strictly validated before rendering.

### **Backend: Django Headless CMS**
*   **Framework:** Python 3.11+ & Django 5.0+.
*   **API Layer:** Django REST Framework (DRF).
*   **Auth Provider:** Django Native Auth (for Admin Vault access).
*   **Why this stack?**
    *   **Enterprise Security:** Django provides built-in protection against SQL Injection, XSS, and CSRF by default.
    *   **Admin Panel:** Provides CA Priyam Gupta with a "no-code" GUI to manage her career trajectory without database knowledge.

### **Database: Managed PostgreSQL**
*   **Provider:** Supabase, Railway, or Render PostgreSQL.
*   **Role:** Relational storage for career milestones, academic records, and networking message logs.

---

## 2. DYNAMIC CONTENT MANAGEMENT API DESIGN
The backend acts as a **Read-Only JSON Source** for the public. All mutative operations are locked behind the Django Admin.

| Endpoint | Method | Data Payload | Security Policy |
| :--- | :--- | :--- | :--- |
| `/api/profile/` | `GET` | Name, Bio, Designation, Contact Metadata. | Public (Read-Only) |
| `/api/experience/` | `GET` | Array of timeline objects (Role, Firm, Dates, Points). | Public (Read-Only) |
| `/api/education/` | `GET` | Array of academic qualifications (ICAI, ICSI, University). | Public (Read-Only) |
| `/api/skills/` | `GET` | Categorized object (Tax, Audit, Tools). | Public (Read-Only) |

**CRITICAL AGENT INSTRUCTION:** 
The API must implement `ReadOnlyModelViewSet` or explicit `GET`-only permission classes for the above endpoints. Any `POST`, `PUT`, `PATCH`, or `DELETE` attempt from a non-authenticated admin session must return `405 Method Not Allowed`.

---

## 3. NETWORK INQUIRY FORM API SPECIFICATION
This is the only public "Write" operation permitted on the system.

*   **Endpoint:** `POST /api/networking-inquiries/`
*   **Payload Validation:**
    1.  **Frontend (Zod):** Validate `email` format, `name` length, and `message` content (max 1000 chars) before submission.
    2.  **Backend (DRF Serializers):** Sanitize input string to remove HTML tags; validate against `email` regex.
*   **Security:** 
    1.  **No Public Discovery:** `GET` requests to this endpoint must return `403 Forbidden`.
    2.  **Encrypted Persistence:** Messages are saved to the PostgreSQL database for Priyam to review via the private vault.

---

## 4. SYSTEM SECURITY & HARDENING ARCHITECTURE

### **CORS Whitelisting**
Install and configure `django-cors-headers`.
```python
# settings.py
CORS_ALLOWED_ORIGINS = [
    "https://priyamgupta.com", # Production Frontend
    "http://localhost:3000",   # Local Development
]
CORS_ALLOW_METHODS = ["GET", "POST", "OPTIONS"]
```

### **Rate Limiting (Anti-Spam)**
Implement DRF Throttling to prevent bot abuse of the networking form.
```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '5/day', # Maximum 5 inquiries per IP per day
    }
}
```

### **Admin Vault Obscurity**
The native `/admin/` path is a high-security risk. AI agents must rename the route:
*   **Target Route:** `/secure-ca-vault-789/`
*   **Requirement:** Any request to the standard `/admin/` should return a 404 or redirect to the home page.

### **Production Security Headers**
Force secure communication in the production environment:
*   `SECURE_SSL_REDIRECT = True`
*   `SESSION_COOKIE_SECURE = True`
*   `CSRF_COOKIE_SECURE = True`
*   `SECURE_HSTS_SECONDS = 31536000` (1 Year)

---

## 5. DEPLOYMENT & ENVIRONMENT VARIABLE BLUEPRINT

### **Frontend Configuration (`/frontend/.env.local`)**
```bash
# Public API URL for fetching data
NEXT_PUBLIC_API_BASE_URL="https://api.priyamgupta.com"
```

### **Backend Configuration (`/backend/.env`)**
```bash
# Core Settings
DEBUG=False
SECRET_KEY="<Generated-High-Entropy-String>"

# Database
DATABASE_URL="postgres://user:password@host:port/dbname"

# Security & CORS
ALLOWED_HOSTS="api.priyamgupta.com"
CORS_ALLOWED_ORIGINS="https://priyamgupta.com"

# Admin Vault Custom Path
ADMIN_PATH="secure-ca-vault-789"
```

### **Deployment Execution Flow**
1.  **Backend:** Deploy via **Docker** or **Gunicorn** to Railway/Render.
2.  **Frontend:** Deploy to **Vercel** for optimized Edge caching and Global CDN delivery.
3.  **Git Policy:** Ensure `.env` and `__pycache__` are explicitly listed in `.gitignore`. **NEVER** commit the `SECRET_KEY` to public repositories.

---

**AUTHORITATIVE COMPLIANCE NOTE:**
The AI agent must ensure that the `robots.txt` file on the frontend allows indexing of professional content but explicitly disallows indexing of the `/secure-ca-vault-789/` path.