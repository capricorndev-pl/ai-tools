# Y-statement template

A one-paragraph decision record, adapted from Zdun et al.'s "Sustainable Architectural Decisions". Good for lightweight decisions inside README files, commit messages, or as a summary block at the top of a longer ADR.

## Form

> In the context of **{use case / feature / quality attribute}**,
> facing **{concern / problem}**,
> we decided for **{chosen option}**
> and against **{main alternative(s)}**
> to achieve **{benefit / quality goal}**,
> accepting **{downside / cost}**.

## Example

> In the context of **real-time notifications in the practitioner portal**,
> facing **the need for server-to-client push without long-lived WebSocket infrastructure**,
> we decided for **Server-Sent Events over a dedicated SSE endpoint**
> and against **WebSockets** and against **short-interval polling**,
> to achieve **lower operational overhead and native browser reconnect handling**,
> accepting **one-way communication only** and **the need for a workaround for some corporate proxies**.

## When to use

- Inline decisions in a larger doc (README, design doc, commit body).
- Summary block at the top of a full MADR/Nygard ADR.
- Quick informal decisions that don't warrant their own file.

Don't use a Y-statement as a standalone file for a significant decision — the context and consequences sections of a full template exist because one paragraph isn't enough to record trade-offs properly.
