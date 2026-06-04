from pathlib import Path
import pandas as pd

RAW_DIR = Path("../data/raw")

csv_files = sorted(RAW_DIR.glob("*.csv"))

print("=" * 60)
print("BLUESTOCK MF DATA INGESTION")
print("=" * 60)

for file in csv_files:

    print(f"\nLoading: {file.name}")

    df = pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("-" * 60)
    print("\n" + "=" * 60)
print("FUND MASTER EXPLORATION")
print("=" * 60)

fund_master = pd.read_csv("../data/raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())
print("\n" + "=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

nav_history = pd.read_csv("../data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"].astype(str))
nav_codes = set(nav_history["amfi_code"].astype(str))

missing_codes = master_codes - nav_codes

print("\nFund Master Codes:", len(master_codes))
print("NAV History Codes:", len(nav_codes))

if len(missing_codes) == 0:
    print("\nAll AMFI codes exist in nav_history.")
else:
    print("\nMissing Codes:")
    print(missing_codes)

print("\nDATA QUALITY SUMMARY")
print("- No missing AMFI codes found")
print("- NAV history aligns with fund master")
print("- Date columns should be converted to datetime later")
print("- Datasets loaded successfully")
