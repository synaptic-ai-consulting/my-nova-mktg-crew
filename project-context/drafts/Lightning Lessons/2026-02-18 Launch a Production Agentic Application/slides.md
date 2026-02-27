# Lightning Lesson Slides: Launch a Production Agentic Application
**Date:** February 18, 2026  
**Duration:** 30 minutes  
**Audience:** Technical — software engineers, tech leads, AI/ML engineers  
**Presenter:** Carmelo Iaria  
**Session URL:** https://maven.com/p/2f7f42/launch-a-production-agentic-application

---

## Slide 1: Title Slide

# Launch a Production Agentic Application

### From "Works on My Laptop" to a Live, Value-Generating Pilot in 90 Days

**Carmelo Iaria**  
Synaptic AI Consulting | Agentic Architect | O'Reilly Instructor  
Pearson SME | ex-Cisco

**Maven Lightning Lesson · February 18, 2026**

---

## Slide 2: What You'll Learn Today

### Three Things You'll Leave With

✅ **A scoring framework** to select a first project that is low-risk but highly visible  
✅ **A 90-day rollout roadmap** — week-by-week phases from assessment to production  
✅ **The 3 pilot killers** — and exactly how to sidestep them  

> *"Tutorials are comfortable. Shipping is what builds careers."*

**30 minutes. Practical. No vibe coding.**

---

## Slide 3: The Deployment Gap

### The Brutal Truth About Agentic AI in 2026

| | |
|---|---|
| **72%** | of organizations have adopted AI in at least one function *(McKinsey, 2024)* |
| **< 20%** | of those pilots ever reach production |
| **Most common cause** | Not the tech — the execution layer |

**The gap isn't intelligence. It's orchestration, governance, and rollout.**

> Most aspiring architects stall here: "It works in my dev environment."  
> Today we close that gap.

---

## Slide 4: The 4 Patterns of SDLC Evolution

### How AI is Restructuring How Software Gets Built

```
TRADITIONAL SDLC          AI AUGMENTED SDLC       AGENTIC SDLC              AGENTIC VDLC
─────────────────         ─────────────────        ─────────────             ──────────────
Scoping                   Scoping                  Scoping                   Continuously monitor
System Design     ──►     System Design    ──►     System Design    ──►      technology & business
Implementation            Implementation           Implementation            KPIs
Validation                Validation               Validation
Review                    Review                   Review                    Spawns agent swarms
Release                   Release                  Release                   End-to-end autonomous
Monitoring                Monitoring               Monitoring                delivery
Feedback                  Feedback                 Feedback

PM / SA / SWEs            PM / SA / SWEs           AI Agent Personas         Agentic Architect
QAEs / DevOps             QAEs / DevOps            (PM, SA, SWE, QA)         + AI Manager Agents
                          + AI Tools               Agentic Architect
                                                   orchestrates
```

| Pattern | What Changes | Risk | Who's In Charge |
|---|---|---|---|
| **1. Vibe Coding** | Developers replaced by AI generation | 🔴 High — no governance, no structure | No one |
| **2. AI Augmented SDLC** | AI tools assist; humans still own every step | 🟡 Medium — speed gains, quality risk | Human team |
| **3. Agentic SDLC** | AI Agent Personas own each SDLC phase; human orchestrates | 🟢 Managed — governance by design | Agentic Architect |
| **4. Agentic VDLC** | Continuous value delivery, self-improving loops, agent swarms | 🔵 Next frontier | Agentic Architect + AI Managers |

> **The deployment gap lives here:** Pattern 1 (Vibe Coding) produces prototypes. Pattern 3 (Agentic SDLC) produces production systems.  
> **Today we teach you to operate at Pattern 3.**

---

## Slide 5: Poll — Where Is Your Team Right Now?

### Which pattern are you operating in?

*(Single choice)*

1. 🔧 Pattern 1 — Vibe Coding: AI-generated code, minimal structure  
2. 🤝 Pattern 2 — AI Augmented: AI tools + human-owned process  
3. 🏗️ Pattern 3 — Agentic SDLC: Agent personas, Agentic Architect orchestrating  
4. 🚀 Pattern 4 — Agentic VDLC: Continuous, autonomous value delivery  

---

## Slide 5: Step 1 — Use Case Selection

### The Most Expensive Mistake: Starting With the Wrong Project

