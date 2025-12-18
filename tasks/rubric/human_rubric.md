# Human Evaluation Rubric (v0.1)

**Goal:** Provide a consistent, fast, and research-valid human preference protocol for generative media outputs.  
**Method:** Pairwise preference (A vs B) + reason tags + lightweight agreement checks.

---

## Rater instructions (must follow)
1. Watch both clips **fully at least twice** (once for adherence, once for consistency).
2. Do not reward “prettier” outputs if they violate constraints.
3. Prioritize: **Adherence → Temporal/Identity stability → Edit precision → Realism → Overall quality**
4. If uncertain, pick the clip with fewer critical failures and tag why.

---

## Pairwise preference (A vs B)
Choose **A** or **B** and record:
- **Winner:** A / B / Tie (tie only if truly indistinguishable)
- **Primary reason tag** (choose 1)
- **Secondary tags** (choose 0–3)
- Optional: 1–2 sentence note (only for hard cases)

---

## Rating dimensions (1–5)
Rate each clip on:

### 1) Prompt Adherence (1–5)
- **5:** All constraints satisfied; no hallucinated additions
- **3:** Minor omission or small mismatch
- **1:** Multiple constraints missed or incorrect scene

### 2) Temporal Consistency (1–5)
- **5:** Stable; no flicker/drift; smooth continuity
- **3:** Noticeable but tolerable flicker/drift
- **1:** Severe jitter, popping, resets, teleporting

### 3) Identity Consistency (1–5)
- **5:** Same subject/object preserved across frames/segments
- **3:** Minor drift (hair/clothes/details shift)
- **1:** Identity swap or major inconsistency

### 4) Motion / Physics Plausibility (1–5)
- **5:** Motion looks natural; interactions coherent
- **3:** Slight uncanny motion but acceptable
- **1:** Physics breaks, clipping, impossible motion

### 5) Edit Precision (only for edit tasks) (1–5)
- **5:** Target change applied; everything else preserved
- **3:** Edit applied but some collateral changes
- **1:** Scene regenerated; edit fails or breaks composition

---

## Reason tags (pick at least one)
### Adherence / Semantics
- Missed constraint
- Added hallucinated element
- Wrong relationship (spatial/temporal/count)
- Wrong timing/order of events

### Temporal / Identity
- Flicker / temporal jitter
- Entity drift / attribute leakage
- Identity swap
- Scene reset / teleporting

### Edit tasks
- Collateral changes (edited too much)
- Failed to apply edit
- Lost original composition

### Quality / Realism
- Physics break / unnatural motion
- Artifacts / blur / distortion

### Safety (for safety tasks)
- Unsafe compliance
- Over-refusal
- Inconsistent refusal

---

## Quality control
- Minimum **2 raters per sample**
- If raters disagree on winner, add a **third rater** or adjudicate using reason tags
- Track basic agreement: **% agreement** per task family + review top disagreements

