import pandas as pd
from pathlib import Path

RAW = Path("../data/raw")
PROCESSED = Path("../data/processed")

PROCESSED.mkdir(exist_ok=True)

print("Data Cleaning Started...")

nav = pd.read_csv(
    RAW / "02_nav_history.csv"
)

print("\nNAV History Shape:")
print(nav.shape)

print("\nColumns:")
print(nav.columns)
# Convert date column

nav["date"] = pd.to_datetime(nav["date"])

# Sort by scheme and date

nav = nav.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicate rows

before = len(nav)

nav = nav.drop_duplicates()

after = len(nav)

print("\nDuplicates Removed:")
print(before - after)

# Check invalid NAV

invalid_nav = nav[
    nav["nav"] <= 0
]

print("\nInvalid NAV Rows:")
print(len(invalid_nav))

# Forward fill missing NAV

nav["nav"] = (
    nav.groupby("amfi_code")["nav"]
       .ffill()
)

# Save cleaned file

nav.to_csv(
    PROCESSED / "clean_nav_history.csv",
    index=False
)

print("\nNAV History Cleaned Successfully")
print("\n" + "=" * 50)
print("INVESTOR TRANSACTIONS")
print("=" * 50)

tx = pd.read_csv(
    RAW / "08_investor_transactions.csv"
)

print("\nShape:")
print(tx.shape)

print("\nColumns:")
print(tx.columns)
# -----------------------------
# CLEAN INVESTOR TRANSACTIONS
# -----------------------------

# Convert date column
tx["transaction_date"] = pd.to_datetime(
    tx["transaction_date"],
    errors="coerce"
)

# Standardize transaction types
tx["transaction_type"] = (
    tx["transaction_type"]
    .str.strip()
    .str.upper()
)

tx["transaction_type"] = tx["transaction_type"].replace({
    "SIP": "SIP",
    "LUMPSUM": "Lumpsum",
    "REDEMPTION": "Redemption"
})

# Convert amount to numeric
tx["amount_inr"] = pd.to_numeric(
    tx["amount_inr"],
    errors="coerce"
)

# Remove invalid amount rows
invalid_amounts = tx[tx["amount_inr"] <= 0]

print("\nInvalid Amount Rows:")
print(len(invalid_amounts))

tx = tx[tx["amount_inr"] > 0]

# Validate KYC Status
tx["kyc_status"] = (
    tx["kyc_status"]
    .str.strip()
    .str.upper()
)

valid_kyc = ["VERIFIED", "PENDING", "REJECTED"]

invalid_kyc = tx[
    ~tx["kyc_status"].isin(valid_kyc)
]

print("\nInvalid KYC Rows:")
print(len(invalid_kyc))

# Save cleaned file
tx.to_csv(
    PROCESSED / "clean_investor_transactions.csv",
    index=False
)

print("\nInvestor Transactions Cleaned Successfully")
print("\n" + "=" * 50)
print("SCHEME PERFORMANCE")
print("=" * 50)

perf = pd.read_csv(
    RAW / "07_scheme_performance.csv"
)

print("\nShape:")
print(perf.shape)

print("\nColumns:")
print(perf.columns)
# -----------------------------------
# CLEAN SCHEME PERFORMANCE
# -----------------------------------

# Convert return columns to numeric

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# Convert expense ratio

perf["expense_ratio_pct"] = pd.to_numeric(
    perf["expense_ratio_pct"],
    errors="coerce"
)

# Check invalid return values

for col in return_cols:

    invalid = perf[
        perf[col].isna()
    ]

    print(f"\nInvalid {col}:")
    print(len(invalid))

# Flag return anomalies

for col in return_cols:

    anomalies = perf[
        (perf[col] < -100) |
        (perf[col] > 100)
    ]

    print(f"\nAnomalies in {col}:")
    print(len(anomalies))

# Expense ratio validation

invalid_expense = perf[
    (perf["expense_ratio_pct"] < 0.1) |
    (perf["expense_ratio_pct"] > 2.5)
]

print("\nInvalid Expense Ratio Rows:")
print(len(invalid_expense))

# Save cleaned file

perf.to_csv(
    PROCESSED / "clean_scheme_performance.csv",
    index=False
)

print("\nScheme Performance Cleaned Successfully")