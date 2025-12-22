# Quickstart — Running GenMediaEval v0.1

This guide describes how to run a lightweight benchmark comparison between two models (A vs B) using the v0.1 task catalog, prompt set, human rubric, and reporting templates in this repo.

---

## 1) Pick a run scope (recommended defaults)
- Compare: **Model A vs Model B**
- Clip length: **~4–8s** (keep constant)
- Samples: **30–40 prompts total**
- Raters: **2 raters per sample** (add a 3rd if disagreement)

---

## 2) Sample prompts (stratified)
Use `tasks/prompts_v0.1.md` and sample across task families:

Suggested minimum per family:
- **T1 Adherence:** 6 prompts
- **T2 Temporal:** 5 prompts
- **T3 Identity:** 4 prompts
- **T4 Editability:** 4 prompts
- **T5 Relations/Timing:** 5 prompts
- **T6 Physics/Motion:** 4 prompts
- **T7 Safety:** 2 prompts (ensure policy-safe handling)

If limited on time, run a smaller “smoke test”:
- 12 prompts total (2 per task family for T1–T6)

---

## 3) Generate outputs (standardize)
For each prompt:
- Generate output from **Model A** and **Model B**
- Keep generation settings consistent (seed, steps, guidance, duration where applicable)
- Store outputs in a consistent naming scheme (example):
  - `A_T2_p09.mp4`
  - `B_T2_p09.mp4`

---

## 4) Human scoring workflow (pairwise)
Use:
- Rubric: `rubric/human_rubric.md`
- Scoring sheet: `reporting/scoring_sheet.csv`

For each prompt pair:
- Rater watches A and B fully (at least twice)
- Selects winner (A/B/Tie)
- Records rubric ratings + failure tags + brief note if needed

Disagreement handling:
- If raters disagree, add a **third rater** or adjudicate with reason tags.

---

## 5) Summarize results (one-page report)
Use:
- `reporting/one_page_report_template.md`

Fill:
- Overall win-rate
- Win-rate by task family
- Top 5 failure tags
- 5 example prompts (with winner + tags)
- Next iteration plan (what to add/change for v0.2)

---

## 6) Output artifacts (what you should end with)
- Completed scoring sheet (`scoring_sheet.csv`)
- One-page report (`run_report_<date>.md` or PDF)
- A short list of “top failure prompts” to target in v0.2

---

## Notes
- For generative media, human preference is the primary signal; automated metrics are best used for triage and clustering.
- Always report **slice metrics** (by task family) to avoid hiding failures in averages.
