# Weekly Report — Standard Operating Instructions

**Owner:** Alex (Funnel Operations Manager)  
**Frequency:** Weekly (Saturday evening)  
**Output location:** `project-context/reports/weekly-report-YYYY-MM-DD.md`

---

## Purpose

Produce a weekly performance report that measures all marketing activities against the enrollment objectives defined in the active conversion plan. The report serves as the single source of truth for what happened, what worked, what didn't, and what to do next.

---

## Pre-Report Checklist

Before generating the report, gather all data sources:

### 1. Context Files (Always Read First)
- [ ] `AGENTS.md` — current priorities, deadlines, crew roster
- [ ] `STATUS.md` — actions completed during the week, notifications
- [ ] Active conversion plan (e.g., `project-context/plans/cohort3-10days-conversion-plan.md`)

### 2. Landing Page Analytics
- [ ] Download 5 CSV files from Maven analytics dashboard and save to `project-context/analysis/raw/LP/` with today's date:
  1. `visitor_to_purchase_funnel_YYYY-MM-DDTHH_MM_SS.csv`
  2. `purchases_over_time_YYYY-MM-DDTHH_MM_SS.csv`
  3. `landing_page_views_over_time_YYYY-MM-DDTHH_MM_SS.csv`
  4. `landing_page_views_by_tracked_source_YYYY-MM-DDTHH_MM_SS.csv`
  5. `enrolled_student_detail_YYYY-MM-DDTHH_MM_SS.csv`
- [ ] Locate the same 5 CSVs from the previous week's snapshot for comparison

### 3. Lightning Lesson Analytics
- [ ] Download from Maven and save to `project-context/analysis/raw/LL/`:
  1. `lightning_lesson_signups_and_performance_YYYY-MM-DDTHH_MM_SS.csv`
  2. `lightning_lessons_student_signups_YYYY-MM-DDTHH_MM_SS.csv`

### 4. Abandoned Cart Data
- [ ] Download from Maven and save to `project-context/analysis/raw/cart/`:
  - Active cohort contact lists (e.g., `Become an Agentic Architect_3_XX-contacts_YYYY-MM-DD.csv`)
- [ ] Capture screenshot of the abandoned cart email sequence performance from Maven dashboard
- [ ] If available, compare with previous abandoned cart performance snapshot (e.g., `abandoned_payment_sequence_performance_YYYY-MM-DD.csv`)

### 5. Broadcast Email Performance
- [ ] Capture screenshots of each email sent this week from the Maven email dashboard (showing delivered, opened, open rate, click rate)
- [ ] Note any planned emails that were NOT sent

### 6. LinkedIn Post Analytics
- [ ] List all LinkedIn posts published during the week
- [ ] For each post, record: post theme, date, reactions count, comments count, CTA/link
- [ ] Note the LinkedIn post URLs for reference

### 7. Waitlist Monitoring
- [ ] Download latest waitlist export from Maven (course waitlist / lead list) and save to `project-context/analysis/raw/waitlist/` with a clear date in the filename (e.g. `Become an Agentic Architect_waitlist_XXXXcontacts_MMDDYY.csv`)
- [ ] Locate the previous week's waitlist snapshot in the same folder for comparison

### 8. Other Activities
- [ ] Note any newsletter articles published
- [ ] Note any lead magnets created or promoted
- [ ] Note any external events, partnerships, or mentions

---

## Report Structure

The weekly report MUST include all of the following sections:

### Section 1: Executive Summary (3–5 sentences)
- Total activities executed
- Key enrollment result (new enrollments this week)
- Gap vs target
- One-sentence assessment of trajectory

### Section 2: Enrollment Performance
- **Current state table:** Compare previous snapshot vs current (enrolled students, new enrollments)
- **Cohort breakdown:** List enrolled students per cohort with date, amount paid, promo code
- **Progress vs goal:** Target, achieved, remaining, RAG status
- **Abandoned cart pipeline:** Count by status (enrolled vs interested) and source
- **Abandoned cart email sequence performance:** Table with subject, timing, delivered, opened, open rate, click rate
- **Comparison vs previous sequence:** Side-by-side metrics if sequence was updated

### Section 3: Landing Page Performance
- **Funnel comparison table:** Visitors, clicks, purchases, conversion rates (previous vs current)
- **Weekly LP views trend:** Table showing views, purchases, conversion by week
- **Top traffic sources:** Table with notable changes in referral sources
- **Assessment:** Did any LP changes produce measurable lift?

### Section 4: Lightning Lessons Performance
- **This week's sessions:** Table with signups, attended, attendance rate, conversion
- **Upcoming sessions:** Signups count and growth
- **Historical benchmark:** Compare with top-performing past LLs
- **Follow-up sequences status:** What's sent, what's scheduled, what's missing

