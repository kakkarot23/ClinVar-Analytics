# 📊 Report 02 — Target Class Distribution Analysis

## 🎯 Target Column: `alphamissense_pred`

- **Total Observations**: 368,851
- **Unique Classes**: 3

### 📈 Class Distribution Summary Table

| Class Label | Interpretation | Count | Percentage |
| :--- | :--- | :--- | :--- |
| `0.0` | Likely Benign | 224,626 | 60.90% |
| `0.5` | Ambiguous / VUS | 74,124 | 20.10% |
| `1.0` | Likely Pathogenic | 70,101 | 19.01% |

### ⚖️ Imbalance Metrics
- **Majority Class**: `0.0` (224,626 samples, 60.90%)
- **Minority Class**: `1.0` (70,101 samples, 19.01%)
- **Imbalance Ratio (Majority / Minority)**: 3.20 : 1

> [!NOTE]
> SMOTE / rebalancing techniques are intentionally **locked for Phase 05** to prevent data leakage during baseline profiling.
