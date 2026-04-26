---
name: prd-author
description: End-to-end PRD (Product Requirements Document) authoring skill. Drives a three-phase interactive pipeline — discovery Q&A → structured session summary → final PRD — and produces two deliverable artifacts. Use whenever the user wants to plan, scope, draft, or write a PRD, MVP requirements, product spec, or "wymagania produktowe". Triggers on phrases like "PRD", "product requirements", "MVP scope", "spec produktu", "zaplanujmy produkt", "pomóż mi rozpisać MVP", "wygeneruj PRD".
---

# PRD Author

Three-phase pipeline that takes a high-level project idea and produces a complete Product Requirements Document. The user is an experienced product owner / developer — assume product literacy and skip basics.

## Pipeline overview

```
Phase 0:  Language selection      (one turn)
Phase 1:  Discovery Q&A loop      (N rounds, max 6 questions per round)
Phase 2:  Session summary         (XML structured artifact)
Phase 3:  Final PRD               (markdown artifact)
```

Each phase has a clear entry condition and a clear exit. Track which phase you are in based on conversation state, not just user keywords.

The pipeline is also pausable mid-Phase-1 via checkpoints — see the Checkpoints section below.

## Formatting convention

This skill uses three different formats for three different purposes. Be strict about which is which.

| Where | Format | Why |
|---|---|---|
| This SKILL.md (instructions for you) | Markdown | Human-readable instructions |
| Discovery output (questions, recommendations) | XML tags | Structured model output, parses cleanly |
| Checkpoint (Phase 1 pause artifact) | XML tags inside a markdown file | Structured save state, machine-readable on resume |
| Session summary (Phase 2 artifact) | XML tags inside a markdown file | Structured intermediate, downstream consumable |
| Final PRD (Phase 3 artifact) | Pure markdown | Deliverable for humans and tools |

Never mix. No XML in the PRD. No markdown headers competing with XML structure in the summary.

## Phase 0 — Language selection

On the very first turn of a session, ask exactly one question:

> W jakim języku prowadzimy sesję? / Which language for this session?
> 1. Polski
> 2. English

Wait for the answer. From that point on, conduct everything in the chosen language: questions, recommendations, summary content, PRD content. These instructions stay in English (they are for you).

Skip this question if the user has already started in one language with a clear substantive request (e.g. they pasted a project description in Polish and asked "zaplanujmy PRD"). In that case, use the language they used. Confirm only if genuinely ambiguous.

## Phase 1 — Discovery loop

Entry condition: language is set, user has provided some project description.

Each round:

1. Analyze silently in your reasoning block — the core user problem, candidate MVP features, likely user stories and flows, success criteria, constraints (timeline, resources, tech, regulatory). Do not narrate this analysis in the visible response.

2. Output exactly two XML blocks, in the user's language:

```
<questions>
1. ...
2. ...
</questions>

<recommendations>
1. ...
2. ...
</recommendations>
```

3. On the first round only, suggest a response format:

> Odpowiadaj w formacie "1. ..., 2. ..." — pytania, na które jeszcze nie znasz odpowiedzi, możesz pominąć pisząc "pomijam" lub "nie wiem".
>
> Reply in "1. ..., 2. ..." format — for questions you cannot answer yet, write "skip" or "don't know".

### Question rules

- Maximum 6 per round. Hard ceiling. If you have more candidates, drop the least blocking ones — they can return in later rounds.
- Order from most blocking to least blocking. No PRD progress is possible without the top one. The bottom one is nice-to-have.
- Re-read the full conversation context before each round. Never ask things already answered.
- One question per item. Split compound questions ("What's the timeline and budget?" → two items).
- Specific over generic. "Is the primary user the practitioner or the end client?" beats "Who are your users?".

### Recommendation rules

- Address ambiguities, gaps, or risks surfaced by your analysis.
- 3–7 per round is typical. No hard cap.
- Actionable, not vague. "Cap MVP scope at booking + practitioner profiles, defer wiki to v2" beats "Consider scope".

### Loop continuation

After the user responds, update your understanding and generate a fresh round covering newly opened areas, contradictions, or remaining gaps.

Continue until the user explicitly asks for a summary. Trigger phrases: "podsumuj", "podsumowanie", "wygeneruj podsumowanie", "kończymy", "summary", "let's wrap up", "generate the summary".

After 3–4 rounds, if gaps are minor and the user has not asked for a summary, you may proactively offer:

> Czy mamy wystarczająco materiału, żeby wygenerować podsumowanie sesji?
>
> Do we have enough material to generate the session summary?

Do not push.

## Checkpoints — pausing and resuming Phase 1

Phase 1 can span many rounds across multiple days. Because the skill is stateless across conversations, mid-session continuity relies on checkpoint files: a single self-contained markdown artifact the user takes with them and brings back next session.

Checkpoints only matter for Phase 1. Phase 2 and Phase 3 are short and atomic — no pausing inside them.

### Saving a checkpoint

Trigger phrases (in any language): "checkpoint", "zapisz checkpoint", "zapisz stan", "pause", "przerwij", "wracam jutro", "let's pause", "save state".

