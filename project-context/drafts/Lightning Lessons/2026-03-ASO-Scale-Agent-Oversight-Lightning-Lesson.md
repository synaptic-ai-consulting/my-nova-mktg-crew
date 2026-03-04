# Lightning Lesson Draft: Scale AI Agent Oversight Beyond 8

**Source:** ASO paper (Adaptive Stigmergic Oversight framework)  
**Target ICP:** Software developers, tech leads, engineering managers, AI/ML engineers — Become an Agentic Architect course audience  
**Status:** Draft — ready for review  
**Created:** 2026-03-04

---

## Maven Listing Copy

### Title Options (choose one — under 40 characters)

| Option | Characters | Notes |
|--------|------------|-------|
| **Scale AI Agent Oversight Beyond 8** | 32 | Direct, actionable, speaks to fan-out ceiling |
| **Orchestrate 50+ AI Agents Without Burning Out** | 43 | Too long — trim to "Orchestrate 50 AI Agents Without Burning Out" (40) |
| **Design Intent-Based AI Agent Oversight** | 38 | Technical, framework-focused |
| **Scale Human Oversight of AI Agent Swarms** | 38 | Clear outcome |

**Recommended:** **Scale AI Agent Oversight Beyond 8**

---

### Short Description (for Maven listing)

**Hook (1–2 sentences):**  
Human-in-the-loop caps you at ~5–8 agents. Full autonomy amplifies errors 17×. There's a fourth paradigm—and it's backed by 45+ years of human factors research.

**Body:**  
Learn the three-layer framework from cutting-edge research: intent-based delegation, stigmergic swarm coordination, and exception-based review. In 30 minutes you'll see how to scale oversight of 50+ AI agents without becoming the bottleneck—and without losing control. Includes a Cursor-ready implementation pattern you can apply this week.

**Who it's for:**  
Software developers, tech leads, and AI engineers who already orchestrate multiple agents (in Cursor, CrewAI, or similar) and hit the ceiling where manual review doesn't scale.

---

### Learning Outcomes (bullet list for Maven)

- Understand why HITL, HOTL, and full autonomy all fail at scale—and what replaces them
- Apply the three-layer ASO architecture: intent, stigmergic coordination, exception review
- Design constraint envelopes and exception triggers for your own agent workflows
- Map the Cursor ecosystem (worktrees, Cloud Agents, rules) to an ASO-style implementation

---

## 30-Minute Structure (Maven Format)

| Segment | Duration | Content |
|---------|----------|---------|
| Pre-lesson | 10 min | Attendees in Zoom, tech check |
| Intro + icebreaker | 2 min | "How many AI agents do you routinely work with? Drop in chat." |
| Personal story | 3 min | Challenge: scaling from 2–3 agents to 8+ without losing control |
| Tactical how-to | 14 min | ASO three layers + Cursor implementation pattern |
| Course pitch | 1 min | Become an Agentic Architect — 6 weeks, production capstone |
| Q&A | 10 min | Open |

---

## Script & Content Notes

### Intro + Icebreaker (2 min)

- Welcome, quick intro
- **Icebreaker:** "How many AI agents do you routinely work with? Type a number in chat—2, 5, 10, more?"
- **Transition:** "If you said more than 5, you've probably felt the squeeze. Research shows human-in-the-loop caps most of us at 5–8 agents. Beyond that, we become the bottleneck."

---

### Personal Story (3 min)

**Challenge:**  
"I was orchestrating multiple agents in Cursor for client work—feature agents, test agents, review agents. At 3–4 agents it was manageable. At 6–7, I was drowning in PRs and context switches. I couldn't scale up without either micromanaging everything or letting agents run loose and risking cascading errors."

**Discovery:**  
"I dug into the research—supervisory control theory, swarm intelligence, trust calibration. The insight: we don't need to choose between control and scale. We need a different architecture. One that keeps the human at the strategic layer—intent and exceptions—while agents coordinate through shared artifacts, not through us."

**Outcome:**  
"That's the framework I'll walk you through: Adaptive Stigmergic Oversight, or ASO. It's grounded in 45+ years of human factors research and recent multi-agent scaling studies from Google and others."

---

### Tactical How-To (14 min)

