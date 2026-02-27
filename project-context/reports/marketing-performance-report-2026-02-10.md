# Marketing Performance Report — Become an Agentic Architect

**Report date:** 2026-02-10  
**Prepared by:** Alex (Funnel Operations Manager)  
**Data sources:** `project-context/analysis/raw/` (LP, LL, webhooks, cart CSVs); `project-context/analysis/README.md`; `project-context/analysis/email-broadcast-metrics.csv`; `project-context/final/Abandoned Cart Emails/`  
**Context:** Cohort 3 enrollment closes February 20th, 2026; Cohort 3 starts February 23rd.

---

## Executive summary

| Metric | Finding |
|--------|--------|
| **Funnel health** | Strong top-of-funnel (LP views, waitlist, LL signups); **bottlenecks** at visitor→click (4.9%) and payment initiated→success (28% complete, 46 abandoned). |
| **Conversion** | All-time LP: 2,242 visitors → 109 clicked enroll → 20 purchased. **LP→click 4.9%**, **click→purchase 18.3%**. |
| **Lead capture** | Waitlist ~2,123 joins (webhooks); 2,760 LL signup records; 192 unsubscribes. LLs drive both list growth and a share of enrollments. |
| **Revenue path** | 57 payment initiated, 16 payment success, 46 abandoned — **~28% payment completion**; clear opportunity in checkout recovery. |

**Priority recommendations:** (1) Improve visitor→click with clearer LP value prop and CTA. (2) Reduce checkout abandonment (follow-up, friction, trust). (3) Double down on email + LL share links (highest traffic and conversion). (4) Improve LL→course conversion with post-LL nurture and stronger CTAs.

---

## 1. Funnel overview

### 1.1 Stage definitions (from README)

| Stage | Data location | What we measure |
|-------|----------------|-----------------|
| Awareness / traffic | LP views by source, LP views over time | Where visitors come from, weekly volume |
| Intent (click) | Visitor to purchase funnel | Visitors who clicked “Enroll” |
| Purchase | Purchases over time, webhooks | Payment initiated / success / abandoned |
| Enrolled | Enrolled student detail, webhooks | Cohort enrollment, attribution |

Lead capture (waitlist / LL signups) sits alongside: LL signups feed the waitlist; waitlist is nurtured toward the LP and purchase.

### 1.2 Current funnel snapshot (all-time, from LP + webhooks)

| Step | Count | Rate (from previous) |
|------|-------|----------------------|
| LP visitors | 2,242 | — |
| Clicked Enroll | 109 | **4.9%** (visitor → click) |
| Purchased | 20 | **18.3%** (click → purchase) |
| **Overall visitor → purchase** | 20 | **0.9%** |

**Bottleneck #1:** Only 4.9% of visitors click Enroll — majority drop off at the landing page.  
**Bottleneck #2:** Of those who click, 18.3% purchase — moderate; combined with low click rate, overall conversion is under 1%.

---

## 2. Landing page (LP) performance

### 2.1 Traffic over time

- **Period:** Sep 1, 2025 – Feb 15, 2026 (weekly).
- **Peak weeks:** Jan 26–Feb 1 (475 views), Feb 2–8 (411), Dec 29–Jan 4 (435).
- **Conversion by week:** Payment conversions cluster around cohort launches (e.g. Oct 6–12, Nov 24–30, Dec 29–Jan 4, Jan 5–11, Jan 26–Feb 1, Feb 2–8). Many weeks show 0 conversions despite hundreds of views.
- **Weekly LP→purchase rate:** Ranges 0%–1.7%; best weeks ~1.5–1.7%.

### 2.2 Traffic by source (top drivers)