**Common failure modes:**
- Automate everything at once → over-complexity, over-budget
- Pick the most exciting use case → too risky for a first pilot
- Pick the easiest use case → no visibility, no budget approval

**The right approach: Low-risk + High-visibility**

| | Wrong Pick | Right Pick |
|---|---|---|
| **Risk** | High (novel, unmapped) | Low (known domain, clear scope) |
| **Visibility** | Low (internal, invisible) | High (exec-visible, measurable) |
| **ROI** | Hard to quantify | Clear, defensible numbers |

---

## Slide 6: The Scoring Framework

### 4-Criteria Matrix — Score Each Candidate Use Case 1–5

| Criterion | What to Evaluate | Weight |
|---|---|---|
| **Business Visibility** | Will leadership notice if this succeeds? | 30% |
| **ROI Clarity** | Can you calculate cost savings or revenue lift? | 30% |
| **Technical Feasibility** | APIs available, data accessible, scope bounded? | 25% |
| **Risk Profile** | Low regulatory exposure, low customer-facing consequences | 15% |

**Target score: 3.5+ to proceed**

> ⚠️ Never pick a use case that scores high on excitement but low on ROI Clarity. That's how pilot purgatory starts.

---

## Slide 7: Example — Scoring a Customer Support Use Case

### Customer Support Multi-Agent System (Our Capstone)

**Scenario:** Mid-market bank, 24,000 queries/month, 70% automation target

| Criterion | Score | Rationale |
|---|---|---|
| Business Visibility | 5/5 | CFO and VP Customer Success care deeply about support costs |
| ROI Clarity | 5/5 | $60K/month in labor → $11.6K/month with agents = $48K saved monthly |
| Technical Feasibility | 4/5 | Existing ticketing system, API-ready knowledge base |
| Risk Profile | 3/5 | Regulated industry; needs careful escalation design |
| **Weighted Score** | **4.5/5** | ✅ High confidence to proceed |

**Agents needed:** Triage → Resolution → Escalation → Knowledge Manager

---

## Slide 8: Step 2 — The 90-Day Rollout Roadmap

### The One-Page Blueprint (4 Phases)

```
PHASE 1: Internal Validation    Weeks 1-3   → Proof of concept with your team
PHASE 2: Soft Launch            Weeks 4-6   → 25% production traffic with safety nets
PHASE 3: Ramping                Weeks 7-10  → Gradual scale to 70% target traffic
PHASE 4: Stabilization          Weeks 11-12 → Handoff to ops, steady state
```

**Why phased?**
- De-risks each step before adding load
- Builds stakeholder confidence early
- Allows context fixes without model retraining
- Gives your team time to adapt (change management)

> *"A single-launch strategy is a bet. A phased rollout is a plan."*

---

## Slide 9: Phase 1 — Internal Validation (Weeks 1–3)

### Proof of Concept With Your Team

**Objective:** Validate that agents work as designed before external exposure

**Activities:**
- Deploy agents alongside human support (parallel run)
- 100% human review of all agent outputs
- Collect feedback on quality, UX, integration issues

**Success Criteria:**
- ✓ Zero critical bugs (PII leakage, escalation failures, data corruption)
- ✓ Triage accuracy > 90% (94% is the prod target — don't panic if you're not there yet)
- ✓ CSAT on reviewed outputs > 3.8/5
- ✓ Team confidence survey: > 70%

**Key Roles:**
- You (Agentic Architect) → technical lead, context engineering
- Operations Manager → day-to-day execution
- A "champion" → respected team member who tests and advocates

> Phase 1 is about **finding what you missed**, not proving success.

---

## Slide 10: Phase 2 — Soft Launch (Weeks 4–6)

### Limited Production With Safety Nets

**Activities:**
- Route **25% of live traffic** to agents; 75% still handled by humans (control group)
- Monitor dashboards hourly; daily standup
- Deploy context/template fixes weekly (no model retraining needed)

**Success Criteria:**
- ✓ Auto-resolution rate: 55–65% (ramping toward 70% target)
- ✓ CSAT (auto-resolved): > 4.0/5
- ✓ Zero regulatory/compliance breaches
- ✓ System latency: p95 < 5s

**Rollback Plan:**
- CSAT drops below 3.8 → investigate before rolling back
- Compliance violation detected → **immediate pause + root cause analysis**
- Latency p95 > 10s → infrastructure investigation

**Improvement Cycle During Phase 2:**

