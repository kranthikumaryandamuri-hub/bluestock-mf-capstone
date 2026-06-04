import pandas as pd
from sqlalchemy import create_engine

# Database connection
engine = create_engine(
    "sqlite:///../data/db/bluestock_mf.db"
)

print("Loading datasets...")

# NAV
nav = pd.read_csv(
    "../data/processed/clean_nav_history.csv"
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("fact_nav loaded:", len(nav))

# Transactions
tx = pd.read_csv(
    "../data/processed/clean_investor_transactions.csv"
)

tx.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("fact_transactions loaded:", len(tx))

# Performance
perf = pd.read_csv(
    "../data/processed/clean_scheme_performance.csv"
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("fact_performance loaded:", len(perf))

print("\nAll datasets loaded successfully")
print("\nVerifying row counts...")

print(
    pd.read_sql(
        "SELECT COUNT(*) as rows FROM fact_nav",
        engine
    )
)

print(
    pd.read_sql(
        "SELECT COUNT(*) as rows FROM fact_transactions",
        engine
    )
)

print(
    pd.read_sql(
        "SELECT COUNT(*) as rows FROM fact_performance",
        engine
    )
)