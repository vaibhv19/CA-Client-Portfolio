# Visual Design Specification: CA Priyam Gupta Executive Portfolio

This document serves as the visual and structural blueprint for the decoupled frontend of the **CA Priyam Gupta Executive Digital Portfolio**. The visual design details here correspond directly to the Stitch MCP server generated project layout ("Corporate Executive Portfolio" / "Executive Zenith" theme).

---

## 1. Core Brand & Aesthetic Identity
*   **Design Theme:** Institutional Modernism / Midnight Professional.
*   **Visual Direction:** A minimalist, highly structured, dark atmospheric interface utilizing low-contrast borders and high-contrast typography. 
*   **Design Tone:** Professional, authoritative, disciplined, and clinical.
*   **Key Design Principle:** Snapped grid alignment with absolute zero-radius (sharp) corners, symbolizing professional precision.

---

## 2. Global Design Tokens (Parsed from Stitch Canvas)

### A. Color Palette
The color tokens establish a dark background system paired with highly readable text hierarchy and selective interactive highlights.

| Token Name | Value | Description / Usage |
| :--- | :--- | :--- |
| `background` | `#121415` | Default dark-mode canvas background. |
| `primary-background` | `#0B192C` | Deep navy background for high-impact content areas (e.g., journey cards, main page sections). |
| `primary` | `#BAC7E1` | Steel blue-grey for secondary active elements, markers, and accent headers. |
| `on-primary` | `#243145` | High-contrast dark text inside solid primary containers. |
| `primary-container` | `#0B192C` | Background wrapper for main layout clusters. |
| `on-primary-container` | `#75829A` | Subtle grey-blue text for metadata within containers. |
| `secondary` | `#C8C6C9` | Neutral grey used for minor accents. |
| `surface` | `#121415` | Dark slate background used for page panels and cards. |
| `surface-container` | `#1E2021` | Slightly lighter dark background for containers (e.g., side nav). |
| `on-surface` | `#E2E2E3` | Off-white (Zinc) text used for primary body content and headers. |
| `on-surface-variant` | `#C5C6CD` | Medium grey text for secondary text, descriptions, and labels. |
| `tertiary` | `#7BD0FF` | Light sky-blue accent for timeline highlights and section overlines. |
| `outline` | `#8F9097` | Border color for interactive components. |
| `outline-variant` | `#44474C` | Architectural divider lines and default low-contrast border color (`#27272A` / `#44474C`). |
| `accent-highlight` | `#38BDF8` | Interactive highlight color (hover states, KPI metrics, current timelines). |

### B. Typography
The system uses **Inter** as its primary typeface to emphasize a systematic, clean presentation.

| Text Style | Font Family | Size | Weight | Line Height | Letter Spacing | Usage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `display-lg` | Inter | `48px` | `700` | `56px` | `-0.02em` | Desktop Hero / Main Screen Headers |
| `display-lg-mobile` | Inter | `32px` | `700` | `40px` | `-0.02em` | Mobile Hero Header |
| `headline-md` | Inter | `24px` | `600` | `32px` | `-0.01em` | Card Titles / Section Headings |
| `stats-xl` | Inter | `40px` | `700` | `48px` | `-0.03em` | Metric numbers |
| `body-lg` | Inter | `18px` | `400` | `28px` | Default | Large summary paragraphs / Bios |
| `body-md` | Inter | `16px` | `400` | `24px` | Default | Timeline descriptions, form entries |
| `label-caps` | Inter | `12px` | `600` | `16px` | `0.1em` | Overlines, CAPS category tags, buttons |

### C. Spacing Scale
Layout spacing is governed by standard stack offsets to enforce vertical rhythm:
*   `gutter`: `24px` (horizontal gap for grids)
*   `margin-mobile`: `16px` (outer mobile page padding)
*   `margin-desktop`: `48px` (outer desktop page padding)
*   `container-max`: `1280px` (max width of centered grids)
*   `stack-sm`: `8px` (internal item spacing)
*   `stack-md`: `16px` (card internal spacing)
*   `stack-lg`: `32px` (header to body / list item spacing)
*   `stack-xl`: `64px` (section to section spacing)

### D. Shapes & Elevation
*   **Borders:** `borderRadius: 0px` (or `0rem`). Rounded edges are strictly prohibited except for standard circle badges/avatars (`9999px`).
*   **Elevation:** Level 1 components use a `1px solid #27272A` outline. Heavy drop shadows are omitted in favor of flat borders. When hovering, cards transition to `border-color: #38BDF8` with a subtle, low-opacity ambient black shadow (`rgba(0,0,0,0.5)`).

---

## 3. Structural Page Frameworks

