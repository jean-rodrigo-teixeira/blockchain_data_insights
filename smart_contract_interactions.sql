SELECT  
    DATE_TRUNC('day', block_timestamp) AS transaction_date,  
    COUNT(tx_hash) AS smart_contract_interactions  
FROM ETHEREUM.core.fact_transactions  
WHERE to_address IS NOT NULL  
AND origin_function_signature IS NOT NULL  
AND tx_succeeded = TRUE  
GROUP BY transaction_date  
ORDER BY transaction_date;