```
Week 1: "Agents don't understand fraud signals" → update AGENT_Triage.md
Week 2: "Escalation missing customer history" → fix AGENT_Escalation output template
Week 3: "Wrong specialist routing" → refine riskClassification rules
```

> Context fixes deploy in **hours**. Not weeks. That's your competitive edge.

---

## Slide 11: Phase 3 — Ramping (Weeks 7–10)

### Building Operational Muscle

**Traffic ramp-up:**

| Week | Traffic to Agents |
|------|-------------------|
| Week 7 | 40% |
| Week 8 | 55% |
| Week 9 | 65% |
| Week 10 | 70% (full target) |

**Parallel Training Track (while ramping):**
- Week 7: "How agents work + how to escalate effectively" (30-min workshop)
- Week 8: "Reading agent logs for quality review" (hands-on lab)
- Week 9: "Giving feedback to improve agent behavior" (1:1 coaching)

**Success Criteria:**
- ✓ Auto-resolution rate tracking toward 70%
- ✓ CSAT (auto-resolved): > 4.2/5
- ✓ Team comfort level: survey > 85%
- ✓ Cost per resolution trending toward $0.05

> This phase shifts the mindset from "let's be careful" to **"this is how we work now."**

---

## Slide 12: Phase 4 — Stabilization (Weeks 11–12)

### From Launch to Steady State

**Objectives:**
- 100% production traffic through agent triage/escalation logic
- Transition from launch team to permanent ops team
- Establish runbooks, on-call, SLOs

**Operations Handoff Checklist:**
- [ ] Runbooks: what to do when an agent fails
- [ ] Escalation path: who to call when things break
- [ ] Alerting rules: what triggers wake-up calls
- [ ] SLOs defined: what level of reliability we expect

**Definition of "Mission Accomplished":**
- ✓ 70% of tickets auto-resolved
- ✓ CSAT on auto-resolved ≥ 4.2/5
- ✓ Cost per resolution ≤ $0.05
- ✓ Zero compliance breaches throughout rollout
- ✓ Projected savings: $520K/year (Year 2+)

> Success here means **you can step back**. The system runs without constant care.

---

## Slide 13: Observability — How You Prove Value

### The Three-Layer Evaluation Framework

*You can't improve what you don't measure. And you can't get budget for Round 2 without proof.*

**Layer 1: Model Performance** *(table stakes)*
- Triage accuracy, hallucination rate, compliance adherence
- Automated weekly test suite

**Layer 2: Agent Orchestration Quality** *(your differentiation)*
- Plan quality, tool selection accuracy, error recovery
- 500+ nightly simulation scenarios with synthetic personas

**Layer 3: System & Business Outcomes** *(what leadership cares about)*
- First Contact Resolution %, CSAT, Cost per Resolution, Compliance Violations
- This is what you show the CFO

> Most teams obsess over Layer 1. Smart Agentic Architects measure all three **simultaneously**.

---

## Slide 14: The Metrics Dashboard

### Your Single Pane of Glass (Datadog / Grafana / Looker)

| Metric | Target | Alert Threshold |
|---|---|---|
| Auto-Resolution Rate | 70% | < 65% |
| CSAT (auto-resolved) | 4.2/5 | < 4.0 |
| Cost per Resolution | $0.05 | > $0.07 |
| Escalation Accuracy | > 90% | < 85% |
| Triage Accuracy | > 94% | < 90% |
| p95 Latency | < 3s | > 5s |
| Compliance Violations | 0 | > 0 (immediate alert) |

**Example Monthly Report (January 2026):**
- 24K queries processed · 70% auto-resolved · $0.043 avg cost ✓
- **$187,000 in cost savings vs. human-only baseline**

> These numbers are what turn a pilot into a program.

---

## Slide 15: Step 3 — The 3 Pilot Killers

### What Actually Kills Agentic Pilots

**Killer #1: Wrong Use Case**
- Picked for excitement, not ROI visibility
- No exec sponsor, no budget renewal
- *Fix: Use the scoring framework before you write a line of code*

**Killer #2: No Phased Plan**
- Single-launch → one failure → entire program killed
- No safety nets, no rollback, no learning cycles
- *Fix: 4-phase blueprint with success criteria at each gate*

**Killer #3: Tool Proliferation**
- 7 frameworks, 3 orchestrators, 5 LLMs in the first sprint
- Complexity compounds, teams lose trust
- *Fix: One framework. Nail the fundamentals. Expand after Phase 4.*

