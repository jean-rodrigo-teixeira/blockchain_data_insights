from flipside import Flipside
import pandas as pd
import os

# Inicialize o Flipside com a sua chave API e URL da API
flipside = Flipside("bee16fe2-eada-494f-b5a6-9589cf47ad9d", "https://api-v2.flipsidecrypto.xyz")

sql = """
SELECT 
    SUM(value) AS total_transaction_value
FROM ETHEREUM.core.fact_transactions
WHERE tx_succeeded = TRUE;
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
    file_path = os.path.join(blockchain_data_path, "transaction_value.csv")
    
    # Exportando o DataFrame para CSV
    df.to_csv(file_path, index=False)
    
    print(f"Arquivo CSV salvo em: {file_path}")
else:
    print("A variável de ambiente 'blockchain_data_path' não está definida.")
