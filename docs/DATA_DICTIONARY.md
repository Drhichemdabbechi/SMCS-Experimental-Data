# Data dictionary

All files use comma-separated values (UTF-8) with a single header row. Numerical values use `.` as the decimal mark and **no thousands separator**. `year`, `month_number`, `dataset_scale_percent`, and count columns are integers. Timing and storage metrics are floating-point values.

## Corpus

`corpus_distribution_2013_2019.csv`: `brand` identifies one of ten smartphone brands; `facebook_posts`, `facebook_comments`, `tweets`, `youtube_posts`, `youtube_comments`, `total_posts`, `total_comments` are source-record counts. The total posts count comprises Facebook posts, tweets and YouTube posts; the total comments count comprises Facebook and YouTube comments.

## Analytical results

- `w1_facebook_posts_by_brand_2018.csv`: `distinct_posts` counts eligible Facebook publication objects in 2018 by `brand`.
- `w2_sony_likes_performed_monthly_2018.csv`: `likes_performed` counts user-attributed liking actions by Sony in 2018. It does **not** denote likes received by Sony posts.
- `w3_huawei_comment_engagement_2018.csv`: `distinct_comments` is the count of comment records; `replies_received` is the sum of `CommentFact.CommentCount`; `likes_received` is the sum of `CommentFact.LikeCount`; `words_in_comments` is `CommentFact.WordCount` aggregated over the workload population.
- `w4_5g_keyword_occurrences_by_brand_2013_2019.csv`: `keyword_occurrences` is term occurrence count; it is not the number of documents containing the term.
- `w5_drill_across_platform_annual_2018.csv`: post-side (`distinct_posts`, `post_likes_received`) and comment-side (`distinct_comments`, `comment_likes_received`, `comment_word_count`) annual aggregates, separately computed before alignment by platform/year. Empty Twitter comment-side fields mean **unavailable**, not zero. The reported totals are from 12 month-level groups per platform; this dataset is the annual summary rather than those monthly groups.

## Performance

- `w1_w4_latency_summary.csv`: one row per workload, DBMS and percentage scale; `median_ms` is reported median end-to-end latency. `iqr_ms` and `p95_ms` are reported at 100% scale **only**, so their cells are blank at lower scales. `scalability_factor_100_over_25` is reported at 100% scale only; ratios of rounded medians may differ slightly due to presentation rounding. `reported_repetitions` is the manuscript's number of measured query executions per configuration, **not** the number of rows in this CSV.
- `warehouse_readiness_storage.csv`: ingestion, physical construction, and total readiness times in seconds; full-scale warehouse footprint in GiB.