**Slide 1: The Three Paradigms That Fail**

| Paradigm | Strength | Fatal flaw at scale |
|----------|----------|---------------------|
| Human-in-the-loop (HITL) | Maximum control | Fan-out ceiling ~5–8 agents |
| Human-on-the-loop (HOTL) | Better throughput | Situation awareness degrades; out-of-the-loop problem |
| Full autonomy | Maximum throughput | Error amplification 17×; hallucination cascades |

**Slide 2: ASO — Three Layers**

1. **Intent-Based Delegation (Human → Swarm)**  
   - Specify intent, not tasks. Intent = high-level objective + constraint envelope (quality, risk, scope, approach).  
   - Example: "Add OAuth2 + JWT auth, 90%+ test coverage, no DB schema changes."

2. **Stigmergic Swarm (Agent ↔ Agent)**  
   - Agents coordinate through shared artifacts (codebase, docs, test results)—not through you.  
   - Same pattern as open-source: developers react to code changes, not to each other.  
   - Coordination cost grows O(n) instead of O(n²) with message passing.

3. **Exception-Based Review (Swarm → Human)**  
   - Validators assess outputs against the constraint envelope.  
   - High confidence → auto-approve. Low confidence → escalate to you with context.  
   - Target: &lt;10% exception rate so you review ~4 outputs per cycle from 50 agents.

**Slide 3: Cursor Implementation Pattern**

- **Intent:** `.cursor/rules` + custom commands or `# .aso/intent.yaml`-style config
- **Stigmergic medium:** Git repo + CI/CD + test results + linter
- **Exception triggers:** Failing CI, security findings, coverage below threshold, architectural drift
- **Trust thresholds:** `auto_approve: 0.85`, `escalate: 0.60`, `block: 0.40`

**Slide 4: One Concrete Example**

- Intent: "Implement user notification system — event-driven, use existing message bus, &gt;85% coverage, &lt;200ms delivery."
- Constraint envelope: No changes to auth or billing; follow project coding standards.
- Agents: Feature implementers, test writers, validators.
- You only see: Exceptions (failing CI, security alerts, coverage drops).

---

### Course Pitch (1 min)

"This is a taste of the orchestration discipline we build in *Become an Agentic Architect*—a 6-week, project-based course where you design, build, and deploy a production-ready multi-agent AI application with CrewAI and the AAMAD framework. Real capstone, live coaching, no empty theory. Link in the chat—and there's a promo for Lightning Lesson attendees."

---

## ICP Hooks (for promotion copy)

Use these angles when promoting the Lightning Lesson to your audience:

- **Developers:** "You're already using Cursor with multiple agents. Research says HITL caps you at ~8. Here's the architecture that scales beyond that."
- **Tech leads:** "38% of enterprises report hallucination cascades in multi-agent setups. ASO gives you exception-based oversight without micromanaging."
- **AI/ML engineers:** "Google's 2026 scaling study: centralized coordination improved parallelizable tasks by 80.9%, but independent agents amplified errors 17×. Learn the middle path."

---

## Research & Sources (for credibility)

| Claim | Source (from ASO paper) |
|-------|-------------------------|
| HITL fan-out ceiling ~5–8 agents | Olsen & Goodrich (2004); Perkins & Johnson (2024) |
| Error amplification 17× (independent agents) | Google Research 2026 agent scaling study |
| 38% enterprises report hallucination cascades | Industry surveys cited in ASO paper |
| Stigmergy in software dev (shared codebase) | Crowston et al. (2006) |
| Cursor 2.0: 8 parallel agents, Cloud Agents 10–20 | Cursor changelog, NxCode 2026 |
| 30% of Cursor's merged PRs from agents | Cursor blog, scaling agents |

---

## Next Steps

1. **Review:** Does this structure and copy match your voice and Maven's guidelines?
2. **Title:** Confirm final title (under 40 chars).
3. **Assets:** Create Lightning Lesson image using Maven's template.
4. **Promo:** Draft LinkedIn/email promo using ICP hooks above.
5. **STATUS.md:** Add notification when approved.

---

*Draft prepared by Casey (Course Portfolio & Syllabus Strategist) from ASO paper synthesis. Source: project-context/research/aso_paper.pdf*
