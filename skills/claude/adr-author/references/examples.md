# ADR writing examples

Side-by-side examples of ADR prose. Load this when drafting if you're unsure how sharp a section should be.

## Title

❌ `# Database decision`
❌ `# ADR 0007: We think we should use PostgreSQL`
❌ `# postgresql.md`
✅ `# Use PostgreSQL for the primary OLTP store`

The title is a verb phrase. Past/present imperative, like a commit subject. Matches the filename.

## Context

❌ Too vague:
> We need a database. There are many options. We looked at several and picked one.

❌ Too much history:
> In 2019 we started with SQLite. Then in 2021 we migrated to MySQL 5.7 because Alice joined. In 2023 we considered Cassandra but didn't pursue it. Now it's 2026 and …

✅ Forces and question:
> The booking service currently writes to SQLite on a single node. We need to add a second app instance for HA and support ~200 concurrent writes/sec at peak (2× current load, 10× projected 12-month). The team is two people, both comfortable with SQL, with no prior operational experience running distributed datastores. Which database should back the booking service?

## Options

❌ Straw-man options:
> - PostgreSQL (great, everyone loves it)
> - MongoDB (no schema, bad)
> - Writing our own (lol)

✅ Each option treated seriously:
> - **PostgreSQL on managed RDS** — mature SQL, strong consistency, team familiarity; operational cost of a managed service.
> - **SQLite with Litestream replication** — near-zero ops, already in use; single-writer bottleneck becomes the limit.
> - **CockroachDB Serverless** — horizontal scale, PG wire-compatible; team has no operational experience, cost model less predictable at our projected volume.

## Decision

❌ Hedged:
> We're leaning toward PostgreSQL but may revisit.

❌ Marketing:
> PostgreSQL is the industry-leading best-in-class choice for modern applications.

✅ Declarative, with the decisive reason:
> Chosen option: **PostgreSQL on managed RDS**, because it clears the concurrent-write target with margin, preserves the team's existing SQL operational skillset, and keeps a straight upgrade path if we outgrow a single primary (read replicas, then Aurora or Citus). The operational cost is acceptable relative to the team's capacity.

## Consequences

❌ Sugar only:
> Great performance, great scalability, happy team.

❌ Vague negatives:
> Some added complexity.

✅ Specific, both sides:
> **Positive**
> - Single well-understood datastore; no new operational surface.
> - Managed backups, PITR, and patching — ~0.5 FTE-day/month reclaimed vs. self-hosting.
> - Standard tooling (pg_dump, psql, Grafana PG dashboards) already in use.
>
> **Negative**
> - Monthly cost floor rises by ~$180 vs. current SQLite setup.
> - Adds VPC peering to the managed-RDS tenancy; first time this app needs private networking.
> - Migration work: ~3 days to port schema, dual-write window, cut over.
>
> **Neutral / unknown**
> - Write throughput ceiling before needing read replicas is untested at our workload; revisit if sustained load crosses ~60% of baseline capacity.

## Linking a superseded ADR

In the new ADR:

```markdown
- Status: Accepted
…
## Links

- Supersedes [ADR-0003: Use SQLite with Litestream](./0003-use-sqlite-with-litestream.md)
```

In the old ADR, update the status line:

```markdown
- Status: Superseded by [ADR-0012](./0012-use-postgresql-for-primary-oltp-store.md)
```

Don't delete the old file. The history of the reasoning is part of the record.
