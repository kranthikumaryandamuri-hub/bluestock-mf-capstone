# Data Dictionary

## clean_nav_history.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | string | Unique AMFI fund code |
| date | date | NAV date |
| nav | float | Net Asset Value |

---

## clean_investor_transactions.csv

| Column | Type | Description |
|----------|----------|----------|
| investor_id | string | Unique investor identifier |
| transaction_date | date | Transaction date |
| amfi_code | string | Fund AMFI code |
| transaction_type | string | SIP/Lumpsum/Redemption |
| amount_inr | float | Transaction amount |
| state | string | Investor state |
| city | string | Investor city |
| city_tier | string | Tier classification |
| age_group | string | Investor age group |
| gender | string | Gender |
| annual_income_lakh | float | Annual income |
| payment_mode | string | Payment mode |
| kyc_status | string | KYC verification status |

---

## clean_scheme_performance.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | string | AMFI fund code |
| scheme_name | string | Mutual fund name |
| category | string | Fund category |
| return_1yr_pct | float | 1-year return |
| return_3yr_pct | float | 3-year return |
| return_5yr_pct | float | 5-year return |
| sharpe_ratio | float | Risk-adjusted return |
| expense_ratio_pct | float | Expense ratio |
| aum_crore | float | Assets Under Management |