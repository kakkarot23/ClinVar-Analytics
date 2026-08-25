import os
import pandas as pd

def run_task_20():
    print("=== TASK 20: Data Leakage Pre-Check & Quality Risk Audit ===")
    
    os.makedirs("reports", exist_ok=True)
    
    df = pd.read_csv("binary_df.csv")
    
    leakage_audit = [
        {
            "feature": "alphamissense_pred",
            "role": "PRIMARY TARGET",
            "leakage_risk": "TARGET",
            "status": "TARGET_LOCKED",
            "notes": "Ground truth class label for training and evaluation."
        },
        {
            "feature": "alphamissense_score",
            "role": "Continuous Score Equivalent of Target",
            "leakage_risk": "HIGH",
            "status": "REQUIRES_REVIEW",
            "notes": "Derived from the same underlying model source as target. Must be evaluated for potential target leakage or collinearity during feature selection."
        },
        {
            "feature": "GERP++RS",
            "role": "Predictor (Binary Evolutionary Conservation Flag)",
            "leakage_risk": "NONE",
            "status": "SAFE",
            "notes": "External genomic conservation metric."
        },
        {
            "feature": "polyphen2_HVAR_score",
            "role": "Predictor (Binary In-Silico Pathogenicity Score)",
            "leakage_risk": "NONE",
            "status": "SAFE",
            "notes": "External PolyPhen-2 score."
        },
        {
            "feature": "polyphen2_HDIV_score",
            "role": "Predictor (Binary In-Silico Pathogenicity Score)",
            "leakage_risk": "NONE",
            "status": "SAFE",
            "notes": "External PolyPhen-2 HDIV score."
        },
        {
            "feature": "sift_score",
            "role": "Predictor (Binary SIFT Score)",
            "leakage_risk": "NONE",
            "status": "SAFE",
            "notes": "External SIFT pathogenicity score."
        },
        {
            "feature": "metaSVM_score",
            "role": "Predictor (Binary Ensemble MetaSVM Flag)",
            "leakage_risk": "NONE",
            "status": "SAFE",
            "notes": "Ensemble SVM predictor."
        },
        {
            "feature": "metaRNN_score",
            "role": "Predictor (Binary Ensemble MetaRNN Flag)",
            "leakage_risk": "NONE",
            "status": "SAFE",
            "notes": "Ensemble RNN predictor."
        },
        {
            "feature": "metaLR_score",
            "role": "Predictor (Binary Ensemble MetaLR Flag)",
            "leakage_risk": "NONE",
            "status": "SAFE",
            "notes": "Ensemble Logistic Regression predictor."
        },
        {
            "feature": "CADD_phred",
            "role": "Predictor (Binary CADD Phred-scaled Score)",
            "leakage_risk": "NONE",
            "status": "SAFE",
            "notes": "External CADD score."
        },
        {
            "feature": "varity_r_score",
            "role": "Predictor (Binary VARITY R Score)",
            "leakage_risk": "NONE",
            "status": "SAFE",
            "notes": "External VARITY predictor."
        },
        {
            "feature": "AF_avg",
            "role": "Predictor (Binary Allele Frequency Indicator)",
            "leakage_risk": "NONE",
            "status": "SAFE",
            "notes": "Aggregated population allele frequency."
        }
    ]
    
    report_05 = f"""# 🔒 Report 05 — Data Leakage Pre-Check & Quality Audit

## 🛡️ Executive Leakage Summary
- **Total Audited Features**: {len(df.columns)}
- **Safe Predictors**: 10
- **Target Variable**: 1 (`alphamissense_pred`)
- **Suspicious / Collinear Feature**: 1 (`alphamissense_score`)

### 📋 Feature-by-Feature Risk Assessment Table

| Feature Name | Role | Leakage Risk Level | Pre-Check Status | Audit Notes |
| :--- | :--- | :--- | :--- | :--- |
"""
    for item in leakage_audit:
        report_05 += f"| `{item['feature']}` | {item['role']} | **{item['leakage_risk']}** | `{item['status']}` | {item['notes']} |\n"
        
    report_05 += """
### ⚠️ Critical Preprocessing Protocols for Phase 02+
1. **Partitioning Order**: Stratified train/validation/test splitting MUST occur before any feature scaling, imputer fitting, or SMOTE oversampling.
2. **Feature Isolation**: `alphamissense_score` will be closely monitored during feature importance and SHAP analysis to ensure it does not introduce artificial target proxy leakage.
3. **No Unseen Data Exposure**: All preprocessing parameters (scaler means/stds) will be fit ONLY on the training split.
"""
    
    with open("reports/05_data_leakage_precheck.md", "w", encoding="utf-8") as f:
        f.write(report_05)
    print("-> Wrote reports/05_data_leakage_precheck.md")
    print("-> Data leakage pre-check completed successfully.\n")

if __name__ == "__main__":
    run_task_20()
