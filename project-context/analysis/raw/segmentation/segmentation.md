### F1: HCP Score Calculator
**Description:** Calculate High Conversion Propensity score based on engagement signals

**User Story:**  
As a marketing analyst, I need an automated score to identify my hottest leads so I can prioritize outreach.

**Tasks:**
1. Define scoring algorithm with weighted factors
2. Calculate email engagement score (opens, clicks, frequency)
3. Calculate behavioral intent score (lead magnet, payment attempts)
4. Calculate profile completeness score
5. Calculate recency score (days since last activity)
6. Combine into composite HCP score (0-100)
7. Add score to each prospect record

**Acceptance Criteria:**
- ✓ Every prospect has HCP score 0-100
- ✓ Score formula is transparent and adjustable
- ✓ Scores correlate with intuitive conversion readiness

**Scoring Formula:**

#### 1. Email Engagement (Weight: 35%)
- Total clicks: 5 pts each (max 25 pts)
- Total opens: 2 pts each (max 20 pts)
- Unique emails received: 1 pt each (max 10 pts)
- **Subtotal: 55 pts → Normalized to 35%**

#### 2. Behavioral Intent (Weight: 40%)
- Payment initiated: 40 pts
- Lead magnet download: 30 pts
- Lightning Lesson participation: 15 pts
- Waitlist joined: 10 pts
- **Subtotal: Up to 40 pts (highest signal wins)**

#### 3. Profile Completeness (Weight: 10%)
- Has name: 3 pts
- Has company: 3 pts
- Has job title: 2 pts
- Has LinkedIn: 2 pts
- **Subtotal: 10 pts**

#### 4. Recency (Weight: 15%)
- Active in last 7 days: 15 pts
- Active in last 14 days: 10 pts
- Active in last 30 days: 5 pts
- Older than 30 days: 0 pts
- **Subtotal: 15 pts**

**Final Calculation:**
```
HCP Score = (
  (EmailEngagement / 55 * 35) +
  (BehavioralIntent) +
  (ProfileCompleteness) +
  (Recency)
)
```

**Example:**
```
Prospect: rajdippharma1989@gmail.com
- Email: 12 clicks (25 pts), 12 opens (20 pts), 12 emails (10 pts) = 55 pts
- Behavior: Lead magnet downloaded (30 pts)
- Profile: Name + Company + Job (8 pts)
- Recency: Active 2 days ago (15 pts)

HCP Score = (55/55 * 35) + 30 + 8 + 15 = 88/100 → HIGH PRIORITY
```

---

### F2: Segmentation Engine
**Description:** Automatically segment prospects into actionable groups

**User Story:**  
As a marketing analyst, I need prospects automatically sorted into segments so I can execute targeted campaigns.

**Tasks:**
1. Define segment rules based on HCP + behaviors
2. Apply segmentation logic to all prospects
3. Assign segment labels (Urgent, High Intent, Nurture, etc.)
4. Calculate segment sizes
5. Create segment definitions UI

**Acceptance Criteria:**
- ✓ Every prospect assigned to at least one segment
- ✓ Segment sizes shown in dashboard
- ✓ Segment logic is clear and adjustable

**Segment Definitions:**

| Segment | Rule | Typical Size | Action Priority |
|---------|------|--------------|-----------------|
| **Urgent** | HCP > 80 OR Payment Initiated | 2-10 | Immediate (24h) |
| **High Intent** | HCP 60-80 OR Lead Magnet Downloaded | 30-50 | High (1 week) |
| **Engaged Nurture** | HCP 40-60 AND Recent Activity (< 14 days) | 100-150 | Medium (2 weeks) |
| **Cold Nurture** | HCP 20-40 OR No Recent Activity | 200-300 | Low (1 month) |
| **Reactivation** | No activity > 30 days | 100-200 | Specialized |
| **Unsubscribed** | Has unsubscribe event | 25+ | Exclusion list |

