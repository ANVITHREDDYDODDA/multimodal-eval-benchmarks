# Metrics Plan (v0.1)

**Principle:** Automated metrics are *assistive signals* for triage and analysis.  
**Primary decision signal for generative media:** human preference (pairwise) + rubric tags.

---

## 1) Scorecard outputs (per model)
For each run, produce:
- **Overall win-rate** (pairwise preference)
- Win-rate by **task family** (T1–T7)
- Mean rubric ratings by dimension:
  - adherence, temporal, identity, realism, edit precision (where applicable)
- **Failure-tag distribution** (top failure modes)

---

## 2) Assistive automated signals (by task intent)

### T1 Prompt adherence (constraints)
**Goal:** Detect missed constraints when machine-checkable.
- Constraint checklist proxy (entity/action/style keywords where applicable)
- Count checks (when prompts specify counts)

**Use:** flag likely misses for human review; do not replace human judgement.

### T2 Temporal consistency
**Goal:** Identify flicker/drift candidates.
- Frame sampling + stability heuristics (e.g., abrupt changes across sampled frames)

**Use:** triage and failure clustering.

### T3 Identity consistency
**Goal:** Detect identity drift candidates.
- Embedding similarity across sampled frames/segments (identity proxy)

**Use:** rank likely identity failures for targeted review.

### T4 Edit precision
**Goal:** Detect collateral changes.
- Similarity checks to estimate unintended changes outside edited region (proxy)

**Use:** measure preservation vs edit success qualitatively with humans.

### T5 Relationship & timing
**Goal:** Surface relation/timing errors.
- Lightweight structured checks when prompts are explicit (supportive only)

### T7 Safety boundary behavior
**Goal:** Track over-refusal and unsafe compliance rates.
- Refusal/compliance classification tags + counts

---

## 3) Aggregation rules (avoid misleading averages)
- Always report **slice metrics** by task family and difficulty tier.
- Do not over-weight “aesthetic quality” proxies; prioritize adherence + consistency.
- Highlight top failure modes with **example prompts** for fast iteration.

---

## 4) Reporting template (one-page)
Include:
1) Overall results
2) By-task breakdown
3) Top failure modes (with counts)
4) 10 example failures + notes
5) Proposed next benchmark updates
