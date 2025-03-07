SELECT  
    CAST(block_timestamp AS DATE) AS transaction_date,  

    -- Total daily transactions  
    COUNT(tx_hash) AS total_transactions,  

    -- Successful transactions per day  
    COUNT(CASE WHEN tx_succeeded = TRUE THEN tx_hash END) AS successful_transactions,  

    -- Total value transacted (ETH) - Only successful transactions  
    SUM(CASE WHEN tx_succeeded = TRUE THEN value END) AS total_value_transacted,  

    -- Average transaction fee (ETH) - Only successful transactions  
    AVG(CASE WHEN tx_succeeded = TRUE THEN tx_fee END) AS average_tx_fee,  

    -- Transactions with gas usage  
    COUNT(CASE WHEN gas_used > 0 AND tx_succeeded = TRUE THEN tx_hash END) AS transactions_with_gas,  

    -- Total gas spent (ETH) - Only successful transactions  
    SUM(CASE WHEN tx_succeeded = TRUE THEN gas_used * gas_price END) AS total_gas_spent,  

    -- Transaction success rate (%)  
    (COUNT(CASE WHEN tx_succeeded = TRUE THEN tx_hash END) * 100.0 / COUNT(tx_hash)) AS success_rate,  

    -- EIP-1559 transactions  
    COUNT(CASE WHEN tx_type = 2 THEN tx_hash END) AS eip_1559_transactions,  

    -- Legacy transactions  
    COUNT(CASE WHEN tx_type = 0 THEN tx_hash END) AS legacy_transactions,  

    -- Maximum and minimum gas price (Only successful transactions)  
    MAX(CASE WHEN tx_succeeded = TRUE THEN gas_price END) AS max_gas_price,  
    MIN(CASE WHEN tx_succeeded = TRUE THEN gas_price END) AS min_gas_price  

FROM ethereum.core.fact_transactions  
GROUP BY CAST(block_timestamp AS DATE)  
ORDER BY transaction_date;