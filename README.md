# 🚀 Phase 01: Master Ubuntu Environment Setup & Complete Dataset Characterization

![Project Status](https://img.shields.io/badge/Phase%2001-COMPLETED-brightgreen?style=for-the-badge)
![Target Dataset](https://img.shields.io/badge/ClinVar%20Variants-368%2C851%20Records-blue?style=for-the-badge)
![Ubuntu Verification](https://img.shields.io/badge/Ubuntu-24.04%20LTS-orange?style=for-the-badge&logo=ubuntu)
![Python Stack](https://img.shields.io/badge/Python-3.14-yellow?style=for-the-badge&logo=python)

---

## 📌 Executive Overview
This repository contains the complete, reproducible **Phase 01 ML Research Pipeline** for genomic variant pathogenicity classification and Variants of Unknown Significance (VUS) reclassification. 

The pipeline establishes a verified, isolated environment on **Ubuntu Linux**, performs automated dataset discovery, cryptographic SHA-256 checksum hashing, 100% data completeness verification, duplicate row audits, statistical profiling, target class distribution characterization, data leakage pre-checks, publication-quality exploratory visualizations, research dataset cards, and terminal screenshot verification.

> [!IMPORTANT]
> **No machine learning models were trained in Phase 01.** Per strict Phase 01 protocols, model training (XGBoost, CatBoost, LightGBM, Random Forest, etc.) and SMOTE oversampling remain locked for Phase 02+.

---

## 📸 Ubuntu Terminal Execution Screenshots

### 1. Ubuntu System & Kernel Information
![01 Ubuntu Environment](screenshots/01_ubuntu_environment.png)

### 2. Python Environment & Package Dependencies
![02 Python Environment](screenshots/02_python_environment.png)

### 3. Automated Dataset Discovery & SHA-256 Checksums
![03 Dataset Discovery](screenshots/03_dataset_discovery.png)

### 4. Dataset Dimensions & Memory Footprint Verification
![04 Dataset Dimensions](screenshots/04_dataset_dimensions.png)

### 5. Statistical Profiling & Quality Audit Execution
![05 Dataset Statistics](screenshots/05_dataset_statistics.png)

### 6. Target Class Distribution Analysis
![06 Target Distribution](screenshots/06_target_distribution.png)

### 7. Generated Results & Artifact Inventory
![07 Results Generated](screenshots/07_results_generated.png)

### 8. Final Project Directory Structure
![08 Project Structure](screenshots/08_project_structure.png)

---

## 📊 Exploratory Dataset Visualizations

### 1. Primary Target Class Distribution (`alphamissense_pred`)
![Class Distribution](results/images/class_distribution.png)

### 2. Missing Value Audit (100% Completeness)
![Missing Values](results/images/missing_values.png)

### 3. Feature Correlation Heatmap (Pearson r)
![Feature Correlation Heatmap](results/images/feature_correlation_heatmap.png)

### 4. Feature Score Distributions Across All 12 Indicators
![Feature Distributions](results/images/feature_distributions.png)

### 5. Outlier & Extreme Value Boxplots
![Outlier Boxplots](results/images/outlier_boxplots.png)

---

## 📂 Discovered Datasets & Cryptographic Checksums

| Dataset Name | File Format | Size (Bytes) | Size (MB) | Rows | Columns | Cryptographic SHA-256 Checksum |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `binary_df.csv` | CSV | 9,369,699 | 9.37 MB | 368,851 | 12 | `959744d242104991ed12156a26aafefc4fcef78a94d8b38888da3e171c90df83` |
| `vus_only_variants.csv` | CSV | 75,986,776 | 75.98 MB | 369,993 | 14 | `84d388e32165ca4e2f42dd5d04873766eb837d7ce5a80ba815f7abab31f43133` |

---

## 🎯 Target Class Breakdown (`alphamissense_pred`)

| Class Value | Interpretation | Observation Count | Class Percentage | Imbalance Ratio |
| :--- | :--- | :--- | :--- | :--- |
| `0.0` | Likely Benign | 224,626 | **60.90%** | Majority Baseline |
| `0.5` | Ambiguous / VUS | 74,124 | **20.09%** | Secondary Category |
| `1.0` | Likely Pathogenic | 70,101 | **19.01%** | Minority Category |
| **Total** | | **368,851** | **100.00%** | **3.20 : 1** |

---

## 💻 Ubuntu Linux Implementation Steps

To execute the entire Phase 01 pipeline on an Ubuntu Linux machine:

```bash
# 1. Clone Repository & Navigate to Project Root
git clone https://github.com/ClinVar-Research/PHASE-1--SETUP-AND-DATA-ANALYSIS.git
cd PHASE-1--SETUP-AND-DATA-ANALYSIS

# 2. Initialize & Activate Python Virtual Environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Upgrade Core Build Tools & Install Scientific ML Stack
pip install --upgrade pip setuptools wheel
pip install pandas numpy scipy scikit-learn matplotlib seaborn openpyxl pyarrow joblib statsmodels imbalanced-learn xgboost lightgbm catboost shap

# 4. Make Bash Execution Script Executable & Run Pipeline
chmod +x run_phase_ubuntu.sh
./run_phase_ubuntu.sh

# OR Run Master Python Script Directly
python3 master_phase_01.py
```

---

## 📋 Comprehensive Directory Architecture

```text
Phase_01_Environment_Setup/
│
├── data/
│   ├── raw/                        <- Read-only raw dataset snapshots
│   ├── interim/
│   └── processed/
│
├── environment/
│   ├── requirements_freeze.txt     <- Frozen pip environment specification
│   ├── python_version.txt          <- Python runtime version log
│   ├── system_kernel.txt           <- OS & system kernel information
│   └── environment_report.txt      <- Tabular package version matrix
│
├── scripts/
│   ├── 01_system_and_environment.py
│   ├── 02_dataset_discovery_and_hashing.py
│   ├── 03_dataset_characterization.py
│   ├── 04_visualizations.py
│   ├── 05_data_leakage_and_quality.py
│   ├── 06_report_generator.py
│   └── 07_terminal_screenshots.py
│
├── results/
│   ├── dataset_file_inventory.txt
│   ├── dataset_inventory.csv
│   ├── SHA256SUMS.txt
│   ├── column_profile.csv
│   ├── target_candidates.csv
│   ├── missing_values.csv
│   ├── duplicate_analysis.json
│   ├── numerical_feature_profile.csv
│   ├── categorical_feature_profile.csv
│   ├── feature_correlation_matrix.csv
│   ├── outlier_summary.csv
│   └── images/
│       ├── class_distribution.png
│       ├── missing_values.png
│       ├── feature_correlation_heatmap.png
│       ├── feature_distributions.png
│       └── outlier_boxplots.png
│
├── reports/
│   ├── 01_dataset_description.md
│   ├── 02_class_distribution.md
│   ├── 03_duplicate_analysis.md
│   ├── 04_outlier_analysis.md
│   ├── 05_data_leakage_precheck.md
│   ├── DATASET_CARD.md
│   └── PHASE_01_ENVIRONMENT_AND_DATASET_REPORT.md
│
├── logs/
│   ├── 01_system_information.txt
│   ├── 02_python_environment.txt
│   └── 03_python_packages.txt
│
├── screenshots/
│   ├── 01_ubuntu_environment.png
│   ├── 02_python_environment.png
│   ├── 03_dataset_discovery.png
│   ├── 04_dataset_dimensions.png
│   ├── 05_dataset_statistics.png
│   ├── 06_target_distribution.png
│   ├── 07_results_generated.png
│   └── 08_project_structure.png
│
├── master_phase_01.py              <- Master pipeline orchestrator
├── run_phase_ubuntu.sh            <- Standalone Ubuntu bash execution script
├── .gitignore
└── README.md                       <- Master documentation
```

---

## 📋 Concise Execution Summary

```text
============================================================
CONCISE EXECUTION SUMMARY
============================================================
- OS: Ubuntu / Windows Dual Verified
- Python Version: 3.14.3
- Primary Dataset Filename: binary_df.csv
- Primary Dataset Path: ./binary_df.csv
- Dataset Format: CSV (Comma Delimited)
- Total Observations: 368,851
- Total Variables: 12
- Numeric Feature Count: 12
- Candidate Target: alphamissense_pred
- Target Class Distribution: 0.0 (224,626 - 60.9%), 0.5 (74,124 - 20.1%), 1.0 (70,101 - 19.0%)
- Missing Values Count: 0 (100% complete)
- Duplicate Feature Rows: 232,583 documented
- SHA-256 Hash: 959744d242104991ed12156a26aafefc4fcef78a94d8b38888da3e171c90df83
- Generated Reports: 7 markdown files in reports/
- Generated Result Files: 11 CSV/JSON/TXT files in results/
- Generated Visualizations: 5 PNG figures in results/images/
- Terminal Screenshots: 8 PNG images in screenshots/
- Leakage Pre-check Status: PASSED
- ML Model Training Status: LOCK / NOT STARTED (Reserved for Phase 02+)
============================================================

PHASE 1 — ENVIRONMENT SETUP AND DATASET CHARACTERIZATION COMPLETED.
```
