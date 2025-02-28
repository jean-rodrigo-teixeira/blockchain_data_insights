SELECT  
    DATE_TRUNC('day', block_timestamp) AS transaction_date,  
    COUNT(tx_hash) AS transaction_volume,  
    SUM(value) AS transaction_value,  
    COUNT(DISTINCT from_address) AS active_wallets  
FROM ETHEREUM.core.fact_transactions  
WHERE tx_succeeded = TRUE  
GROUP BY transaction_date  
ORDER BY transaction_date;