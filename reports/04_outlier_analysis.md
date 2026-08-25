# 📈 Report 04 — Outlier & Extreme Value Analysis

## 📌 Overview
Outlier detection performed on binary and continuous indicator scores using 1.5 × IQR standard boundaries.

| Feature Name | Outlier Count (IQR) | Outlier Percentage | Interpretation |
| :--- | :--- | :--- | :--- |
| `GERP++RS` | 42,747 | 11.59% | Valid binary/indicator score | 
| `polyphen2_HVAR_score` | 0 | 0.00% | Valid binary/indicator score | 
| `polyphen2_HDIV_score` | 0 | 0.00% | Valid binary/indicator score | 
| `sift_score` | 39,565 | 10.73% | Valid binary/indicator score | 
| `metaSVM_score` | 72,497 | 19.65% | Valid binary/indicator score | 
| `alphamissense_pred` | 0 | 0.00% | Valid binary/indicator score | 
| `alphamissense_score` | 87,625 | 23.76% | Valid binary/indicator score | 
| `metaRNN_score` | 0 | 0.00% | Valid binary/indicator score | 
| `metaLR_score` | 0 | 0.00% | Valid binary/indicator score | 
| `CADD_phred` | 37,870 | 10.27% | Valid binary/indicator score | 
| `varity_r_score` | 0 | 0.00% | Valid binary/indicator score | 
| `AF_avg` | 0 | 0.00% | Valid binary/indicator score | 

> [!TIP]
> **Scientific Finding**: Outliers in binary score matrices correspond to rare variant indicator flags (e.g. `sift_score=1` or `metaSVM_score=1`). These represent genuine biological variation rather than data corruption. No records are deleted.