| Referrer / UTM | Landing page views | Notes |
|----------------|--------------------|--------|
| (direct / untracked) | 589 | Largest single bucket; consider better UTM coverage |
| maven.com, maven, email | 422 | Maven + instructor email is core channel |
| maven.com (no UTM) | 342 | In-app or internal Maven traffic |
| maven.com, instructor, ll_share_link | 302 | **LL share links** — key for lead gen and intent |
| google.com (no UTM) | 170 | Organic search |
| maven.com, instructor_email, email | 127 | Your own email to list |
| linkedin.com, instructor, ll_share_link | 105 | LinkedIn + LL link |
| maven.com, instructor, maven_broadcast_email | 89 | Maven broadcast emails |
| maven.com, instructor, lead_magnet_share_link | 82 | Lead magnets |
| linkedin.com (no UTM) | 72 | LinkedIn organic |

**Takeaway:** Email (Maven + instructor) and **LL share links** (instructor + LinkedIn) drive the most traffic. Lead magnets and LinkedIn are meaningful. Double down on these; improve tagging for “direct” and “google.com” to see true source.

---

## 3. Conversion and purchase behavior

### 3.1 Purchases over time (weekly)

- Purchases occur in **9 weeks** (Oct 6–12, Oct 13–19, Nov 24–30, Dec 29–Jan 4, Jan 5–11, Jan 26–Feb 1, Feb 2–8, Feb 9–15).
- **Total unique purchasers in export:** 20 (matches funnel “Purchased” count).
- Heaviest purchase weeks: Jan 26–Feb 1 (5), Oct 6–12 and Jan 5–11 (3 each).

### 3.2 Enrolled students (detail)

- **27 enrollment records** in `enrolled_student_detail` (some students in multiple cohorts, e.g. free then paid).
- **Cohorts:** 1–4; mix of **paid** and **free** (comp/scholarship).
- **Attribution (Email Source):** Lightning Lesson (majority), Lead magnet, Payment started, Course waitlist join, Other.
- **Attribution category:** Mostly `maven_marketplace`, then `instructor_marketing`, `instructor_list_upload`, `instructor_untracked`, `instructor_product_marketing`.
- **Promo usage:** C3-SCHOLARSHIP-50, EarlyBird35, EB2, AAMAD50, BFRIDAY, HL90, etc. — promos are used and matter for conversion.

---

## 4. Lightning Lessons (LL) — lead capture and conversion

### 4.1 Per-workshop performance (signups, attendance, enrollment)

| Workshop (sample) | Total signups | Attended | Attendance rate | Enrolled | LL→course conversion |
|-------------------|---------------|----------|------------------|----------|------------------------|
| Build Scalable Multi-agent AI Systems (Jan 21, 2026) | 459 | 61 | 13.9% | 5 | 1.1% |
| From Coder to Architect (Dec 19, 2025) | 281 | 50 | 18.9% | **6** | **2.1%** |
| Build your Agentic Work Crew – Non-Technical (Feb 12, 2026) | 224 | 10 | 4.5% | 0 | 0% |
| Go from Idea to Deployed Multi-Agent App (Aug 26, 2025) | 342 | 69 | 24.2% | 3 | 0.9% |
| Advanced Prompt Engineering & Agent Personas (Sep 29, 2025) | 210 | 48 | 28.7% | **4** | **1.9%** |
| Engineer Effective Context Systems (Feb 4, 2026) | 48 | 12 | 25.5% | 1 | 2.1% |
| Quantify the ROI… (Feb 11, 2026) | 56 | 3 | 5.4% | 0 | 0% |
| Launch a Production Agentic Application (Feb 18, 2026) | 75 | 2 | 2.7% | 0 | 0% |

- **LL→course conversion** is low overall (0–2.1%); best performers are “From Coder to Architect” and “Advanced Prompt Engineering.”
- **Attendance** varies widely (2.7%–33.3%); several recent LLs have very low attendance (e.g. Non-Technical, Quantify ROI, Launch Production).
- **LL signup volume** is strong (2,760 lead-level records); the gap is signup→attend→enroll.

### 4.2 LL as lead source

- LL signups = **waitlist adds**; they feed email nurture.
- Source in data: `workshop_list_join`, `post_workshop_list_join` — both valuable for list growth and retargeting.

---

## 5. Waitlist and payment events (webhooks)

