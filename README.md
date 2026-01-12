# multimodal-eval-benchmarks

Work-in-progress benchmark & evaluation suite for multimodal / generative media models — task sets, scoring metrics, and human preference rubrics.  
**Started:** Dec 18, 2025  
**Last updated:** Dec 22, 2025

## Progress log
### 2025-12-18 — v0.1 initialized
- Defined benchmark scope + failure taxonomy
- Drafted v0.1 task set and task catalog
- Wrote human rubric + evaluation protocol + metrics plan
- Added prompt set v0.1 (36 prompts)
- Added reporting artifacts (one-page template, scoring sheet templates)
- Added quickstart for running an end-to-end eval workflow

### 2025-12-22 — pipeline validated + first “gold run” started (12 prompts)
**Environment + repo setup**
- Downloaded repo locally and fixed path issues by running commands from repo root (instead of `C:\Users\Anvit`)
- Confirmed scripts run end-to-end from the correct working directory

**Run artifact generation (prepare_run.py)**
- Generated a 12-sample run manifest + scoring sheet successfully:
  - `runs/2025-12-22/prompt_manifest.csv`
  - `runs/2025-12-22/scoring_sheet.csv`
- Verified the manifest contains prompt_text entries for:
  - T1 prompts 1–6
  - T2 prompts 7–11
  - T3 prompt 12
- Verified scoring sheet includes sample IDs `s001` → `s012`

**Aggregation script validation (aggregate_scores.py)**
- Ran aggregation on the example scoring sheet:
  - `python scripts/aggregate_scores.py --scores reporting/scoring_sheet_example.csv`
- Confirmed script prints:
  - overall winner counts
  - per-task winner counts
  - tag distribution
  - dry-run note when values are `TBD`

**First real model comparison (Runway vs Luma)**
- Selected evaluation pair:
  - Model A: `runway_gen3`
  - Model B: `luma_dream_machine`
- Completed sample `s001` with **image + prompt conditioning**
  - Generated reference image (16:9, photoreal constraints)
  - Generated video outputs from both tools
  - Noted free-tier watermark constraint
  - Observed: Runway continued the input image; Luma followed the prompt but did not preserve/continue the input image (prompt-only behavior)

**Manual scoring completed**
- Filled `runs/2025-12-22/scoring_sheet.csv` for `s001` including:
  - winner (model_a)
  - rubric scores (adherence/temporal/identity/realism/edit_precision)
  - primary_tag + secondary_tags
  - notes including: watermark_free_tier and image_conditioning_failed_luma
  - rater_id: `anvith_1`

**Status**
- ✅ Run scaffolding complete (manifest + scoring sheet generated)
- ✅ Aggregation script verified on example sheet
- ✅ Real evaluation started: `s001` fully executed and scored
- 🔜 Next: complete `s002–s012` outputs + scoring, then aggregate real results:
  - `python scripts/aggregate_scores.py --scores runs/2025-12-22/scoring_sheet.csv`


## Repo map (start here)
- **Tasks:** `tasks/task_catalog.md`
- **Prompts:** `tasks/prompts_v0.1.md`
- **Human rubric:** `rubric/human_rubric.md`
- **Evaluation protocol:** `eval/evaluation_protocol.md`
- **Quickstart (how to run):** `eval/quickstart.md`
- **Metrics plan:** `metrics/metrics_plan.md`
- **Reporting template:** `reporting/one_page_report_template.md`
- **Scoring sheet (blank):** `reporting/scoring_sheet.csv`
- **Dry run report:** `reporting/run_report_2025-12-18.md`
- **Dry run scoring sheet (example):** `reporting/scoring_sheet_example.csv`

## What a run produces
- Overall + per-task **win-rates** (pairwise preference)
- Rubric dimension scores: **adherence, temporal consistency, identity consistency, realism, edit precision**
- Failure-tag distribution + top examples (for fast iteration)
- **Artifacts per run:** a completed scoring sheet + a one-page report (stored under `reporting/`)

## Changelog
- **2025-12-18:** v0.1 initialized (tasks, rubric, protocol, metrics plan)
- **2025-12-18:** added prompt set v0.1 (36 prompts)
- **2025-12-18:** added reporting artifacts (one-page template, scoring sheets, dry-run report skeleton)
- **2025-12-18:** added quickstart guide for running an end-to-end eval
- **2025-12-22:** README polish + added dry-run artifacts and reporting/quickstart refinements
