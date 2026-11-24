# SMCS — Experimental Data and Results

**Associated article:** *A Multidimensional Constellation Model for Cross-Platform Social Media Analytics in NoSQL Data Warehouses* (submitted manuscript candidate for *Big Data Research*).

This data-only repository contains **the original analytical result values and experimental summary statistics reported in the final author-validated manuscript**. Its contents are derived from the manuscript's tables and retained original Figures 6–8. The authors state that their reported measurements and analyses were obtained and validated through real experiments.

## Contents

| Folder | File(s) | Scope |
| --- | --- | --- |
| `data/corpus/` | `corpus_distribution_2013_2019.csv` | Counts of publications and comments by brand and platform |
| `data/analytical/` | `w1_...csv` to `w5_...csv` | Reported analytical outputs for workloads W1–W5 |
| `data/benchmark/` | `w1_w4_latency_summary.csv` | Original reported benchmark medians, IQR, P95 and scalability factors |
| `data/benchmark/` | `warehouse_readiness_storage.csv` | Ingestion, construction, readiness and storage summary |
| `docs/` | `data_catalog.csv`, `DATA_DICTIONARY.md`, `PROVENANCE.md` | Documentation and traceability |
| `scripts/` | `validate_reported_results.py` | Structural, arithmetic, and cross-table checks |

## Analytical workloads

- **W1 — PostFact:** Facebook 2018 distinct publications for ten smartphone brands (3,183 in total).
- **W2 — UserFact:** Likes **performed** by Sony in 2018, by month and platform (Facebook 133, Twitter 214, YouTube 79).
- **W3 — CommentFact:** Huawei 2018 distinct comments and separate reply, like, and word-count measures on Facebook and YouTube.
- **W4 — KeywordFact:** Occurrences of the normalized term `5G` across brands during 2013–2019 (7,858 in total).
- **W5 — PostFact + CommentFact:** Grain-safe *drill-across* reported as annual platform totals derived by the authors from month-level aggregates. Separate aggregation is performed on each fact before alignment.

## Performance evaluation

The reported **timed benchmark covers W1–W4**, at dataset scales 25%, 50%, 75% and 100%, on MongoDB 7.0, Apache Cassandra 4.1 (single node), and SQL Server 16.0. The protocol described in the manuscript specifies 30 measured repetitions per configuration after five warm-up executions (1,440 measured executions total). The files here report the final published **summary statistics**, not the individual run records.

**W5 is an analytical validation workload, not a component of the timed W1–W4 benchmark.** No W5 comparative timing results are claimed in these files.

## Scope and availability

This repository makes available **aggregated results and summaries only**. It does **not** contain platform-native raw records, personally identifiable social media records, exact executable database schemas/queries, or original per-execution timing logs. The repository does not constitute a full independent reproduction of the benchmark. Source-data redistribution remains subject to the original platform and collection conditions.

The published values are retained exactly as in the manuscript; alternative working drafts and generated test datasets are excluded. A blank CSV cell denotes an unavailable result, not a measured zero (notably Twitter comment-side fields in W5). No output or statistical inference has been synthesized for missing raw timing records.

## Validation

Run:

```bash
python scripts/validate_reported_results.py
```

The script verifies published totals, uniqueness and expected group cardinalities, and the consistency of scalability ratios with the rounded medians. These arithmetic checks are distinct from independently rerunning the original database experiments.

## Citation and licensing

Please cite the associated article once publication details are finalized. A template is provided in `CITATION.cff`. **No reuse license has been selected by the authors yet**; confirm permissions and choose a license before publication.

## Publication note

The manuscript's Data and Code Availability statement should be updated **only after an actual public repository URL exists**, to describe precisely which aggregates are publicly available. See `docs/DATA_AVAILABILITY_TEXT.md`.
