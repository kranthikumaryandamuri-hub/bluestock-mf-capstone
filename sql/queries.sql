-- 1. Top 5 Funds by AUM

SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-------------------------------------------------

-- 2. Average NAV

SELECT
    AVG(nav) AS average_nav
FROM fact_nav;

-------------------------------------------------

-- 3. Monthly Average NAV

SELECT
    substr(nav_date,1,7) AS month,
    AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-------------------------------------------------

-- 4. Transaction Count by State

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-------------------------------------------------

-- 5. Funds with Expense Ratio < 1%

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-------------------------------------------------

-- 6. Top 5 Funds by 1-Year Return

SELECT
    scheme_name,
    return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-------------------------------------------------

-- 7. Top 5 Funds by 5-Year Return

SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-------------------------------------------------

-- 8. Average Transaction Amount by State

SELECT
    state,
    AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY state
ORDER BY avg_amount DESC;

-------------------------------------------------

-- 9. Highest Sharpe Ratio Funds

SELECT
    scheme_name,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-------------------------------------------------

-- 10. Category-wise Average Returns

SELECT
    category,
    AVG(return_1yr_pct) AS avg_return_1yr
FROM fact_performance
GROUP BY category
ORDER BY avg_return_1yr DESC;