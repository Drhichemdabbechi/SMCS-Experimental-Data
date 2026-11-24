# Provenance and verification scope

- Primary source for the CSV files: `SMCS_Big_Data_Research_Final_Candidate.tex`, the author-provided submission candidate dated 2026-11-24, including the original Figures 6–8 and the dataset, W5, latency and storage tables.
- Author's status statement: the reported values and statistical summaries are from actual experiments and were checked and validated by the authors.
- This repository faithfully transcribes the **reported** aggregates from that manuscript, and its validation script verifies arithmetic and schema constraints. Independent verification against original database logs, transformation jobs and source tables has **not** been performed in creating the repository.
- `data/analytical/w1_...csv`, `w2_...csv` and `w4_...csv` use the original figure series selected by the authors, not a subsequently proposed replacement distribution.
- The W3 `distinct_comments` measure is distinct from `replies_received` (`CommentFact.CommentCount`).
- W5 annual totals correspond to the manuscript's Table `w5-summary`. The underlying 12 monthly group results per platform are not contained in this source package; they have not been fabricated or reconstructed from totals.
- Only W1–W4 have timed statistical summaries in the manuscript. The reported 30-run observations are **not** in this repository. Median, IQR and P95 cannot be reverse-engineered into the original observations.
- No raw social media data are redistributed.

**Before publishing**, the corresponding author should review each table against the original source exports and verify redistribution rights. Metadata and article version may then be finalized.
