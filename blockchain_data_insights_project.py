from flipside import Flipside
import pandas as pd
import os

# Inicialize o Flipside com a sua chave API e URL da API
flipside = Flipside("bee16fe2-eada-494f-b5a6-9589cf47ad9d", "https://api-v2.flipsidecrypto.xyz")

sql = """
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
