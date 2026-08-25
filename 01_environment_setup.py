import sys, os, pandas, numpy, scipy, sklearn, xgboost, lightgbm, catboost, shap, joblib
import pandas as pd
print("=== Phase 01: Environment Setup & Package Verification ===")
env_data = [
    {"Package": "Python", "Version": sys.version.split()[0]},
    {"Package": "pandas", "Version": pandas.__version__},
    {"Package": "numpy", "Version": numpy.__version__},
    {"Package": "scipy", "Version": scipy.__version__},
    {"Package": "scikit-learn", "Version": sklearn.__version__},
    {"Package": "xgboost", "Version": xgboost.__version__},
    {"Package": "lightgbm", "Version": lightgbm.__version__},
    {"Package": "catboost", "Version": catboost.__version__},
    {"Package": "shap", "Version": shap.__version__},
    {"Package": "joblib", "Version": joblib.__version__}
]
df_env = pd.DataFrame(env_data)
df_env.to_csv("environment_report.csv", index=False)
print("Environment report saved to environment_report.csv")
