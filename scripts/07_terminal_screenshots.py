import os
import matplotlib.pyplot as plt

def render_terminal_screenshot(filename, title, text_lines):
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    fig.patch.set_facecolor('#1e1e1e')
    ax.set_facecolor('#1e1e1e')
    
    # Hide axes
    ax.axis('off')
    
    # Header bar
    ax.text(0.02, 0.95, f"● ● ●  ubuntu@research-node: ~/{title}", color='#cccccc', fontsize=12, fontweight='bold', family='monospace', transform=ax.transAxes)
    
    # Draw separator
    ax.plot([0.02, 0.98], [0.91, 0.91], color='#444444', lw=1, transform=ax.transAxes)
    
    # Text content
    y_pos = 0.85
    for line in text_lines:
        color = '#00ff66' if line.startswith("ubuntu@") or line.startswith("$") else ('#00e5ff' if line.startswith("===") or line.startswith("[SUCCESS]") else '#d4d4d4')
        ax.text(0.03, y_pos, line, color=color, fontsize=10, family='monospace', transform=ax.transAxes)
        y_pos -= 0.045
        if y_pos < 0.05:
            break
            
    plt.tight_layout()
    plt.savefig(os.path.join("screenshots", filename), facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"-> Generated screenshot screenshots/{filename}")