When triggered:

1. Stop the current round. Do not output a new question batch.
2. Generate the checkpoint artifact (structure below).
3. Save to `/mnt/user-data/outputs/prd-session-checkpoint-YYYY-MM-DD.md` in sandboxed environments, or `./prd-session-checkpoint-YYYY-MM-DD.md` in Claude Code locally. Use today's date.
4. Present the file. One-line confirmation telling the user: paste this file at the start of the next session to resume.
5. Stop. Do not ask follow-ups.

### Checkpoint structure

Markdown file with an XML block inside, content in the session language:

```
# PRD Session Checkpoint

<prd_checkpoint>
<meta>
language: pl | en
phase: discovery
round: [N — number of completed rounds so far]
date: YYYY-MM-DD
</meta>

<project_description>
[The original project description the user provided at session start. Verbatim if pasted, summarized faithfully if shared piece by piece.]
</project_description>

<qa_history>
[Numbered Q&A pairs from all completed rounds. Format:

Round 1:
Q1: [question text]
A1: [user's answer, including "skip" / "don't know" if applicable]
Q2: ...
A2: ...

Round 2:
...

Be faithful — do not paraphrase the user's answers.]
</qa_history>

<open_threads>
[Numbered list of topics still needing clarification. These become the seeds for the next round when the session resumes. Pulled from your latest analysis of remaining gaps.]
</open_threads>

<latest_recommendations>
[The recommendations from your most recent round. Useful context for resuming.]
</latest_recommendations>
</prd_checkpoint>

---

How to resume: paste this entire file into a new Claude conversation and say "kontynuujemy sesję PRD" / "resuming PRD session".
```

The footer line ("How to resume...") is part of the artifact, not an instruction to you — write it in the artifact in the session language so the user sees it when they reopen the file.

### Resuming from a checkpoint

Detection: at the start of any session, if the user's first message contains a `<prd_checkpoint>` block (or pastes a file with one), recognize this as a resume and skip Phase 0.

When resuming:

1. Parse the checkpoint. Extract language, completed rounds, Q&A history, open threads.
2. Acknowledge briefly in the language from `<meta>`: "Wznawiam sesję — ostatnio zakończyliśmy rundę N." / "Resuming — last completed round was N."
3. Re-enter Phase 1 at round N+1. Use `<open_threads>` and `<qa_history>` as input for generating the next batch of questions. Do not re-ask things already answered in `<qa_history>`.
4. Continue normally. Subsequent checkpoints, summary request, and PRD generation work the same as in a fresh session.

If the pasted checkpoint is malformed, partial, or ambiguous, ask the user one clarifying question rather than guessing — better to lose 30 seconds than to silently re-ask things they already answered.

### Checkpoint vs summary — do not confuse them

| | Checkpoint | Summary |
|---|---|---|
| When | Mid-Phase-1, user pauses | End of Phase 1, user wraps up |
| Contains | Raw Q&A history, open threads | Distilled decisions, matched recommendations, planning prose |
| Used for | Resuming the same session later | Input to PRD generation |
| Throwaway | Yes, after resume | No, kept as deliverable |

A checkpoint is a save file. A summary is a deliverable. Never substitute one for the other.

## Phase 2 — Session summary

Entry condition: user explicitly requested a summary.

Switch modes. Do not ask more questions. Produce the summary using the structure below, save it as artifact #1, then ask whether to proceed to the PRD.

### Summary structure

XML tags, content in the session language:

```
<conversation_summary>
<decisions>
[Numbered list of decisions the user actively made — concrete commitments, not "we discussed". Example: "1. MVP scope limited to booking + practitioner profiles, wiki deferred to v2."]
</decisions>

<matched_recommendations>
[Numbered list of YOUR recommendations from earlier rounds that the user implicitly or explicitly accepted. Skip rejected or now-irrelevant ones.]
</matched_recommendations>

<prd_planning_summary>
[Detailed prose covering:
 a. Main functional requirements
 b. Key user stories and usage flows
 c. Success criteria and how they will be measured
 d. Cross-cutting constraints (tech, regulatory, timeline)
Enough detail that someone reading only this can write the PRD. No platitudes. Include numbers, names, scope boundaries.]
</prd_planning_summary>

<unresolved_issues>
[Numbered list of open questions, deferred decisions, or areas needing more clarity. If everything is resolved, write "Brak" / "None".]
</unresolved_issues>
</conversation_summary>
```

### Summary rules

- Decisions are things the user actively chose. Not your suggestions. Not "we talked about". Concrete commitments.
- Matched recommendations are the ones that survived contact with the user's answers. Recommended split into two roles, user agreed → matched. User said "no, one role" → not matched, do not include.
- Planning summary must be self-contained. Someone with no access to the chat history must be able to write the PRD from it alone.
- Unresolved issues are honest. If something is fuzzy, name it. Do not paper over gaps.

### Saving the summary artifact

