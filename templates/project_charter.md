# {project-name} — Project Charter

*{one-line headline: what the product is, in plain language}*

**Status:** {Working draft | Approved | Superseded}
**Last updated:** {YYYY-MM-DD}

---

## 1. Purpose

{2–4 sentences answering: what is this product, who is it for, and what category does it sit in? If positioning against well-known reference products is useful, include it here — but call out how this product differs in approach (e.g. opinionated vs. general-purpose, managed vs. self-serve, vertical vs. horizontal).}

## 2. Background and problem statement

{Describe the situation the target market is in today and why existing options fail them. A useful structure:

- Why the workload is significant enough to justify dedicated tooling.
- Why the obvious off-the-shelf solutions (SaaS, generic platforms) don't fit — scale, regulatory posture, data residency, integration, etc.
- Why the obvious solution doesn't fit — cost, headcount, expertise.
- What people actually do today and why that's getting worse.

End with the binding constraint — the single thing that, if solved, unlocks adoption. This is usually not "more features" but something structural: missing expertise, missing trust, missing integration, etc. Naming it sharpens everything downstream.}

## 3. Product hypothesis

{One paragraph stating the central bet. Format: "Target customers will adopt {product approach} — rather than {plausible alternative} — because {causal reason tied to the binding constraint above}."

Optionally a second paragraph on retention or expansion dynamics: why does value compound over time, and what makes switching costly?}

## 4. Target markets

### Buyers

- {Primary buyer segment}: {role in the deal — primary, alternative, later phase}
- {Secondary buyer segment}: {role}
- {Future segments}: {role}

### Users

- {User role 1}: {what they do with the product}
- {User role 2}: {what they do with the product}
- {User role 3}: {what they do with the product}

{Geographic scope and distribution channel for initial rollout — e.g. "Initial rollout limited to {region}, distributed through {channel}."}

## 5. Solution overview

### 5.1 Core user scenario

{A short narrative — 3–6 sentences — describing what a typical user does on a typical day with the product. Avoid feature lists; describe the experience. Include who triggers things, who consumes outputs, and where humans intervene.}

### 5.2 Key differentiators vs. {nearest competitor category}

1. **{Differentiator 1, stated as a property of the product}.** {1–2 sentences explaining why this matters and how it contrasts with the competitor category.}
2. **{Differentiator 2}.** {Explanation.}
3. **{Differentiator 3}.** {Explanation.}
4. **{Differentiator 4}.** {Explanation.}

{Aim for 3–5 differentiators. Each one should be defensible — something a competitor can't trivially copy without changing their business model.}

### 5.3 High-level architecture

{2–4 sentences sketching the shape of the system at a level a non-engineer stakeholder can follow. Mention the dominant pattern (e.g. DAG, event-driven, request/response, batch), the major modules or surfaces, and the deployment model. Detailed architecture lives elsewhere — link it.}

Detailed architecture, stack, and PRD live in separate documents.

## 6. Scope

### 6.1 In scope

- {Capability 1}
- {Capability 2}
- {Capability 3}
- {Delivery / service component, if part of the offering}
- {Operational component — installation, handover, ongoing maintenance, etc.}

### 6.2 Out of scope (initial release)

- {Tempting feature deliberately deferred — name it explicitly so the team can resist scope creep}
- {Adjacent market or segment not pursued initially}
- {Deployment or distribution model not supported initially}
- {Generalization or expansion explicitly held back}

## 7. Success criteria

- **{Dimension 1, e.g. efficiency}:** {what will be measured, in what window}
- **{Dimension 2, e.g. quality}:** {measurable outcome}
- **{Dimension 3, e.g. retention or expansion}:** {compounding or stickiness signal}
- **{Dimension 4, e.g. commercial}:** {go-to-market validation signal}

{Specific quantitative targets {to be set per engagement during scoping | defined in the PRD | tracked in the metrics dashboard}.}

## 8. Key assumptions

- {Assumption about buyer willingness or budget}
- {Assumption about how a key product property will be perceived — feature vs. tax, asset vs. liability}
- {Assumption about reusability or amortization across customers}
- {Assumption about distribution channel viability}

{Each assumption should be falsifiable — something you could later say "we were wrong about this" about. If you can't imagine being wrong, it's not really an assumption, it's a description.}

## 9. Constraints

- **{Constraint type, e.g. regulatory}:** {specific regimes or rules that shape the product}
- **{Constraint type, e.g. data residency}:** {what must be true about where data lives}
- **{Constraint type, e.g. market / localization}:** {language, cultural, or jurisdictional requirements}
- **{Constraint type, e.g. delivery model}:** {what the chosen GTM forces on the org — e.g. provider capacity bottleneck}
- **{Constraint type, e.g. security}:** {non-negotiable security or compliance posture}

## 10. Key risks

| Risk | Notes |
|---|---|
| {Risk 1 — usually about the delivery model or unit economics} | {Why it's a risk. Mitigation: {concrete approach}.} |
| {Risk 2 — usually about sales cycle, GTM, or adoption pace} | {Notes and mitigation.} |
| {Risk 3 — usually about operational or support burden at scale} | {Notes and mitigation.} |
| {Risk 4 — usually about customer expectations diverging from the product thesis} | {Notes and mitigation.} |
| {Risk 5 — usually about external change: regulation, market, dependencies} | {Notes and mitigation.} |

## 11. Related documents

- {Full PRD}
- {Architecture specification}
- {Stack specification}
- {Other supporting docs as relevant}

## 12. Open questions

- {Pricing and packaging question}
- {Minimum viable scope question}
- {Support / SLA question}
- {Standardization vs. flexibility question}
- {Any other unresolved decisions blocking the next phase}