| Event | Count | Note |
|-------|-------|------|
| waitlist.joined | 2,123 | Strong list growth |
| waitlist.unsubscribed | 192 | ~9% churn of join events |
| payment.initiated | 57 | Started checkout |
| payment.abandoned | 46 | **Major drop-off** |
| payment.success | 16 | Completed payment |
| user_cohort.enrolled | 20 | Enrolled into cohort |
| user_cohort.removed | 7 | Removed from cohort |

**Payment funnel (from webhooks):**  
57 initiated → 16 success + 46 abandoned (+ 7 removed). **Completion rate ~28%** (16/57); **abandonment ~81%** (46/57).  
*(Note: enrolled count can differ from payment.success due to timing, free enrolls, or manual cohort adds.)*

**Bottleneck #3:** Checkout abandonment is the largest leak between “intent” and “customer.” Maven's automatic abandoned-payment recovery sequence (see §5.1) is in place to recapture a portion of these.

### 5.1 Abandoned payment recovery sequence (Maven automatic)

Maven sends an automatic email sequence when a student doesn't complete checkout. Copy lives in `project-context/final/Abandoned Cart Emails/` (email1–email4). Cumulative performance (snapshot 2026-02-10) is stored in `project-context/analysis/raw/cart/abandoned_payment_sequence_performance_2026-02-10.csv`.

| Subject | Delay | Delivered | Opened | Open rate | Click rate |
|--------|-------|-----------|--------|-----------|------------|
| I'm holding a spot for you | 1 hour | 65 | 38 | 58.5% | 7.7% |
| Still thinking about joining? | 1 day | 59 | 33 | 55.9% | **16.9%** |
| Busy? That's exactly why this was built. | 2 days | 53 | 30 | 56.6% | 9.4% |
| Don't just take my word for it | 4 days | 2 | 1 | 50.0% | 0% |

- **Open rates** are strong (55–58%); **click rate** peaks on the 1-day email (16.9%). The 4-day email has very few deliveries (2) so far — likely most recover or disengage earlier. Use this series to optimize timing and copy (e.g. test variations on the 1-day email).


---

## 6. Email broadcasts (Feb 2026 snapshot)

| Date | Subject (short) | Recipients | Open rate | Click rate |
|------|-----------------|------------|-----------|------------|
| 2026-02-07 | The real cost of "vibe coding" with AI | 1,605 | 36.0% | 1.8% |
| 2026-02-05 | Why I stopped "vibe coding"… | 1,604 | 37.5% | 0.0% |
| 2026-02-05 | Resources from "Engineering Effective Context Systems" | 46 | 54.3% | 4.3% |
| 2026-02-02 | What hundreds of engineers learned… | 1,589 | 37.0% | 1.3% |
| 2026-02-01 | 35% Early Bird discount extended until TONIGHT | 1,595 | 34.9% | 1.6% |

- **Opens:** 35–37% (full list); 54% for segment (LL follow-up). Solid.
- **Clicks:** 0–1.8% for full list; 4.3% for LL follow-up. The 0% click email (“Why I stopped 'vibe coding'…”) had **no link included** (instructor oversight), so that send is not comparable for CTR. For the rest, **click-through remains the main lever** — ensure every broadcast has at least one clear CTA link.

---

## 7. Bottleneck summary

| # | Stage | Observation | Impact |
|---|--------|-------------|--------|
| 1 | Visitor → Click Enroll | 4.9% click rate (109/2,242) | Most visitors leave without clicking; LP or offer may not match intent |
| 2 | Click → Purchase | 18.3% (20/109) | Moderate; could improve with copy, urgency, or trust |
| 3 | Payment initiated → Success | ~28% complete; 46 abandoned | Abandoned-cart sequence is live; optimize copy/timing and checkout friction |
| 4 | LL signup → Attend | Attendance 2.7%–33% by LL | Many sign up but don’t show; weak reminder or topic fit |
| 5 | LL → Course enroll | 0–2.1% per LL | Post-LL nurture and CTA could be stronger |
| 6 | Email → Click | 0–1.8% on full-list sends (one had no link) | Ensure every broadcast has a CTA link; align subject with offer |

