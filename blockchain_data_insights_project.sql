SELECT  
    CAST(block_timestamp AS DATE) AS transaction_date,  

    -- Total daily transactions  
    COUNT(tx_hash) AS total_transactions,  

    -- Successful transactions per day  
    COUNT(CASE WHEN tx_succeeded = TRUE THEN tx_hash END) AS successful_transactions,  

    -- Total value transacted (ETH) - Only successful transactions  
    SUM(CASE WHEN tx_succeeded = TRUE THEN value END) AS total_value,  

    -- EIP-4844 transactions  
    COUNT(CASE WHEN tx_type = 3 THEN tx_hash END) AS eip_4844_transactions,

    -- EIP-1559 transactions  
    COUNT(CASE WHEN tx_type = 2 THEN tx_hash END) AS eip_1559_transactions,  

    -- EIP-2930 transactions  
    COUNT(CASE WHEN tx_type = 1 THEN tx_hash END) AS eip_2930_transactions,  

    -- Legacy transactions  
    COUNT(CASE WHEN tx_type = 0 THEN tx_hash END) AS legacy_transactions

FROM ethereum.core.fact_transactions  
GROUP BY CAST(block_timestamp AS DATE) 
ORDER BY transaction_date;