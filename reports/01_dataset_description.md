# 📄 Report 01 — Comprehensive Dataset Description & Inventory

## 📌 Executive Summary
This report provides a formal dataset description for the ML research pipeline. The project contains two primary datasets located in the project root:
1. `binary_df.csv`: Primary binarized/indicator feature matrix with ground truth target labels.
2. `vus_only_variants.csv`: Unlabeled dataset of Variants of Unknown Significance (VUS) for downstream inference.

---

## 📊 Dataset Inventory & File Specification

| Dataset Name | File Path | File Format | File Size | Observations (Rows) | Variables (Columns) | Primary Role |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `binary_df.csv` | `./binary_df.csv` | CSV (Comma Delimited) | 9.37 MB | 368,851 | 12 | Training & Benchmark Feature Matrix |
| `vus_only_variants.csv` | `./vus_only_variants.csv` | CSV (Comma Delimited) | 75.98 MB | 369,993 | 14 | Holdout VUS Reclassification Target |

---

## 🔬 Feature Schema (`binary_df.csv`)

| Variable Name | Data Type | Non-Null Count | Missing % | Unique Values | Description / Interpretation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `GERP++RS` | `int64` | 368,851 | 0.0% | 2 | Evolutionary Conservation Binary Flag |
| `polyphen2_HVAR_score` | `int64` | 368,851 | 0.0% | 2 | PolyPhen-2 HVAR Pathogenicity Score Flag |
| `polyphen2_HDIV_score` | `int64` | 368,851 | 0.0% | 2 | PolyPhen-2 HDIV Pathogenicity Score Flag |
| `sift_score` | `int64` | 368,851 | 0.0% | 2 | SIFT Pathogenicity Score Flag |
| `metaSVM_score` | `int64` | 368,851 | 0.0% | 2 | Ensemble MetaSVM Predictor Flag |
| `alphamissense_pred` | `float64` | 368,851 | 0.0% | 3 | **PRIMARY TARGET** (0.0: Benign, 0.5: VUS, 1.0: Pathogenic) |
| `alphamissense_score` | `int64` | 368,851 | 0.0% | 2 | AlphaMissense Continuous/Binary Score |
| `metaRNN_score` | `int64` | 368,851 | 0.0% | 2 | Ensemble MetaRNN Predictor Flag |
| `metaLR_score` | `int64` | 368,851 | 0.0% | 2 | Ensemble MetaLR Predictor Flag |
| `CADD_phred` | `int64` | 368,851 | 0.0% | 2 | CADD Phred-scaled Score Flag |
| `varity_r_score` | `int64` | 368,851 | 0.0% | 2 | VARITY R Score Flag |
| `AF_avg` | `int64` | 368,851 | 0.0% | 2 | Population Allele Frequency Flag |

---

## 📈 Summary Statistics Table (`binary_df.csv`)

```text
                         count      mean       std  min  25%  50%  75%  max
GERP++RS              368851.0  0.884108  0.320096  0.0  1.0  1.0  1.0  1.0
polyphen2_HVAR_score  368851.0  0.452240  0.497714  0.0  0.0  0.0  1.0  1.0
polyphen2_HDIV_score  368851.0  0.567638  0.495405  0.0  0.0  1.0  1.0  1.0
sift_score            368851.0  0.107266  0.309451  0.0  0.0  0.0  0.0  1.0
metaSVM_score         368851.0  0.196548  0.397388  0.0  0.0  0.0  0.0  1.0
alphamissense_pred    368851.0  0.290532  0.394821  0.0  0.0  0.0  0.5  1.0
alphamissense_score   368851.0  0.237562  0.425590  0.0  0.0  0.0  0.0  1.0
metaRNN_score         368851.0  0.401956  0.490294  0.0  0.0  0.0  1.0  1.0
metaLR_score          368851.0  0.391247  0.488030  0.0  0.0  0.0  1.0  1.0
CADD_phred            368851.0  0.897330  0.303528  0.0  1.0  1.0  1.0  1.0
varity_r_score        368851.0  0.286373  0.452066  0.0  0.0  0.0  1.0  1.0
AF_avg                368851.0  0.459570  0.498363  0.0  0.0  0.0  1.0  1.0
```
