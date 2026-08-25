import os
import glob
import hashlib
import time
import shutil
import pandas as pd

def get_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def run_task_6_to_8():
    print("=== TASK 6-8: Dataset Discovery, Hashing & Inventory ===")
    
    os.makedirs("results", exist_ok=True)
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/interim", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)
    
    # Task 6 — Dataset Discovery
    search_exts = ["*.csv", "*.tsv", "*.txt", "*.xlsx", "*.xls", "*.parquet", "*.json"]
    candidate_files = []
    
    for ext in search_exts:
        for fname in glob.glob(ext):
            if not fname.startswith("environment") and not fname.startswith("run_phase"):
                candidate_files.append(fname)
                
    # Also search subfolders except excluded
    for root, dirs, files in os.walk("."):
        # filter out excluded dirs
        dirs[:] = [d for d in dirs if d not in [".venv", "results", "logs", "screenshots", "reports", ".git", "scratch", "environment", "data"]]
        for f in files:
            for ext_pat in [".csv", ".tsv", ".parquet", ".json", ".xlsx"]:
                if f.endswith(ext_pat):
                    full_p = os.path.normpath(os.path.join(root, f))
                    if full_p not in candidate_files and not full_p.startswith("environment"):
                        candidate_files.append(full_p)
                        
    # Sort files
    candidate_files = sorted(list(set(candidate_files)))
    
    print(f"Found {len(candidate_files)} candidate dataset files: {candidate_files}")
    
    with open("results/dataset_file_inventory.txt", "w", encoding="utf-8") as f:
        f.write("=== DATASET FILE INVENTORY ===\n")
        for cf in candidate_files:
            f.write(f"{os.path.abspath(cf)}\n")
    print("-> Wrote results/dataset_file_inventory.txt")
    
    # Task 7 — Dataset Inventory & Copy to data/raw/
    inventory_records = []
    sha_records = []
    
    for cf in candidate_files:
        abs_p = os.path.abspath(cf)
        fsize = os.path.getsize(cf)
        mtime = time.ctime(os.path.getmtime(cf))
        ext = os.path.splitext(cf)[1].lower()
        sha = get_sha256(cf)
        sha_records.append(f"{sha}  {os.path.basename(cf)}")
        
        # Read dimensions
        rows, cols = 0, 0
        try:
            if ext == ".csv":
                df_temp = pd.read_csv(cf)
                rows, cols = df_temp.shape
            elif ext == ".tsv" or ext == ".txt":
                df_temp = pd.read_csv(cf, sep="\t")
                rows, cols = df_temp.shape
            elif ext == ".parquet":
                df_temp = pd.read_parquet(cf)
                rows, cols = df_temp.shape
        except Exception as e:
            print(f"Could not read shape of {cf}: {e}")
            
        role = "Primary Feature Matrix" if "binary" in cf.lower() else ("VUS Holdout Target Matrix" if "vus" in cf.lower() else "Auxiliary Dataset")
        
        inventory_records.append({
            "file_name": os.path.basename(cf),
            "absolute_path": abs_p,
            "file_type": ext,
            "file_size_bytes": fsize,
            "modified_time": mtime,
            "rows": rows,
            "columns": cols,
            "candidate_role": role
        })
        
        # Copy to data/raw/ if not already there
        target_raw_path = os.path.join("data/raw", os.path.basename(cf))
        if not os.path.exists(target_raw_path):
            shutil.copy2(cf, target_raw_path)
            print(f"-> Copied read-only snapshot to {target_raw_path}")
            
    df_inv = pd.DataFrame(inventory_records)
    df_inv.to_csv("results/dataset_inventory.csv", index=False)
    print("-> Wrote results/dataset_inventory.csv")
    
    # Task 8 — RAW Data Hash
    with open("results/SHA256SUMS.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(sha_records) + "\n")
    print("-> Wrote results/SHA256SUMS.txt")
    print("-> Discovery and hashing completed.\n")

if __name__ == "__main__":
    run_task_6_to_8()
