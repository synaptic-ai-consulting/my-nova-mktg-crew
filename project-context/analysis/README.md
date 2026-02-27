# Maven course analytics — analysis plan

This folder holds **raw exports** from the Maven Course Analytics (Metabase) dashboard and the **plan** for turning them into clean, analysis-ready tables. Raw files are organized by funnel stage: **LP** (landing page / course conversion) and **LL** (Lightning Lessons / lead capture).

---

## Why the LP and LL datasets matter

**Landing page (LP):** All marketing efforts drive users to the **course landing page** for conversion. The five LP exports measure traffic, click-to-enroll, and purchases — the core **marketing performance** from top-of-funnel to conversion.

**Lightning Lessons (LL):** LLs are free 30-minute sessions and the **main vehicle to capture new leads**. Anyone who signs up for an LL is automatically added to your **course waitlist** (the email list used to nurture prospects toward the bottom of the funnel). The two LL exports measure how many people sign up per workshop and who those leads are — critical for **lead acquisition** and funnel health.

| Funnel stage | Folder | What we measure |
|--------------|--------|-----------------|
| **LP — traffic & conversion** | `raw/LP/` | Visitors to LP, LP conversion (click-to-enroll), enroll-page conversion (purchased), enrolled students |
| **LL — lead capture** | `raw/LL/` | Signups per Lightning Lesson, attendance, LL→course conversion; plus lead-level signup list (waitlist growth) |
| **Webhooks — waitlist & payment events** | `raw/webhooks/` | Real-time Maven events: waitlist joins/unsubscribes, payment initiated/abandoned/success, cohort enrollment (manual CSV export from Google Sheet) |

---

## 1. Raw data (`raw/`)

**Source:** Maven → Course Analytics BETA (and Lightning Lesson analytics where applicable) → per-chart “⋯ → Download results” (CSV).

**Filename pattern (as exported by Maven):** `{table_name}_{timestamp}.csv`

### 1.1 LP — Course landing page & conversion (`raw/LP/`)

| File | Maven chart | Rows (approx) |
|------|-------------|----------------|
| `landing_page_views_over_time_*.csv` | Landing Page Views Over Time | ~25 (weekly) |
| `landing_page_views_by_tracked_source_*.csv` | Landing Page Views by Tracked Source | ~416 |
| `purchases_over_time_*.csv` | Purchases Over Time | ~10 (weekly) |
| `visitor_to_purchase_funnel_*.csv` | Visitor to Purchase Funnel | 3 (Visitors, Clicked Enroll, Purchased) |
| `enrolled_student_detail_*.csv` | Enrolled Student Detail | ~27 |

**Note:** LP exports are tied to the **cohort** and date filter selected in the Analytics UI when you download.

### 1.2 LL — Lightning Lessons (`raw/LL/`)

| File | Maven chart / source | Rows (approx) |
|------|----------------------|----------------|
| `lightning_lesson_signups_and_performance_*.csv` | Lightning Lesson signups and performance (aggregate per workshop) | ~14 (one per LL) |
| `lightning_lessons_student_signups_*.csv` | Lightning Lessons student signups (one row per signup = lead added to waitlist) | ~2,700+ |

**LL aggregate columns:** `WORKSHOP_TITLE`, `WORKSHOP_START_DATE`, `URL`, `LIVE_SIGNUPS`, `ON_DEMAND_SIGNUPS`, `ATTENDED_USERS`, `TOTAL_SIGNUPS`, `ENROLLED`, `ATTENDANCE_RATE`, `CONVERSION_RATE`.

**LL signup (lead-level) columns:** `Email`, `Lightning Lessons Name`, `URL`, `Source` (e.g. `workshop_list_join`, `post_workshop_list_join`), `Created At: Day`, `Attended Live`.

### 1.3 Webhooks — Waitlist & payment events (`raw/webhooks/`)

**Source:** A Google Sheet whose “Maven Webhooks” tab is populated by a Maven webhook. The sheet is exported manually as CSV and saved here (e.g. `Maven Course Become an Agentic Architect - Maven Webhooks.csv`).

**Columns:** `Timestamp`, `Event`, `Course`, `Cohort`, `User Name`, `Email`, `Payment Amount`, `Raw JSON`.

**Event types (typical counts):** `waitlist.joined` (leads added to waitlist), `waitlist.unsubscribed`, `payment.initiated`, `payment.abandoned`, `payment.success`, `user_cohort.enrolled`, `user_cohort.removed`. Cohort is often empty for waitlist events and set (e.g. 3, 4) for payment/enrollment. `Payment Amount` is filled for `payment.success`.

**Why it matters:** Complements LP and LL data by giving a direct feed of waitlist growth, drop-off (unsubscribes), and the funnel from waitlist → payment started → payment success / enrollment. Use for time-series of joins/unsubscribes and conversion from waitlist to paid.

---

## 2. Clean tables we will produce

Once raw CSVs are in `raw/LP/` and `raw/LL/`, we transform them into these **analysis-ready** assets (in this folder or a `clean/` subfolder).

### LP — Landing page & conversion

### 2.1 `landing_page_views_weekly`