> These three traps are not about intelligence — they're about execution discipline.

---

## Slide 16: The Rollout Paradox

### Smart Design ≠ Successful Adoption

**What happens in practice:**
- System works perfectly in pre-prod ✓
- Stakeholders trained and on board ✓
- Launch day arrives... and teams **bypass the agents**

**Why:**
- "It's easier to just handle it myself"
- "I don't trust the agent yet"
- "The agent doesn't understand my specific case"

**Root Causes:**
- Insufficient change management
- No "quick wins" to build early confidence
- Rollout too fast → insufficient learning time
- Rollout too slow → momentum lost

> *"Change management is 50% of your job as Agentic Architect."*

---

## Slide 17: Change Management — The 5 Moves

### Getting Real People to Use What You Built

**1. Involve Early (Phase 1)**  
Get 2–3 vocal team members on the design team from day 1. They become champions who say "I helped build this."

**2. Show the Jobs Agents Will Do First (Phase 1, Week 3)**  
"Agents handle 70% of routine inquiries. You handle 30% of complex cases. Your job shifts from routine to judgment-based."

**3. De-Risk With Soft Launch (Phase 2)**  
Review every auto-response. Escalations come back fast. You're not competing with the agent — you're a partner.

**4. Celebrate Wins Publicly (Every Phase)**  
"Agents caught 3 fraudulent transactions this week that slipped human review." "Team freed up 20 hours for complex cases."

**5. Offer Career Pathways (Ongoing)**  
- Agent quality reviewer → Agent behavior coach → AI operations specialist  
These are **promotions**, not demotions.

---

## Slide 18: What 90-Day Success Looks Like

### How You'll Know You're Winning

By Day 90:

✅ Agents are handling 25–40% of your use case in production  
✅ Your team believes in the system (70%+ in surveys)  
✅ You have concrete ROI data (cost savings, CSAT improvement)  
✅ Leadership is asking: "When can we do this for our other problems?"  
✅ You're recognized as the **expert on agentic architecture** in your org  

**The bigger picture:**
- Most organizations are in "pilot purgatory" — many experiments, few production deployments
- The gap isn't intelligence — it's **orchestration, governance, and rollout discipline**
- First-mover advantage lasts 6–18 months in your organization

> *"Your choices in the next 6–12 months will define your career for the next decade."*

---

## Slide 19: What's Next — Cohort 3

### Go Deeper in 6 Weeks

**Become an Agentic Architect — Cohort 3**  
February 23 – April 3, 2026

What you'll build:
- A **production-ready multi-agent application** using CrewAI and the AAMAD framework
- Governance artifacts (Cursor rules, agent personas, pattern libraries)
- A full observability stack
- A one-page rollout blueprint for your specific use case

What's included:
- 12 live sessions + office hours
- 1:1 coaching
- Lifetime access + community

**⚠️ Cohort 3 is the last one at the introductory price.**  
Enrollment closes **Friday, February 20**.

**Live attendees today get 25% off.**

👉 **maven.com/carmelo-iaria/agentic-architect**

---

## Slide 20: Q&A + Resources

### Thank You — Let's Build

**Resources shared today:**
- 📘 The Agentic Architect Playbook (free on my Maven page)
- 📋 90-Day Rollout Blueprint Template
- 📊 Use Case Scoring Framework (4-criteria matrix)

**Questions? Connect with me:**
- LinkedIn: linkedin.com/in/carmeloiaria
- Maven: maven.com/carmelo-iaria

**Cohort 3 enrollment:** maven.com/carmelo-iaria/agentic-architect  
Closes Friday, February 20 · Last cohort at introductory pricing

---

## 📋 SPEAKER NOTES

### Timing Guide (30 minutes total)

