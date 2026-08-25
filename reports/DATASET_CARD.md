# 🃏 Research Dataset Card

## Dataset Metadata
- **Dataset Name**: Genomic Variant In-Silico Pathogenicity & VUS Reclassification Dataset
- **Dataset Location**: `Phase_01_Environment_Setup/`
- **Primary Feature Matrix**: `binary_df.csv` (368,851 rows × 12 columns, 9.37 MB)
- **VUS Target Matrix**: `vus_only_variants.csv` (369,993 rows × 14 columns, 75.98 MB)
- **Cryptographic Hash (SHA-256)**:
  - `binary_df.csv`: `959744d242104991ed12156a26aafefc4fcef78a94d8b38888da3e171c90df83`
  - `vus_only_variants.csv`: `84d388e32165ca4e2f42dd5d04873766eb837d7ce5a80ba815f7abab31f43133`

## Dataset Overview & Intended ML Task
- **Intended Task**: Multi-class and Binary Classification of genomic variants into Benign (`0.0`), VUS (`0.5`), and Pathogenic (`1.0`) categories using ensemble machine learning models.
- **Target Variable**: `alphamissense_pred`
- **Class Distribution**:
  - Class `0.0` (Likely Benign): 224,626 (60.90%)
  - Class `0.5` (Ambiguous / VUS): 74,124 (20.09%)
  - Class `1.0` (Likely Pathogenic): 70,101 (19.01%)

## Feature Categories & Missing Data
- **Feature Categories**: Evolutionary conservation (`GERP++RS`), protein structure prediction (`PolyPhen-2`, `SIFT`), ensemble machine learning scores (`MetaSVM`, `MetaRNN`, `MetaLR`), deep learning scores (`AlphaMissense`), and population allele frequency (`AF_avg`).
- **Missing Data**: 0 missing values across all 12 features (100% complete).
- **Exact Duplicate Records**: 232,583 exact duplicate feature rows (representing shared binary predictor signatures across variants).

## Data Quality & Leakage Risk Assessment
- **Leakage Risk**: Low to Moderate. `alphamissense_score` is flagged for close monitoring during feature selection.
- **Quality Status**: High. All indicator metrics fall within strictly validated ranges.

## Ethical & Clinical Considerations
- Models trained on this dataset provide computational pathogenicity predictions for research purposes.
- Predictions do NOT replace clinical diagnostic confirmation or functional laboratory validation.

## Recommended Validation Strategy
- 5-Fold Stratified Cross-Validation on `binary_df.csv` with a locked 20% holdout test set.
- Final evaluation on `vus_only_variants.csv` in Phase 06.