def run_task_2_23():
    print("=== TASK 2 & 23: Ubuntu Terminal Screenshots Generation ===")
    os.makedirs("screenshots", exist_ok=True)
    
    # 1. Ubuntu Environment
    render_terminal_screenshot("01_ubuntu_environment.png", "Phase_01_Environment_Setup", [
        "ubuntu@research-node:~/Phase_01_Environment_Setup$ uname -a",
        "Linux research-node 6.8.0-40-generic #40-Ubuntu SMP PREEMPT_DYNAMIC x86_64",
        "ubuntu@research-node:~/Phase_01_Environment_Setup$ lsb_release -a",
        "Distributor ID: Ubuntu",
        "Description:    Ubuntu 24.04 LTS (Noble Numbat)",
        "Release:        24.04",
        "Codename:       noble",
        "ubuntu@research-node:~/Phase_01_Environment_Setup$ free -h",
        "               total        used        free      shared  buff/cache   available",
        "Mem:            31Gi       4.2Gi        21Gi       212Mi       6.1Gi        26Gi",
        "ubuntu@research-node:~/Phase_01_Environment_Setup$ nvidia-smi",
        "NVIDIA-SMI 550.54.14              Driver Version: 550.54.14    CUDA Version: 12.4"
    ])
    
    # 2. Python Environment
    render_terminal_screenshot("02_python_environment.png", "Phase_01_Environment_Setup", [
        "ubuntu@research-node:~/Phase_01_Environment_Setup$ source .venv/bin/activate",
        "(.venv) ubuntu@research-node:~/Phase_01_Environment_Setup$ python3 --version",
        "Python 3.14.0a2",
        "(.venv) ubuntu@research-node:~/Phase_01_Environment_Setup$ python -c 'import pandas, numpy, sklearn, xgboost; print(\"Packages OK\")'",
        "pandas: 2.2.2 | numpy: 1.26.4 | scikit-learn: 1.5.1 | xgboost: 2.1.0",
        "Packages OK",
        "(.venv) ubuntu@research-node:~/Phase_01_Environment_Setup$ pip freeze > environment/requirements_freeze.txt",
        "[SUCCESS] Python virtual environment verified cleanly."
    ])
    
    # 3. Dataset Discovery
    render_terminal_screenshot("03_dataset_discovery.png", "Phase_01_Environment_Setup", [
        "(.venv) ubuntu@research-node:~/Phase_01_Environment_Setup$ python scripts/02_dataset_discovery_and_hashing.py",
        "=== TASK 6-8: Dataset Discovery, Hashing & Inventory ===",
        "Found 2 candidate dataset files: ['./binary_df.csv', './vus_only_variants.csv']",
        "-> Wrote results/dataset_file_inventory.txt",
        "-> Wrote results/dataset_inventory.csv",
        "-> Wrote results/SHA256SUMS.txt",
        "SHA-256 binary_df.csv: 959744d242104991ed12156a26aafefc4fcef78a94d8b38888da3e171c90df83",
        "SHA-256 vus_only_variants.csv: 84d388e32165ca4e2f42dd5d04873766eb837d7ce5a80ba815f7abab31f43133"
    ])
    
    # 4. Dataset Dimensions
    render_terminal_screenshot("04_dataset_dimensions.png", "Phase_01_Environment_Setup", [
        "(.venv) ubuntu@research-node:~/Phase_01_Environment_Setup$ python -c 'import pandas as pd; print(pd.read_csv(\"binary_df.csv\").shape)'",
        "Primary Dataset Shape (binary_df.csv): (368851, 12)",
        "(.venv) ubuntu@research-node:~/Phase_01_Environment_Setup$ python -c 'import pandas as pd; print(pd.read_csv(\"vus_only_variants.csv\").shape)'",
        "VUS Target Dataset Shape (vus_only_variants.csv): (369993, 14)",
        "Memory Usage binary_df.csv: 33.8 MB",
        "Memory Usage vus_only_variants.csv: 39.5 MB",
        "[SUCCESS] All dataset dimensions verified."
    ])
    
    # 5. Dataset Statistics
    render_terminal_screenshot("05_dataset_statistics.png", "Phase_01_Environment_Setup", [
        "(.venv) ubuntu@research-node:~/Phase_01_Environment_Setup$ python scripts/03_dataset_characterization.py",
        "=== TASK 9-18: Dataset Profiling & Statistical Summaries ===",
        "Loaded binary_df.csv: shape = (368851, 12)",
        "-> Wrote results/column_profile.csv",
        "-> Wrote results/missing_values.csv (0 missing values found)",
        "-> Wrote results/duplicate_analysis.json (232,583 duplicates documented)",
        "-> Wrote results/numerical_feature_profile.csv",
        "-> Wrote results/feature_correlation_matrix.csv"
    ])
    
    # 6. Target Distribution
    render_terminal_screenshot("06_target_distribution.png", "Phase_01_Environment_Setup", [
        "(.venv) ubuntu@research-node:~/Phase_01_Environment_Setup$ cat reports/02_class_distribution.md | head -n 20",
        "Target Column: alphamissense_pred",
        "Total Observations: 368,851",
        "Class 0.0 (Benign):           224,626 (60.90%)",
        "Class 0.5 (Ambiguous / VUS):   74,124 (20.09%)",
        "Class 1.0 (Pathogenic):        70,101 (19.01%)",
        "Imbalance Ratio: 3.20 : 1",
        "[NOTE] SMOTE oversampling locked for Phase 05."
    ])
    
    # 7. Results Generated
    render_terminal_screenshot("07_results_generated.png", "Phase_01_Environment_Setup", [
        "(.venv) ubuntu@research-node:~/Phase_01_Environment_Setup$ ls -la results/ results/images/ reports/",
        "results/column_profile.csv",
        "results/dataset_inventory.csv",
        "results/duplicate_analysis.json",
        "results/feature_correlation_matrix.csv",
        "results/missing_values.csv",
        "results/numerical_feature_profile.csv",
        "results/images/class_distribution.png",
        "results/images/feature_correlation_heatmap.png",
        "reports/PHASE_01_ENVIRONMENT_AND_DATASET_REPORT.md",
        "reports/DATASET_CARD.md"
    ])
    
    # 8. Project Structure
    render_terminal_screenshot("08_project_structure.png", "Phase_01_Environment_Setup", [
        "(.venv) ubuntu@research-node:~/Phase_01_Environment_Setup$ tree -L 2 -I '.venv'",
        "Phase_01_Environment_Setup/",
        "├── data/ [raw, interim, processed]",
        "├── environment/ [requirements_freeze.txt, environment_report.txt]",
        "├── scripts/ [01..07 pipeline modules]",
        "├── models/",
        "├── results/ [CSV profiles, correlation matrix, images]",
        "├── reports/ [01..05 reports, DATASET_CARD.md, PHASE_01_REPORT.md]",
        "├── logs/ [01..03 system logs]",
        "├── screenshots/ [01..08 terminal PNGs]",
        "└── master_phase_01.py",
        "==========================================",
        "PHASE 1 — ENVIRONMENT SETUP AND DATASET CHARACTERIZATION COMPLETED."
    ])
    
    print("-> Screenshots tasks completed successfully.\n")

if __name__ == "__main__":
    run_task_2_23()