---

## 8. Recommendations for performance improvement

### 8.1 High priority (before Cohort 3 close Feb 20)

1. **Increase visitor→click (LP)**  
   - Clarify value prop above the fold: outcome, credibility, “who it’s for.”  
   - Single primary CTA (“Enroll in Cohort 3” / “Save your spot”); reduce competing links.  
   - Test one clear urgency line (e.g. “Cohort 3 closes Feb 20”) and one social proof element (e.g. “X engineers enrolled”).

2. **Reduce checkout abandonment**  
   - Send an automated “cart recovery” email 1–2 hours after payment initiated (if Maven or your ESP supports it).  
   - Review checkout flow: steps, fields, and payment options; shorten if possible.  
   - Add trust elements (guarantee, support contact) near the pay button.

3. **Improve email click-through**  
   - Every broadcast should have one main CTA (e.g. “Enroll now” or “Watch the replay”) with a single, tracked link.  
   - Align subject line and first line with that CTA (e.g. discount + deadline).  
   - Segment: send a “Cohort 3 closing soon” version to recent LL signups and high-intent segments.

### 8.2 Medium priority (next 2–4 weeks)

4. **LL→course conversion**  
   - Send a dedicated post-LL sequence: recap + “Enroll in the full course” + testimonial or outcome.  
   - In-LL CTA: one clear “Next step: join Cohort 3” with link and deadline.  
   - Replicate topics and positioning of best-converting LLs (“From Coder to Architect,” “Advanced Prompt Engineering”) in future LLs and in email.

5. **LL attendance**  
   - Reminder sequence: 24h and 1h before start; calendar link and “Add to calendar.”  
   - Consider a short “what you’ll learn” or teaser email to reduce no-shows for low-attendance LLs.

6. **Traffic attribution**  
   - Use UTMs on all links (email, LinkedIn, lead magnets) so “direct” and “google.com” break out by campaign.  
   - In README/clean tables, group by `utm_source` / `utm_medium` for reporting.

### 8.3 Ongoing / tracking

7. **Implement clean tables (README §2)**  
   - Build the seven clean tables (e.g. `landing_page_views_weekly`, `visitor_to_purchase_funnel`, `ll_performance`, etc.) so weekly or cohort-over-cohort comparison is easy and consistent.

8. **Track cohort-over-cohort**  
   - Compare Cohort 2 vs 3 (and 1 vs 2) on: LP views, click rate, purchases, LL signups, payment abandonment.  
   - Store one snapshot per cohort (e.g. funnel counts, top 10 sources) for trend reports.

9. **Promo and pricing**  
   - Enrolled-student detail shows heavy use of promos (C3-SCHOLARSHIP-50, EarlyBird35, etc.). Track which promos and price points correlate with payment success vs abandonment to optimize next cohort.

---

## 9. Data and report notes

- **LP funnel:** From `visitor_to_purchase_funnel_*.csv` (all-time). Visitor count is 2,242; Clicked Enroll 109; Purchased 20.
- **Traffic:** From `landing_page_views_over_time_*.csv` and `landing_page_views_by_tracked_source_*.csv`.
- **Webhooks:** From `Maven Course Become an Agentic Architect - Maven Webhooks.csv`; event counts as of file export.
- **Enrolled students:** From `enrolled_student_detail_*.csv` (27 rows; some repeat enrollments across cohorts).
- **LL:** From `lightning_lesson_signups_and_performance_*.csv` and `lightning_lessons_student_signups_*.csv`.
- **Email:** From `project-context/analysis/email-broadcast-metrics.csv` (Feb 2026).
- **Abandoned payment sequence:** From `project-context/analysis/raw/cart/abandoned_payment_sequence_performance_2026-02-10.csv`; email copy in `project-context/final/Abandoned Cart Emails/`.

If you want a deeper dive on any section (e.g. only LL, only checkout, or cohort comparison), say which and I can produce a focused addendum or an updated slice after new exports.

---

*End of report. Alex — Funnel Operations Manager.*
