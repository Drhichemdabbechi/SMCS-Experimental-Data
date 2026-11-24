#!/usr/bin/env python3
"""Validate table-level consistency of the manuscript-reported SMCS summaries.

Checks are structural/arithmetic; this program does not independently replay DBMS queries.
"""
from pathlib import Path
import csv, math
BASE=Path(__file__).resolve().parents[1]

def rows(path):
    with (BASE/path).open(newline='',encoding='utf-8') as file:
        return list(csv.DictReader(file))

def total(rs,key): return sum(int(row[key]) for row in rs)

def distinct(rs,keys):
    keys=[tuple(r[k] for k in keys) for r in rs]
    assert len(keys)==len(set(keys)),'duplicate grain keys'

c=rows('data/corpus/corpus_distribution_2013_2019.csv')
assert len(c)==10
assert total(c,'total_posts')==156220
assert total(c,'total_comments')==1668858
assert all(int(r['facebook_posts'])+int(r['tweets'])+int(r['youtube_posts'])==int(r['total_posts']) for r in c)
assert all(int(r['facebook_comments'])+int(r['youtube_comments'])==int(r['total_comments']) for r in c)

w1=rows('data/analytical/w1_facebook_posts_by_brand_2018.csv')
assert len(w1)==10 and total(w1,'distinct_posts')==3183
distinct(w1,['year','platform','brand'])
assert next(int(r['distinct_posts']) for r in w1 if r['brand']=='Sony')==824

w2=rows('data/analytical/w2_sony_likes_performed_monthly_2018.csv')
assert len(w2)==36 and total(w2,'likes_performed')==426
distinct(w2,['year','month_number','platform'])
assert {p:sum(int(r['likes_performed']) for r in w2 if r['platform']==p) for p in ('Facebook','Twitter','YouTube')}=={'Facebook':133,'Twitter':214,'YouTube':79}

w3=rows('data/analytical/w3_huawei_comment_engagement_2018.csv')
assert len(w3)==2
distinct(w3,['year','brand','platform'])
assert {r['platform']:(int(r['distinct_comments']),int(r['replies_received']),int(r['likes_received']),int(r['words_in_comments'])) for r in w3}=={'Facebook':(6400,102862,417631,60720),'YouTube':(2300,7295,220300,78170)}

w4=rows('data/analytical/w4_5g_keyword_occurrences_by_brand_2013_2019.csv')
assert len(w4)==10 and total(w4,'keyword_occurrences')==7858
distinct(w4,['period_start_year','period_end_year','keyword','brand'])

w5=rows('data/analytical/w5_drill_across_platform_annual_2018.csv')
assert len(w5)==3
distinct(w5,['year','platform'])
assert next(r for r in w5 if r['platform']=='Twitter')['distinct_comments']==''
assert next(r for r in w5 if r['platform']=='Facebook')['distinct_posts']=='3183'

b=rows('data/benchmark/w1_w4_latency_summary.csv')
assert len(b)==48
distinct(b,['workload','dbms','dataset_scale_percent'])
assert all(x['reported_repetitions']=='30' for x in b)
for w in ('W1','W2','W3','W4'):
    for db in ('MongoDB','Cassandra','SQL Server'):
        pairs={int(x['dataset_scale_percent']):x for x in b if x['workload']==w and x['dbms']==db}
        assert set(pairs)=={25,50,75,100}
        expected=round(float(pairs[100]['median_ms'])/float(pairs[25]['median_ms']),2)
        assert abs(expected-float(pairs[100]['scalability_factor_100_over_25']))<=0.02
        assert pairs[100]['iqr_ms'] and pairs[100]['p95_ms']
        assert all(pairs[s]['iqr_ms']=='' and pairs[s]['p95_ms']=='' and pairs[s]['scalability_factor_100_over_25']=='' for s in (25,50,75))

s=rows('data/benchmark/warehouse_readiness_storage.csv')
assert len(s)==3
for r in s:
    assert math.isclose(float(r['ingestion_seconds'])+float(r['structure_construction_seconds']),float(r['readiness_seconds']),abs_tol=1e-8)

print('PASS: corpus, W1–W5 analytical summaries, W1–W4 benchmark statistics and readiness values match the retained manuscript totals.')
print('Scope: arithmetic/consistency checks only; primary benchmark logs were not independently replayed.')