| Slide | Title | Target Time | Notes |
|---|---|---|---|
| 1 | Title | 0:00 | Welcome, intro |
| 2 | What You'll Learn | 0:30 | Set expectations |
| 3 | Deployment Gap | 1:30 | Hit the pain point hard — McKinsey stat |
| 4 | **4 SDLC Patterns** | 3:00 | Walk the 4 patterns; land on "Pattern 1 = pilot graveyard, Pattern 3 = today's goal" |
| 5 | Poll | 5:30 | Audience self-identifies; read results live, adjust emphasis |
| 6–7 | Use Case Selection + Framework | 7:00 | Walk through the scoring matrix |
| 8 | Capstone Example | 10:00 | Make it concrete with numbers |
| 9 | 90-Day Roadmap Overview | 12:00 | Show the full arc first, then dive in |
| 10–13 | Phases 1–4 | 14:00 | Move quickly — hit the key success criteria per phase |
| 14–15 | Observability | 20:00 | Three-layer framework + dashboard |
| 16–17 | 3 Pilot Killers + Rollout Paradox | 24:00 | This resonates hard — audience has lived this |
| 18 | Change Management 5 Moves | 27:00 | Keep it punchy |
| 19 | 90-Day Success | 28:30 | Aspirational close |
| 20 | Cohort 3 CTA | 29:30 | Confident, not salesy |
| 21 | Q&A | 30:00 | Leave ~5 min for questions |

### Key Talking Points

**On the Deployment Gap (Slide 3):**
> "72% of organizations have adopted AI in at least one function. But only a fraction of those make it to production. Why? It's not the model quality. It's not the framework. It's execution: picking the wrong project, skipping governance, no phased rollout. That's what today is about."

**On the 4 SDLC Patterns (Slide 4):**
> "Before I give you the how, let me show you the what. There are four patterns of how AI is reshaping software development — and most teams are accidentally stuck in Pattern 1. Vibe Coding. It feels fast, but it has no governance, no structure, no reproducibility. Pattern 1 is exactly why 72% of pilots never make it to production. Today I'm going to show you how to operate at Pattern 3 — Agentic SDLC — where you orchestrate AI Agent Personas through a structured lifecycle. And Pattern 4 is where we're heading next."

**On the Poll (Slide 5):**
> "Before we go further — quick pulse check. Which of these four patterns is your team operating in right now? No wrong answers. This tells me where to focus the next 20 minutes."

**On the Scoring Framework (Slide 7):**
> "I've seen brilliant engineers spend 6 months building something that was technically impressive but had zero business visibility. Nobody cared. No budget renewal. That project died. The scoring framework prevents that."

**On Observability (Slide 13):**
> "Here's what trips most teams: they build something that works, then they can't explain why it works. Stakeholder asks: 'How do you know it's doing the right thing?' And the answer is silence. The three-layer evaluation framework gives you the answer. Always."

**On the Rollout Paradox (Slide 16):**
> "I've seen this happen on real projects. System passes every test. Everyone's aligned. Go live. Day one, support agents route around the system. 'It's just faster to do it myself.' That's not a technology problem. That's change management. You need to plan for adoption the way you plan for architecture."

**On Cohort 3 CTA (Slide 19):**
> "Everything I've walked you through today — the scoring framework, the 90-day blueprint, the observability stack, the rollout plan — that's what we build together in 6 weeks. Not in a tutorial. In your actual project, with your actual use case. Cohort 3 starts February 23. Enrollment closes Friday. If you're in the live session today, you have a 25% discount code coming your way."

### Poll Response Guidance (Slide 4)

- **Mostly option 1-2 (experimenting/prototype):** Lean into the "path to production" framing — this session is their bridge  
- **Mostly option 3 (in production):** Acknowledge them, shift emphasis to observability and scaling (Slides 13-14)  
- **Mostly option 4 (evaluating):** Emphasize ROI clarity and the scoring framework (Slides 5-7)

### Live Attendee Discount Note

After Slide 19: "For everyone who's live right now — check the chat. I'll drop the discount code for Cohort 3. It's valid through Friday midnight. You'll have it in your inbox within an hour as well."

---

## 📝 Appendix: Supporting Data Points

| Claim | Source |
|---|---|
| 72% of orgs adopted AI in at least one function | McKinsey State of AI 2024 |
| Most pilots don't make it to production | McKinsey / internal estimation |
| Customer support example: $48K/month savings, 81% cost reduction | O'Reilly Agentic Architect Playbook (Capstone Use Case) |
| First-mover advantage in agentic patterns: 6–18 months | O'Reilly Agentic Architect Playbook, Module 4 |
| Change management is 50% of the job | O'Reilly Agentic Architect Playbook, Module 4 |
| Year 2+ ROI: 260% on $200K investment | O'Reilly Agentic Architect Playbook, Module 3 |
| Organizations adopting structured approaches outpacing ad-hoc 3:1 | O'Reilly Agentic Architect Playbook, Module 1 |
