from flipside import Flipside
import pandas as pd
import os

# Inicialize o Flipside com a sua chave API e URL da API
flipside = Flipside("bee16fe2-eada-494f-b5a6-9589cf47ad9d", "https://api-v2.flipsidecrypto.xyz")

sql = """
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
"""

# Execute a consulta na Flipside
query_result_set = flipside.query(sql)

# Extraindo os dados corretamente
records = query_result_set.records  # Lista de resultados
columns = query_result_set.columns  # Lista de colunas correta

# Criando um DataFrame
df = pd.DataFrame(records, columns=columns)

# Pegando o caminho da variável de ambiente 'blockchain_data_path'
blockchain_data_path = os.getenv("blockchain_data_path")

# Verificando se a variável de ambiente existe
if blockchain_data_path:
    # Caminho completo para salvar o arquivo CSV
    file_path = os.path.join(blockchain_data_path, "blockchain_data_insights_project.csv")
    
    # Exportando o DataFrame para CSV
    df.to_csv(file_path, index=False)
    
    print(f"Arquivo CSV salvo em: {file_path}")
else:
    print("A variável de ambiente 'blockchain_data_path' não está definida.")
