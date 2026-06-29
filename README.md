# CA Priyam Gupta | Executive Portfolio & Inquiry Pipeline

A high-performance, secure, and visually stunning monorepo portfolio application built for **CA Priyam Gupta** (Chartered Accountant & CS Professional G1). This project bridges a modern Next.js frontend with a robust Django REST Framework backend, implementing advanced features like encrypted database fields, parallel server-side fetches, and production-ready environment configurations.

---

## 🚀 Tech Stack

### Frontend
*   **Framework:** Next.js (App Router, dynamic SSR)
*   **Language:** TypeScript (Strict type safety)
*   **Styling:** Tailwind CSS (Custom dark slate & neon-cyan glassmorphism theme)
*   **HTTP Client:** Native Fetch API (Parallelized via `Promise.all`)

### Backend
*   **Framework:** Django & Django REST Framework (DRF)
*   **Database:** SQLite (development) / PostgreSQL (production-ready via `dj-database-url`)
*   **Security:** Cryptography (AES-256 Fernet symmetric encryption at rest)
*   **Configuration:** `django-environ` (Environment variable isolation)

---

## ✨ Features

### 💻 Frontend (Next.js Application)
*   **Parallel Fetching:** Employs parallel API querying on the server (`Promise.all`) to resolve all portfolio data in a single round-trip, maximizing page load speeds.
*   **Aesthetic UI/UX:** A bespoke premium dark theme using HSL tailored color schemes, subtle ambient glow effects, gradients, and micro-interactions.
*   **Interactive Inquiry Pipeline:** Client-side React state-driven form validating and posting data directly to the Django API, containing:
    *   Dynamic visual states (`Sending...` spinner, emerald-green success banner, and detailed rose-red error alerts).
    *   Support for Recruitment, Networking, and Industry Query subject categorizations.
*   **Universal Tab Management:** Centrally configured Next.js Metadata for search engine optimization (SEO) and tab title resolution.

### 🛡️ Backend (Django REST Framework)
*   **Symmetric Encryption at Rest:** Sensitive client inquiries are encrypted inside the database using a custom Django model field (`EncryptedTextField`) powered by the cryptography library and derived from the Django `SECRET_KEY`.
*   **Admin Obscurity:** Admin paths are obscured dynamically via the `ADMIN_PATH` environment variable.
*   **Database Seeding Command:** A custom Django management command (`python manage.py seed_data`) to automatically clear and seed accurate corporate credentials and articleship timelines.
*   **Automated Admin Superuser:** Triggers a post-migration hook to auto-provision administrative access in cloud environments safely.
*   **CORS & CSRF Policies:** Strict production-ready config matching local hosts and target cloud environments (e.g., Render/Vercel) utilizing `django-cors-headers`.

---

## 📂 Repository Structure

```text
├── Backend/                 # Django Rest API
│   ├── api/                 # Django App for Models, Serializers, Views
│   │   ├── management/      # Custom django management commands (seed_data.py)
│   │   ├── models.py        # Database schema including EncryptedTextField
│   │   └── views.py         # DRF Viewsets
│   ├── core/                # Django project settings (settings.py, urls.py)
│   └── requirements.txt     # Python backend dependencies
├── frontend/                # Next.js Frontend Application
│   ├── app/                 # Next.js App Router (pages, layout)
│   ├── components/          # Reusable Client-side components (ContactForm.tsx)
│   ├── package.json         # Node.js dependencies & scripts
│   └── tsconfig.json        # TypeScript configurations
└── README.md                # Project documentation
```

---

## 🛠️ Local Installation & Setup

### Prerequisites
*   Python 3.10+
*   Node.js 18+
*   npm or yarn

### 1. Backend Setup

1.  Navigate to the `Backend` directory:
    ```bash
    cd Backend
    ```
2.  Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    # Windows:
    .venv\Scripts\activate
    # macOS/Linux:
    source .venv/bin/activate
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Set up your local configuration in `Backend/.env`:
    ```env
    DEBUG=True
    SECRET_KEY="your-local-development-secret-key"
    DATABASE_URL="sqlite:///db.sqlite3"
    ALLOWED_HOSTS="localhost,127.0.0.1"
    CORS_ALLOWED_ORIGINS="http://localhost:3000,http://127.0.0.1:3000"
    ADMIN_PATH="secure-ca-vault-789"
    ```
5.  Apply database migrations:
    ```bash
    python manage.py migrate
    ```
6.  Seed the portfolio resume data:
    ```bash
    python manage.py seed_data
    ```
7.  Run the backend development server:
    ```bash
    python manage.py runserver
    ```

---

### 2. Frontend Setup

1.  Navigate to the `frontend` directory:
    ```bash
    cd ../frontend
    ```
2.  Install dependencies:
    ```bash
    npm install
    ```
3.  Configure local environment variables in `frontend/.env.local`:
    ```env
    NEXT_PUBLIC_API_URL="http://127.0.0.1:8000"
    ```
4.  Run the frontend application in development mode:
    ```bash
    npm run dev
    ```
5.  Open [http://localhost:3000](http://localhost:3000) to view the application in your browser.

---

## 🔒 Security Best Practices Implemented

*   **Environment Variables Separation:** Environment parameters (`.env`, `.env.local`) are added to `.gitignore` files to safeguard private credentials, database secrets, and keys.
*   **Database Encryption:** Custom implementation of cryptography using Fernet symmetric key validation hashes generated securely.
*   **Debug Mode Defaults:** Safe config defaulting to `False` in Django settings when `DEBUG` is omitted in the environment to avoid stack trace leaks.
*   **Throttling:** Integrated REST Framework throttling limits (`AnonRateThrottle` and custom contact submission limits) to guard API endpoints.