### Section 5: Broadcast Email Performance
- **Emails sent table:** Subject, audience, date, delivered, opened, open rate, click rate
- **Emails planned but NOT sent:** Table with planned date, owner, status
- **Gap assessment:** Which missed emails had the highest potential impact?

### Section 6: LinkedIn Performance
- **Posts published table:** Theme, date, reactions, comments, CTA
- **Key findings:** Top performers, engagement trends, traffic impact
- **Missing planned posts:** What was planned but not published?

### Section 7: Plan Execution Scorecard
- **Actions completed:** Table with action, owner, date, plan reference
- **Actions NOT completed:** Table with action, owner, planned date, impact level (RED/YELLOW/GREEN)
- **Execution rate:** Planned vs completed percentage

### Section 8: Risk Assessment & Recommendations
- **Critical risks (RED):** Immediate threats to enrollment goal
- **Moderate risks (YELLOW):** Issues that need attention soon
- **Recommended priority actions:** Table with priority level, action, owner, date, rationale

### Section 9: Waitlist Monitoring
- **Snapshot comparison:** Previous vs current waitlist total, net growth, growth rate
- **Breakdown by source:** Table of contact count by source (e.g. Lightning Lesson, Downloaded lead magnet, Started payment, Waitlist/direct)
- **Assessment:** Trend vs enrollment goal, quality of new signups (e.g. Started payment as high-intent), any recommended actions

### Section 10: Key Metrics Summary
- **Dashboard table:** Key metrics with baseline, current, target, RAG status
- Include: enrolled students, new enrollments, LP visitors, LP conversion rate, waitlist size, LL signups, abandoned cart pipeline, broadcast emails sent

---

## Data Analysis Instructions

### Waitlist Analysis
1. Read the latest waitlist CSV from `project-context/analysis/raw/waitlist/` (filename usually includes contact count and date, e.g. `*_021626.csv` = Feb 16, 2026).
2. Identify the previous snapshot (e.g. same folder, earlier date) for comparison.
3. Compare total contact count: current vs previous; compute net growth and, if useful, growth rate over the period.
4. If the CSV has a `source` (or similar) column, count contacts by source (e.g. Lightning Lesson, Downloaded lead magnet resource, Started payment, Waitlist) and summarize in a table.
5. Note how many contacts are high-intent (e.g. Started payment) vs top-of-funnel (e.g. Lightning Lesson, lead magnet); relate to enrollment pipeline and broadcast reach.

### Landing Page Comparison
1. Read the `visitor_to_purchase_funnel` CSV from both dates
2. Calculate: visitor-to-click rate, click-to-purchase rate, visitor-to-purchase rate
3. Compute deltas (absolute and percentage)
4. Read `landing_page_views_over_time` from both dates
5. Compare the current week row (views will be higher in the newer snapshot for the same partial week)
6. Read `landing_page_views_by_tracked_source` from both dates
7. Identify top 10 sources by volume and compute changes

### Lightning Lesson Analysis
1. Read `lightning_lesson_signups_and_performance` CSV
2. For this week's LLs: extract signups, attended, attendance rate, conversion rate
3. Compare with historical average and top performers
4. Read `lightning_lessons_student_signups` CSV
5. Count new signups per LL by day to assess momentum

### Enrollment Analysis
1. Read `enrolled_student_detail` from both dates
2. Identify any new rows (new enrollments)
3. Cross-reference with cohort-specific cart CSVs for pipeline status
4. Count "interested" contacts by source (Started payment, Lightning Lesson, Waitlist, Lead magnet)

### Abandoned Cart Sequence Analysis
1. Compare current screenshot metrics with previous performance CSV
2. Calculate open rate and click rate changes per email
3. Flag any emails with 0 deliveries (potential config issues)

---

## Post-Report Actions

After the report is complete:
1. [ ] Save report to `project-context/reports/weekly-report-YYYY-MM-DD.md`
2. [ ] Update `STATUS.md` with report completion notification
3. [ ] Highlight any P0 recommendations that need immediate human decision
4. [ ] If enrollment is behind target, propose an emergency action plan

---

## Schedule

| Day | Action |
|-----|--------|
| Sunday PM | Carmelo exports all CSV data from Maven dashboard |
| Monday AM | Alex generates weekly report (full week view: Mon–Sun) |
| Monday AM | Carmelo reviews report and approves/adjusts recommendations |
| Monday PM | Crew executes P0 actions from recommendations |

---

*Created: 2026-02-14. Update this document if report requirements change.*
