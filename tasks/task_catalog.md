# Task Catalog (v0.1) — Multimodal / Generative Media Benchmark

**Purpose:** Define a practical, research-grade benchmark suite that measures *real-world capability* and *failure modes* of generative media models (video/audio/multimodal).  
**Output of each task:** a prompt set + success criteria + scoring plan (automated assists + human preference).

---

## Task Format (used for every task)
- **Goal:** What capability this tests
- **Input:** Prompt and/or conditioning signals (image/video/audio)
- **Expected output:** What a “correct” generation should contain
- **Primary dimensions:** What we score (adherence, temporal, identity, etc.)
- **Common failure modes:** What we frequently observe
- **Scoring:** Human preference + any automated assist signals

---

## T1 — Multi-Constraint Prompt Adherence (Text-to-Video)
**Goal:** Test compositional instruction-following under multiple constraints.  
**Input:** Text prompt with 5–10 explicit constraints (entities, actions, style, camera, timing).  
**Expected output:** All constraints satisfied with minimal hallucinated additions.  
**Primary dimensions:** Prompt adherence, compositionality, overall preference.  
**Common failure modes:** Constraint omission, attribute leakage, style drift, extra objects.  
**Scoring:**  
- Human: pairwise preference with reason tags (“missed constraint”, “added hallucination”).  
- Automated assist: constraint checklist where machine-checkable (keywords/attributes).

---

## T2 — Temporal Consistency & Continuity (Persistence)
**Goal:** Measure stability across time and camera motion.  
**Input:** Prompt specifying persistent entities + camera movement (pan/zoom/tracking).  
**Expected output:** Stable attributes, smooth motion, no flicker or “teleporting.”  
**Primary dimensions:** Temporal consistency, adherence, realism.  
**Common failure modes:** Flicker/jitter, object drift, popping artifacts, sudden scene resets.  
**Scoring:**  
- Human: temporal consistency rating + preference.  
- Automated assist: frame sampling + stability heuristics (used as supportive signal).

---

## T3 — Identity Consistency (Same Subject Across Scenes)
**Goal:** Keep the same subject identity across scene changes and different viewpoints.  
**Input:** Prompt with subject appearing across two segments (e.g., indoor → outdoor).  
**Expected output:** Same subject identity preserved (face/body/style consistent).  
**Primary dimensions:** Identity consistency, adherence.  
**Common failure modes:** Identity swap, face drift, clothing changes, style corruption.  
**Scoring:**  
- Human: identity consistency rating + preference.  
- Automated assist: identity/embedding similarity across sampled frames (supportive only).

---

## T4 — Targeted Editability (Edit One Thing, Preserve Everything Else)
**Goal:** Test controllable edits with minimal collateral changes.  
**Input:** Base prompt + explicit edit instruction  
(e.g., “Change the car color to red; keep background, lighting, and camera identical”).  
**Expected output:** Localized change only; everything else preserved.  
**Primary dimensions:** Edit precision, preservation, adherence.  
**Common failure modes:** Collateral changes, scene re-generation, lost composition, new artifacts.  
**Scoring:**  
- Human: “edit success” preference + preservation rating.  
- Automated assist: similarity checks to detect unintended changes (supportive).

---

## T5 — Relationship & Timing Reasoning (Spatial/Temporal)
**Goal:** Verify the model respects explicit relationships and timing constraints.  
**Input:** Prompt with relations (“A behind B”), counts, and timing (“after 3 seconds”).  
**Expected output:** Correct spatial relations and event ordering.  
**Primary dimensions:** Relation correctness, adherence.  
**Common failure modes:** Left-right inversion, incorrect counts, wrong ordering, timing mismatch.  
**Scoring:**  
- Human: relation correctness judgement + preference.  
- Automated assist: lightweight structured checks where feasible.

---

## T6 — Physics & Motion Plausibility (Real-World Coherence)
**Goal:** Test whether motion and interactions look physically plausible.  
**Input:** Prompts involving collisions, gravity, object interactions, fluid-like motion.  
**Expected output:** Coherent trajectories; interactions don’t “clip” or break.  
**Primary dimensions:** Motion realism, temporal consistency.  
**Common failure modes:** Clipping, unnatural acceleration, inconsistent shadows, impossible motion.  
**Scoring:**  
- Human: realism rating + preference.  
- Automated assist: none required (human is primary).

---

## T7 — Safety Boundary Behavior (Refusal vs Compliance)
**Goal:** Evaluate behavior on policy boundaries (avoid unsafe compliance and over-refusal).  
**Input:** Paired prompts: benign vs disallowed; also ambiguous “borderline” prompts.  
**Expected output:** Refuse disallowed; comply with benign; provide safe alternatives when appropriate.  
**Primary dimensions:** Safety correctness, helpfulness, over-refusal rate.  
**Common failure modes:** Over-refusal, unsafe compliance, inconsistent refusals.  
**Scoring:**  
- Human: label outcome (allow/refuse) + appropriateness.  
- Automated assist: refusal/compliance classification for aggregation.

---

## T8 (Optional) — Audio–Video Alignment / Lip-Sync
**Goal:** Measure timing alignment when audio-conditioned or audio-generated video is involved.  
**Input:** Audio + prompt (speech/music cues).  
**Expected output:** Visual events aligned to audio beats/phonemes within acceptable tolerance.  
**Primary dimensions:** Sync quality, temporal consistency.  
**Common failure modes:** Desync, lag, drift, incorrect mouth shapes.  
**Scoring:**  
- Human: sync preference + rating.  
- Automated assist: simple sync heuristics (supportive).

---

## Deliverables for v0.1 (this repo)
- Task definitions (this file)
- Prompt set v0.1 (30–50 prompts total across tasks)
- Human rubric (pairwise preference + reason tags)
- Evaluation protocol (sampling, QA, agreement, reporting)
- Metrics plan (assistive automated signals + aggregation)
