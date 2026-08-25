# 🔒 Report 05 — Data Leakage Pre-Check & Quality Audit

## 🛡️ Executive Leakage Summary
- **Total Audited Features**: 12
- **Safe Predictors**: 10
- **Target Variable**: 1 (`alphamissense_pred`)
- **Suspicious / Collinear Feature**: 1 (`alphamissense_score`)

### 📋 Feature-by-Feature Risk Assessment Table

| Feature Name | Role | Leakage Risk Level | Pre-Check Status | Audit Notes |
| :--- | :--- | :--- | :--- | :--- |
| `alphamissense_pred` | PRIMARY TARGET | **TARGET** | `TARGET_LOCKED` | Ground truth class label for training and evaluation. |
| `alphamissense_score` | Continuous Score Equivalent of Target | **HIGH** | `REQUIRES_REVIEW` | Derived from the same underlying model source as target. Must be evaluated for potential target leakage or collinearity during feature selection. |
| `GERP++RS` | Predictor (Binary Evolutionary Conservation Flag) | **NONE** | `SAFE` | External genomic conservation metric. |
| `polyphen2_HVAR_score` | Predictor (Binary In-Silico Pathogenicity Score) | **NONE** | `SAFE` | External PolyPhen-2 score. |
| `polyphen2_HDIV_score` | Predictor (Binary In-Silico Pathogenicity Score) | **NONE** | `SAFE` | External PolyPhen-2 HDIV score. |
| `sift_score` | Predictor (Binary SIFT Score) | **NONE** | `SAFE` | External SIFT pathogenicity score. |
| `metaSVM_score` | Predictor (Binary Ensemble MetaSVM Flag) | **NONE** | `SAFE` | Ensemble SVM predictor. |
| `metaRNN_score` | Predictor (Binary Ensemble MetaRNN Flag) | **NONE** | `SAFE` | Ensemble RNN predictor. |
| `metaLR_score` | Predictor (Binary Ensemble MetaLR Flag) | **NONE** | `SAFE` | Ensemble Logistic Regression predictor. |
| `CADD_phred` | Predictor (Binary CADD Phred-scaled Score) | **NONE** | `SAFE` | External CADD score. |
| `varity_r_score` | Predictor (Binary VARITY R Score) | **NONE** | `SAFE` | External VARITY predictor. |
| `AF_avg` | Predictor (Binary Allele Frequency Indicator) | **NONE** | `SAFE` | Aggregated population allele frequency. |

### ⚠️ Critical Preprocessing Protocols for Phase 02+
1. **Partitioning Order**: Stratified train/validation/test splitting MUST occur before any feature scaling, imputer fitting, or SMOTE oversampling.
2. **Feature Isolation**: `alphamissense_score` will be closely monitored during feature importance and SHAP analysis to ensure it does not introduce artificial target proxy leakage.
3. **No Unseen Data Exposure**: All preprocessing parameters (scaler means/stds) will be fit ONLY on the training split.
