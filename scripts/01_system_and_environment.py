import sys
import os
import platform
import subprocess
import pandas as pd
import numpy as np
import scipy
import sklearn
import xgboost
import lightgbm
import catboost
import shap
import imblearn
import joblib

def run_task_1_to_5():
    print("=== TASK 1-5: System & Python Environment Setup & Verification ===")
    
    # Directories
    os.makedirs("environment", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    
    # Task 1 — System Info Log
    sys_info = []
    sys_info.append(f"OS: {platform.system()} {platform.release()} ({platform.version()})")
    sys_info.append(f"Architecture: {platform.architecture()[0]}")
    sys_info.append(f"Machine: {platform.machine()}")
    sys_info.append(f"Processor: {platform.processor()}")
    sys_info.append(f"Python Executable: {sys.executable}")
    sys_info.append(f"Host: {platform.node()}")
    
    # Check GPU
    try:
        res = subprocess.run(["nvidia-smi"], capture_output=True, text=True)
        if res.returncode == 0:
            gpu_info = res.stdout
        else:
            gpu_info = "GPU: Not available / not configured"
    except Exception:
        gpu_info = "GPU: Not available / not configured"
    
    sys_info.append(f"GPU Info: {gpu_info.strip()}")
    
    with open("logs/01_system_information.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(sys_info))
    print("-> Wrote logs/01_system_information.txt")
    
    # Task 3 — Python Environment Log
    py_env = []
    py_env.append(f"Python Version: {sys.version}")
    py_env.append(f"Python Executable: {sys.executable}")
    py_env.append(f"Platform: {sys.platform}")
    
    with open("logs/02_python_environment.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(py_env))
    print("-> Wrote logs/02_python_environment.txt")
    
    # Task 4 — Dependencies Verification
    packages = [
        ("pandas", pd.__version__),
        ("numpy", np.__version__),
        ("scipy", scipy.__version__),
        ("scikit-learn", sklearn.__version__),
        ("xgboost", xgboost.__version__),
        ("lightgbm", lightgbm.__version__),
        ("catboost", catboost.__version__),
        ("shap", shap.__version__),
        ("imbalanced-learn", imblearn.__version__),
        ("joblib", joblib.__version__)
    ]
    
    pkg_str = "\n".join([f"{name}: {ver}" for name, ver in packages])
    with open("logs/03_python_packages.txt", "w", encoding="utf-8") as f:
        f.write(pkg_str)
    print("-> Wrote logs/03_python_packages.txt")
    
    # Task 5 — Freeze Environment
    with open("environment/python_version.txt", "w", encoding="utf-8") as f:
        f.write(f"Python {sys.version.split()[0]}\n")
        
    with open("environment/system_kernel.txt", "w", encoding="utf-8") as f:
        f.write(f"{platform.system()} {platform.release()}\n")
        
    # environment_report.csv
    df_env = pd.DataFrame([{"Package": name, "Version": ver} for name, ver in packages])
    df_env.to_csv("environment/environment_report.txt", sep="\t", index=False)
    
    # requirements_freeze.txt
    try:
        res = subprocess.run([sys.executable, "-m", "pip", "freeze"], capture_output=True, text=True)
        if res.returncode == 0:
            with open("environment/requirements_freeze.txt", "w", encoding="utf-8") as f:
                f.write(res.stdout)
    except Exception as e:
        print("pip freeze warning:", e)
        
    print("-> Environment tasks completed successfully.\n")

if __name__ == "__main__":
    run_task_1_to_5()
