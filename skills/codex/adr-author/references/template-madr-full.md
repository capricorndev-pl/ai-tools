# MADR (full) template

Use this as the default. Copy the block below and fill it in.

```markdown
# {short imperative title, matching filename verb phrase}

- Status: {Proposed | Accepted | Rejected | Deprecated | Superseded by [NNNN](./nnnn-title.md)}
- Date: {YYYY-MM-DD}
- Deciders: {optional — names or roles of people who made the call}
- Consulted: {optional}
- Informed: {optional}

## Context and Problem Statement

{Two to five sentences. What forced this decision now? What problem are we solving? What constraints matter — technical, business, regulatory, team? End with the question being answered, phrased neutrally.}

## Decision Drivers

- {driver 1 — e.g. "Must support 10k concurrent writes"}
- {driver 2 — e.g. "Team has zero Kafka operational experience"}
- {driver 3 — e.g. "Budget ceiling of $X/month for this component"}

## Considered Options

- Option A — {one-line label}
- Option B — {one-line label}
- Option C — {one-line label}

## Decision Outcome

Chosen option: **Option B**, because {one paragraph — the decisive reason, tied back to the drivers above. Not a pros list; the single dominant reason.}

### Consequences

- **Positive:** {concrete outcome, not "better performance"}
- **Positive:** {…}
- **Negative:** {concrete cost — operational, financial, complexity, lock-in}
- **Negative:** {…}
- **Neutral / unknown:** {things to watch — what would invalidate this decision}

## Pros and Cons of the Options

### Option A — {label}

- ✅ {pro — specific}
- ✅ {pro}
- ❌ {con — specific}
- ❌ {con}

### Option B — {label, the chosen one}

- ✅ {pro}
- ✅ {pro}
- ❌ {con — yes, the winner has cons too}

### Option C — {label}

- ✅ {pro}
- ❌ {con}

## Links

- {Related ADR — use relative path, e.g. [ADR-0003](./0003-choose-event-bus.md)}
- {Ticket or RFC link}
- {External reference, vendor doc, benchmark}
```