Save to `/mnt/user-data/outputs/prd-session-summary.md` in sandboxed environments (claude.ai web, Code Execution enabled). In Claude Code locally, save to `./prd-session-summary.md` in the current working directory; confirm path if cwd is ambiguous. In a plain chat with no file tools, output inline in a code block.

The artifact contains exactly the `<conversation_summary>...</conversation_summary>` block. Nothing else. No preamble.

After saving, present the file and ask in the session language:

> Podsumowanie zapisane. Czy wygenerować teraz pełny PRD na jego podstawie?
>
> Summary saved. Generate the full PRD from it now?

Wait for confirmation before entering Phase 3.

## Phase 3 — PRD generation

Entry condition: user confirmed they want the PRD after Phase 2.

Generate the PRD using the original project description plus the summary from Phase 2. Output the markdown directly to a file — do not print the full PRD inline in chat.

### PRD structure

Use exactly this top-level structure. Section numbering is fixed.

```
# Product Requirements Document (PRD) - {app-name}

## 1. Przegląd produktu / Product Overview

## 2. Problem użytkownika / User Problem

## 3. Wymagania funkcjonalne / Functional Requirements

## 4. Granice produktu / Product Boundaries

## 5. Historyjki użytkowników / User Stories

## 6. Metryki sukcesu / Success Metrics
```

Use only the language-appropriate header (one or the other, not both). The `{app-name}` is the product name from the project description.

### Section content rules

1. Product Overview — what the product is, who it is for, core value proposition. Specific, not marketing copy.

2. User Problem — the problem being solved, who has it, why existing solutions fall short. Tied to evidence from the discovery session.

3. Functional Requirements — what the product must do. Numbered or grouped. Specific enough to estimate.

4. Product Boundaries — what is explicitly out of scope for this version. Cite deferred features by name.

5. User Stories — see detailed rules below.

6. Success Metrics — measurable, with targets where possible. "Increase booking conversion to X%" beats "Improve bookings".

### User story rules

This is the most important section. Get it right.

- List every user story. Primary flows, alternative flows, edge cases. If a user can do it, there is a story for it.
- Each story has a unique ID: `US-001`, `US-002`, etc. Sequential, no gaps.
- Include at least one authentication / secure access story if the product has user identification or access control. Do not skip this.
- Each story must be testable. Acceptance criteria must be concrete enough that a tester can mark each as pass or fail.

Use this exact structure for each story:

```
### US-001
Tytuł / Title: [krótki tytuł / short title]

Opis / Description:
[1–3 sentences: as a [role], I want [action], so that [benefit].]

Kryteria akceptacji / Acceptance Criteria:
- [Concrete, testable criterion 1]
- [Concrete, testable criterion 2]
- ...
```

### Markdown formatting rules for the PRD

- Valid markdown. Headers (`#`, `##`, `###`) used as shown.
- No bold (`**text**`). The user prefers PRDs without bold emphasis.
- Italics, lists, code blocks, tables are allowed where useful.
- No XML tags anywhere in the PRD output. The PRD is pure markdown.
- Consistent numbering. Section 3.1, 3.2 are siblings. US-001, US-002 are sequential.

### Self-review before saving

Before writing the file, mentally check:

- Is each user story testable? If not, rewrite the acceptance criteria.
- Are acceptance criteria specific? "Form validates input" is not specific. "Form rejects email addresses without @" is.
- Do the user stories cover building a fully functional product? If a flow is missing, add it.
- If the product needs authentication, is there an auth story?

### Saving the PRD artifact

Save to `/mnt/user-data/outputs/PRD.md` in sandboxed environments. In Claude Code locally, save to `./PRD.md` in cwd; confirm if ambiguous. In plain chat with no file tools, output inline.

After saving, present both files (summary + PRD) and stop. One-line confirmation in the session language. No summary of the summary, no summary of the PRD.

## What this skill does NOT do

- Does not validate product viability or push back on the user's product decisions. The user is making the calls; you facilitate documentation.
- Does not search the web or pull external research. Operates on what the user provides.
- Does not generate code, wireframes, or technical architecture. PRD is product-level.

## Edge cases

- User pastes a long project description with no question: treat as Phase 1 entry. Confirm language if needed, run first round.
- User asks tangential question mid-session ("btw what DB?"): answer briefly, offer to return to the loop.
- User asks for the summary after only one round: comply. Note in `unresolved_issues` that the session was short and many areas remain unexplored.
- User asks for the PRD without going through summary first: generate the summary internally as input to the PRD, but still save both artifacts.
- User wants to switch language mid-session: switch immediately.
- Project description is too thin to ask 6 sensible questions: ask fewer. Max 6 is a ceiling, not a target.
- User rejects PRD generation after summary: stop cleanly. The summary alone is a valid output.
- User asks for a checkpoint during Phase 2 or Phase 3: those phases are atomic — finish the current artifact first, then offer a checkpoint if they still want one (though by that point the summary or PRD itself is the better save).
- User pastes a checkpoint mid-conversation rather than at the start: still recognize it, acknowledge the resume, and continue from the resumed state.
- User pastes a checkpoint from a different (much older) session and the project description in it differs from what they are saying now: ask which one is current before proceeding.