**Segmentation Logic:**
```typescript
function assignSegment(prospect: UnifiedProspect): string {
  // Priority order matters - check most urgent first
  
  if (prospect.unsubscribed) {
    return 'Unsubscribed';
  }
  
  if (prospect.hcp_score > 80 || prospect.payment_initiated) {
    return 'Urgent';
  }
  
  if (prospect.hcp_score >= 60 || prospect.lead_magnet_downloaded) {
    return 'High Intent';
  }
  
  if (prospect.hcp_score >= 40 && prospect.days_since_last_activity <= 14) {
    return 'Engaged Nurture';
  }
  
  if (prospect.days_since_last_activity > 30) {
    return 'Reactivation';
  }
  
  return 'Cold Nurture';
}
```

---

## How to Generate and Update the Segmentation

This section is for anyone (including future you) who needs to (re)run the segmentation and produce the tagged waitlist CSV.

### What Gets Generated

- **Output file:** `project-context/analysis/raw/segmentation/waitlist_segmented_YYYY-MM-DD.csv`
- **Content:** One row per waitlist lead with all original waitlist columns plus:
  - **`hcp_score`** — 0–100 (see formula above)
  - **`segment`** — one of: `Urgent` | `High Intent` | `Engaged Nurture` | `Cold Nurture` | `Reactivation` | `Unsubscribed`
  - **`days_since_last_activity`** — days since last qualifying activity (LL signup, cart event, or webhook event), or blank if unknown

A short **README** in the same folder describes the file and caveats.

### Prerequisites: Input Files

The script reads from the **analysis raw folder**. Paths are relative to the repo root.

| Input | Path (under `project-context/analysis/raw/`) | Purpose |
|-------|-----------------------------------------------|---------|
| Waitlist | `waitlist/Become an Agentic Architect_waitlist_*contacts_*.csv` | Base list; `source` and profile fields drive HCP |
| Cart (Cohort 3) | `cart/Become an Agentic Architect_3_*-contacts_*.csv` | Payment-initiated flag (exclude enrolled when loading) |
| Lightning Lesson signups | `LL/lightning_lessons_student_signups_*.csv` | Latest LL signup date per email → recency |
| Webhooks | `webhooks/Maven Course Become an Agentic Architect - Maven Webhooks.csv` | Unsubscribes + last event date per email |

**Important:** The script uses **hardcoded filenames** for the latest exports. When you add new exports (e.g. a new waitlist or cart file), either:

- Replace the files in place so the same names point to the latest data, or  
- Edit the path constants at the top of `scripts/run_segmentation.py` to point to the new filenames.

### How to Run

1. **From the repo root** (required so paths resolve correctly):
   ```bash
   python3 scripts/run_segmentation.py
   ```
2. The script prints segment counts and the path of the written CSV.
3. Output is written to `project-context/analysis/raw/segmentation/`. The filename includes the run date (e.g. `waitlist_segmented_2026-02-21.csv`).

### When to Update

- After exporting a **new waitlist** from Maven.
- After exporting a **new cart** (abandoned / started payment) list.
- After new **LL signups** or **webhooks** exports.
- Before a **targeted outreach push** (e.g. DM campaign) so the Urgent / High Intent lists are current.

### Data Caveats

- **Email engagement:** Per-lead opens and clicks are not available in the raw exports. The script sets the email-engagement component to **0** for all leads. HCP is therefore based only on behavioral intent, profile completeness, and recency. If Maven (or another tool) later provides per-contact open/click data, the script can be extended to use it.
- **Reference date:** “Days since last activity” is computed against a fixed **reference date** (e.g. 2026-02-21) defined in the script. For a fresh run, update that date in `scripts/run_segmentation.py` if you want “today” to match the run date.
- **Unsubscribed:** Unsubscribe events come from the webhooks file. If that export is for a different product or time range, some unsubscribes may be missing.

### Using the Output

- **DM / high-touch outreach:** Filter to `segment` in (`Urgent`, `High Intent`) and `status != enrolled` to get the shortlist for 1:1 messages.
- **Exclusions:** Exclude `segment == 'Unsubscribed'` for any email or DM campaign.
- **Nurture sequencing:** Use `Engaged Nurture` and `Cold Nurture` for lower-touch flows; use `Reactivation` for win-back or specialized sequences.

### Script Location and Customization

- **Script:** `scripts/run_segmentation.py`
- **Logic:** Implements the HCP formula and segment rules from this document. To change weights or segment thresholds, edit the script and keep this plan in sync so the formula and rules stay documented.