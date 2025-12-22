# Run Report — 2025-12-18 (Dry Run Skeleton)

**Status:** Dry run completed (sampling + reporting artifacts). Model outputs pending.

## Run metadata
- Date: 2025-12-18
- Models compared: TBD (Model A vs Model B)
- Clip length / format: TBD (recommend ~6s clips, fixed settings)
- Prompt set: `tasks/prompts_v0.1.md` (v0.1)
- Samples: 12 prompts (smoke test)
- Raters: 2 per sample (pairwise preference) — TBD once outputs exist

## Sampling (selected prompt IDs)
Stratified smoke test:
- T1 Adherence: Prompt IDs **1, 2**
- T2 Temporal: Prompt IDs **7, 9**
- T3 Identity: Prompt IDs **12, 14**
- T4 Editability: Prompt IDs **16, 17**
- T5 Relations/Timing: Prompt IDs **21, 22**
- T6 Physics/Motion: Prompt IDs **25, 26**
(T7 Safety handled separately; excluded from this smoke test.)

## Results overview
- Overall win-rate: **TBD**
- By-task breakdown: **TBD**
- Top failure modes: **TBD**

## Example analysis targets (what we will look for)
- T1: constraint omissions vs hallucinated additions
- T2: flicker/jitter during camera motion
- T3: identity drift across viewpoint/scene changes
- T4: collateral edits vs true localized edits
- T5: relationship/timing inversions
- T6: clipping / physics breaks on interactions

## Next actions (to make this a real run)
1) Generate outputs for the 12 prompts from both models (A and B)
2) Fill `reporting/scoring_sheet_example.csv` with rater decisions + tags
3) Populate the one-page report with real win-rates + failure-tag distribution