- **Source:** `raw/LP/landing_page_views_over_time_*.csv`
- **Goal:** One row per (week, cohort) with views and conversion.
- **Raw columns used:** `CLIENT_EVENT_TIME: Week`, `Landing Page Views`, `Payment Conversions`, `% Purchase Conversion`
- **Transforms:** Parse week range into `week_start` (date), normalize column names to snake_case, add `cohort` / `export_date` from filename or context.

### 2.2 `landing_page_views_by_source`

- **Source:** `raw/LP/landing_page_views_by_tracked_source_*.csv`
- **Goal:** One row per (referrer_domain, utm_source, utm_medium, cohort) for “what’s driving traffic?”
- **Raw columns used:** `Referrer_Domain`, `UTM_Source`, `UTM_Medium`, `Landing Page Views`
- **Transforms:** Standardize null/empty to a consistent value, snake_case column names, add `cohort` and `export_date`.

### 2.3 `purchases_over_time` (weekly)

- **Source:** `raw/LP/purchases_over_time_*.csv`
- **Goal:** One row per (week, cohort) with purchase counts and unique purchasers — when conversions happen.
- **Raw columns used:** `CLIENT_EVENT_TIME: Week`, `Purchases`, `Unique Users`
- **Transforms:** Parse week range into `week_start` (date), snake_case column names, add `cohort` and `export_date`.

### 2.4 `visitor_to_purchase_funnel`

- **Source:** `raw/LP/visitor_to_purchase_funnel_*.csv`
- **Goal:** One row per funnel step (Visitors, Clicked Enroll, Purchased) with count and derived conversion rates — LP conversion (visitors → click) and enroll-page conversion (click → purchase).
- **Raw columns used:** `Count`, `Step`
- **Transforms:** Parse counts (handle comma-separated numbers), pivot or normalize so we have `step`, `count`, and optionally `conversion_rate` / `conversion_from_previous`. Add `cohort` and `export_date` for snapshot-over-time comparison.

### 2.5 `enrolled_students` (or `enrollments`)

- **Source:** `raw/LP/enrolled_student_detail_*.csv`
- **Goal:** One row per enrolled student per cohort: who enrolled, when, acquisition source, promo, refund status.
- **Raw columns used:** `Email`, `Enrolled`, `Email Join`, `Days Between`, `Email Source`, `Attribution Category`, `Cohort Name`, `Enroll Type`, `Refunded?`, plus optional fields (e.g. promo code, amount paid, goals).
- **Transforms:** Normalize dates to YYYY-MM-DD, map source/attribution to a unified `acquisition_channel` if useful, add `export_date`, optionally flag repeat students.

### LL — Lightning Lessons (lead capture)

### 2.6 `ll_performance` (per-workshop aggregates)

- **Source:** `raw/LL/lightning_lesson_signups_and_performance_*.csv`
- **Goal:** One row per Lightning Lesson: title, date, URL, signups (live vs on-demand), attendance, and conversion to course enrollment — which LLs drive the most waitlist growth and enrollments.
- **Raw columns used:** `WORKSHOP_TITLE`, `WORKSHOP_START_DATE`, `URL`, `LIVE_SIGNUPS`, `ON_DEMAND_SIGNUPS`, `ATTENDED_USERS`, `TOTAL_SIGNUPS`, `ENROLLED`, `ATTENDANCE_RATE`, `CONVERSION_RATE`
- **Transforms:** Parse dates to YYYY-MM-DD, snake_case column names, add `export_date`. Optionally compute derived fields (e.g. enrollment rate from signups).

### 2.7 `ll_signups` (lead-level: waitlist adds)

- **Source:** `raw/LL/lightning_lessons_student_signups_*.csv`
- **Goal:** One row per signup = one lead added to the course waitlist. Enables counting unique leads per LL, over time, and by source (e.g. `workshop_list_join` vs `post_workshop_list_join`).
- **Raw columns used:** `Email`, `Lightning Lessons Name`, `URL`, `Source`, `Created At: Day`, `Attended Live`
- **Transforms:** Normalize dates to YYYY-MM-DD, snake_case column names, add `export_date`. Dedupe by (Email, Lightning Lesson) if the same person signs up for multiple LLs or we merge multiple exports.

---

## 3. Other assets in this folder

- **`email-broadcast-metrics.csv`** — Manual tracking of email broadcast performance (opens, clicks, recipients). Not from Metabase; updated when you capture broadcast stats (e.g. from Maven Emails or your ESP).

---

## 4. Next steps

1. **Re-export when needed:** Re-download the 5 LP CSVs and the 2 LL CSVs from the Analytics page (e.g. after a new cohort, new LL, or date range) and replace or add files in `raw/LP/` and `raw/LL/`. Export the Maven Webhooks sheet to CSV and save in `raw/webhooks/` when you want to refresh waitlist/payment event data.
2. **Other cohorts (LP):** If you export the same 5 LP charts for a different cohort, add those files to `raw/LP/`; we use filename or a `cohort` column so clean tables can combine or compare cohorts.
3. **Implement transforms:** Apply the clean-table logic above (script or manual steps) so we have the seven clean tables (LP: `landing_page_views_weekly`, `landing_page_views_by_source`, `purchases_over_time`, `visitor_to_purchase_funnel`, `enrolled_students`; LL: `ll_performance`, `ll_signups`) ready for funnel and lead-capture analysis and reporting.

---

*Last updated: 2026-02-10*
