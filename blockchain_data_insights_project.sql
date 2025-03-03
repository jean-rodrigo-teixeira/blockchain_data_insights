SELECT
    CAST(block_timestamp AS DATE) AS transaction_date,
    COUNT(tx_hash) AS total_transactions,
    SUM(value) AS total_value_transacted,
    AVG(tx_fee) AS average_tx_fee,
    COUNT(CASE WHEN gas_used > 0 THEN tx_hash END) AS transactions_with_gas,
    SUM(gas_used * gas_price) AS total_gas_spent,
    (COUNT(CASE WHEN tx_succeeded = TRUE THEN tx_hash END) / COUNT(tx_hash)) * 100 AS success_rate,
    COUNT(CASE WHEN tx_type = 2 THEN tx_hash END) AS eip_1559_transactions,
    COUNT(CASE WHEN tx_type = 0 THEN tx_hash END) AS legacy_transactions,
    MAX(gas_price) AS max_gas_price,
    MIN(gas_price) AS min_gas_price
FROM
    ethereum.core.fact_transactions
GROUP BY
    CAST(block_timestamp AS DATE)
ORDER BY
    transaction_date;