import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_task_19():
    print("=== TASK 19: Exploratory Dataset Visualizations ===")
    
    os.makedirs("results/images", exist_ok=True)
    
    # Set style
    sns.set_theme(style="whitegrid", palette="muted")
    plt.rcParams.update({'font.sans-serif': 'DejaVu Sans', 'font.size': 10})
    
    df = pd.read_csv("binary_df.csv")
    
    # 1. Class Distribution Bar Chart
    plt.figure(figsize=(8, 5))
    ax = sns.countplot(x="alphamissense_pred", data=df, hue="alphamissense_pred", palette="viridis", legend=False)
    plt.title("Primary Target Class Distribution (alphamissense_pred)", fontsize=13, fontweight='bold', pad=15)
    plt.xlabel("Class Label (0.0: Benign, 0.5: Ambiguous/VUS, 1.0: Pathogenic)", labelpad=10)
    plt.ylabel("Count of Variants", labelpad=10)
    
    total = len(df)
    for p in ax.patches:
        height = p.get_height()
        pct = (height / total) * 100
        ax.annotate(f'{height:,}\n({pct:.1f}%)', (p.get_x() + p.get_width() / 2., height / 2),
                    ha='center', va='center', fontsize=10, color='white', fontweight='bold')
                    
    plt.tight_layout()
    plt.savefig("results/images/class_distribution.png", dpi=300)
    plt.close()
    print("-> Saved results/images/class_distribution.png")
    
    # 2. Missing Values Visualization
    plt.figure(figsize=(10, 4))
    missing_data = df.isnull().sum()
    ax = sns.barplot(x=missing_data.index, y=missing_data.values, hue=missing_data.index, palette="mako", legend=False)
    plt.title("Missing Value Count Across All Features (0 Missing Cells)", fontsize=13, fontweight='bold', pad=15)
    plt.xlabel("Feature Name", labelpad=10)
    plt.ylabel("Missing Count", labelpad=10)
    plt.xticks(rotation=45, ha='right')
    plt.ylim(0, 10)
    for p in ax.patches:
        ax.annotate('0 (0.0%)', (p.get_x() + p.get_width() / 2., 1), ha='center', va='bottom', fontsize=9)
    plt.tight_layout()
    plt.savefig("results/images/missing_values.png", dpi=300)
    plt.close()
    print("-> Saved results/images/missing_values.png")
    
    # 3. Correlation Heatmap
    plt.figure(figsize=(11, 9))
    corr = df.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    sns.heatmap(corr, mask=mask, cmap="coolwarm", vmax=1.0, vmin=-0.2, annot=True, fmt=".2f",
                square=True, linewidths=.5, cbar_kws={"shrink": .8})
    plt.title("Feature Correlation Heatmap (Pearson r)", fontsize=14, fontweight='bold', pad=15)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig("results/images/feature_correlation_heatmap.png", dpi=300)
    plt.close()
    print("-> Saved results/images/feature_correlation_heatmap.png")
    
    # 4. Feature Distributions Histograms
    df.hist(figsize=(14, 10), bins=20, color='teal', edgecolor='black', grid=True)
    plt.suptitle("Feature Score Distributions Across All 12 Indicators", fontsize=15, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig("results/images/feature_distributions.png", dpi=300)
    plt.close()
    print("-> Saved results/images/feature_distributions.png")
    
    # 5. Outlier Boxplots
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, palette="crest")
    plt.title("Feature Value Spread & Boxplots Across Indicators", fontsize=14, fontweight='bold', pad=15)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("results/images/outlier_boxplots.png", dpi=300)
    plt.close()
    print("-> Saved results/images/outlier_boxplots.png")
    
    print("-> All visualizations generated successfully.\n")

if __name__ == "__main__":
    run_task_19()
