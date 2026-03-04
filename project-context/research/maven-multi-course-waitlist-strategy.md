# Maven Multi-Course Waitlist Strategy

**Context:** Bronze (Learn AAMAD), Silver (Agentic Architect 101), and Gold (Become an Agentic Architect) create three potential Maven courses, each with its own waitlist. Managing three separate lists adds operational overhead and fragments communication.

**Research date:** 2026-03-02  
**Source:** Maven Help Center, Brevo docs, project-context analysis

---

## The Problem

| Tier | Platform | Waitlist |
|------|----------|----------|
| Bronze | Learn AAMAD (GitHub Pages) or Maven | Separate list if on Maven |
| Silver | Maven (if created) | Per-course waitlist |
| Gold | Maven | Per-course waitlist (~1,899) |

**Maven behavior:** Each Maven course has its own waitlist. There is no documented way to merge waitlists or send a single broadcast across multiple courses. Maven uses Brevo for email; lists appear to be course-specific.

---

## Option A: Gold Waitlist as Single Communication Channel (Recommended)

**Idea:** Route all acquisition (Bronze, Silver, Gold) into the **Gold course waitlist** and use it as the only broadcast channel.

**Constraint:** Maven does not support bulk add to waitlist. Manual add is possible but not scalable.

### Primary Approach: Lead Magnets + Lightning Lessons (Organic Flow)

**Lead Magnets and Lightning Lessons are mapped to the Gold course in Maven.** When Bronze or Silver communication promotes these resources, students who signal interest join the Gold waitlist **organically** — no manual add required.

| Resource | Mapped to | Bronze/Silver CTA |
|----------|-----------|-------------------|
| Lead Magnets (e.g. Agentic Architect Playbook, SDLC patterns) | Gold | "Get the Playbook" / "Download the 4 Patterns" → gated resource adds to Gold waitlist |
| Lightning Lessons | Gold | "Join our next Lightning Lesson" → LL signup adds to Gold waitlist |

**Implementation:**

1. **Bronze (Learn AAMAD):**
   - In Bronze communication (Learn AAMAD page, post-completion email): "Want the Agentic Architect Playbook?" / "Join our next Lightning Lesson" → link to **Gold-mapped Lead Magnet or LL**.
   - Bronze visitors who want these resources sign up → join Gold waitlist organically.

2. **Silver:**
   - In Silver communication (LP, post-enrollment, emails): "Get the Playbook" / "Join our Lightning Lesson on [topic]" → link to **Gold-mapped LM or LL**.
   - Silver signups who want these resources → join Gold waitlist organically.

3. **Gold:**
   - Primary waitlist. All broadcasts go from Gold.
   - Messaging: "Learning Roadmap" — Bronze (free) → Silver ($399) → Gold ($1,995).

**Key:** Ensure all Lead Magnets and Lightning Lessons used in Bronze/Silver comms are **mapped to the Gold course** in Maven, so signups flow to Gold waitlist automatically.

### Fallback: Manual Add

For contacts who don't come through LM or LL (e.g. direct Bronze/Silver enrollment without engaging those CTAs), manual add to Gold waitlist remains an option — but the LM/LL approach minimizes this.

### Pros

- No bulk add needed; organic flow via existing Maven mechanics
- Single list, single broadcast tool
- Value exchange: people get LM/LL content in return for joining
- Bronze/Silver signups who engage get full roadmap visibility

---

## Option B: External ESP as Master (Brevo, ConvertKit, etc.)

**Idea:** Use an external email tool as the single source of truth. Export from Maven, add Bronze/Silver signups, send from external tool.

### How to Implement

- Export Gold waitlist from Maven (Students tab → export if available)
- Add Bronze signups (from Learn AAMAD form) and Silver signups to same list
- Send campaigns from Brevo/ConvertKit instead of Maven
- Tag contacts by source (Bronze, Silver, Gold) for segmentation

### Pros

- Full control; segmentation; A/B testing
- No dependency on Maven broadcast features

### Cons

- Maven cohort launch campaigns may expect Maven-native sends
- Double management: Maven for enrollment, external for nurture
- Need to confirm Maven exports waitlist (likely yes — project has `waitlist_1899contacts_022426.csv`)

---

## Option C: Minimal Maven Courses

**Idea:** Reduce Maven footprint to limit waitlist fragmentation.

| Tier | On Maven? | Waitlist |
|------|-----------|----------|
| Bronze | No | GitHub form → Gold survey link |
| Silver | Yes (for checkout) or No (Stripe) | If Maven: export + add to Gold. If Stripe: form → Gold survey |
| Gold | Yes | Master list |

- Bronze: Never on Maven. Learn AAMAD stays on GitHub. CTA → Gold survey.
- Silver: Either Maven (for payment) or Stripe + Calendly. In both cases, post-signup CTA: "Join the Gold waitlist" → Gold survey.
- Gold: Only Maven course with active broadcast. All nurture from Gold.

---

## Recommendation

**Use Option A — Lead Magnets + Lightning Lessons as primary organic flow:**

1. **Bronze:** Keep on GitHub Pages. In Bronze comms (Learn AAMAD page, post-completion): promote **Gold-mapped Lead Magnets** and **Lightning Lessons**. Students who want these resources join Gold waitlist organically.
2. **Silver:** In Silver comms (LP, post-enrollment): promote **Gold-mapped Lead Magnets** and **Lightning Lessons**. Same organic flow.
3. **Gold:** Single communication channel. All broadcasts use "Learning Roadmap" framing. Ensure all LM and LL assets used in Bronze/Silver are mapped to Gold in Maven.
4. **Manual add:** Fallback for contacts who don't come through LM/LL.

**Action:** Audit existing Lead Magnets and Lightning Lessons — confirm they are mapped to the Gold course in Maven. Add LM/LL CTAs to Bronze and Silver communication flows.

---

*Created by Riley. 2026-03-02.*