### A. Navigation Shell (Sticky Sidebar / Nav Bar)
*   **Desktop Layout:** Fixed left sidebar (`width: 64` / `16rem`) spanning full viewport height (`h-screen`). 
    *   *Top Section:* Brand Name (`Executive Intelligence` or name header `CA Priyam Gupta`) in `font-headline-md` with strict tracking.
    *   *Middle Section:* Vertical nav links with active indicator (Steel blue-grey background tint `primary-container/10` and bold text). Hovering links triggers `bg-surface-variant` with a scaling press-effect (`active:scale-95`).
    *   *Footer Section:* Compact legal disclaimer and settings/support links.
*   **Mobile Layout:** Collapsible hamburger menu or a sticky top bar (`h-16`) utilizing backdrop blur (`bg-surface/80 backdrop-blur-md`) with borders separating it from contents.

### B. Core Grid Structures
*   **Desktop Grid:** Standard 12-column grid.
    *   *Dashboard / Home:* Two-column asymmetric layout (1/3 image profile on left, 2/3 bio, text and metrics on right).
    *   *Competencies Page:* 4-column symmetric grid (`grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4`).
*   **Mobile Grid:** Single column layout (`grid-cols-1`), expanding dynamically to double columns on tablet (`md:grid-cols-2`).

---

## 4. Card & Component Setups

### A. Professional Experience Timeline Card
*   **Visual Structure:**
    *   A vertical timeline line (`width: 1px`, color: `#27272A`) runs down the page.
    *   Each experience item features an absolute-positioned marker:
        *   *Current / Active Role:* 8px square marker in sky-blue (`#38BDF8`).
        *   *Past Roles:* 8px square marker in grey (`#27272A`).
    *   The card itself has transparent background, `1px solid #27272A` border, and sharp corners.
    *   Bullet points are separated by a steel blue slash icon (`/`).
*   **Interactive State:** Hovering over the timeline card expands structural bullet details and shifts the border color to sky-blue (`#38BDF8`).

### B. Core Competency Category Card
*   **Visual Structure:**
    *   Framed card with `bg-surface-container` background and `border border-outline-variant`.
    *   Bold title header specifying the category (e.g., *Auditing & Assurance*).
    *   Grid of skill pills within each card:
        *   Pill Style: `px-3 py-1 bg-primary-container/10 text-[#38BDF8] text-sm font-medium rounded-full` (or zero-radius badges depending on aesthetic alignment).
*   **Aesthetics:** Low-contrast grid that keeps tool stacks clean, maintaining consistent box size per category.

### C. Network Inquiry Form
*   **Fields & Setup:**
    *   A stacked single-column input form.
    *   Inputs: Transparent background, `1px solid #27272A` borders, text color `#F4F4F5`, placeholder text at low opacity (30%).
    *   Focused state: Highlights input border to sky-blue (`#38BDF8`).
    *   Submit Button: Full-width, solid light zinc background (`#F4F4F5`) with deep dark text (`#0B192C`), sharp corners, and uppercase letter-spaced label (`font-label-caps`).

---

## 5. Visual Placeholder Note & Django API Model Overrides

> [!IMPORTANT]
> **DYNAMIC OVERRIDE NOTICE:**
> All image frames, profile headshots, text blocks, project timeline narratives, and competency lists displayed in the active Stitch canvas templates are **strictly visual placeholders**. During Phase 6, all front-facing content will be dynamically hydrated and overridden by corporate data structures managed via our Django API database models:
> *   `Profile` model overrides basic biographical texts, headings, and profile pictures.
> *   `Experience` model overrides timeline entries (Role, Company, Tenures, Achievements).
> *   `Education` model overrides academic credentials.
> *   `ProfessionalSkill` model overrides competencies categories and skill tags.
> *   `ContactMessage` model overrides the submit actions for the network inquiry forms.

---

## 6. ICAI Compliance Guidelines & Design Constraints

To maintain 100% compliance with the **ICAI Code of Ethics (13th Edition)** for Chartered Accountants, the frontend implementation must adhere to the following strict constraints, overriding generic template placeholders:

1.  **No Service Solicitation:** Visual sections indicating consulting services or commercial pricing must be omitted. General contact forms must be framed strictly for "Executive Recruitment," "Networking," or "Professional Inquiry."
2.  **No Commercial CTAs:** Buttons such as "Book a Consultation", "Get a Quote", or calendar scheduling widgets (present in generic layouts) are **prohibited** and must not be implemented.
3.  **No Testimonials or Reviews:** Client feedback lists or endorsement sections must not exist.
4.  **No Self-Laudatory Marketing:** All profile taglines and bios must remain purely factual (e.g., using "Chartered Accountant & CS Professional" instead of marketing adjectives like "Expert," "Top-tier," or "Leading").
5.  **No Client Logos:** Only logos/names of the CA firms where the practitioner was employed (e.g., Gaurav G Agrawal & Co.) are permitted. Corporate client logos must not be shown.
