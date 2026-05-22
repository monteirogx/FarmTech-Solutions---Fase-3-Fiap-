import pandas as pd
import numpy as np

# 1. Criar dados simulados (Mock) perfeitos e sem margem para erros de formatação
dados = {
    'ID_SENSOR': range(100, 150), # 50 linhas de dados
    'DATA_LEITURA': pd.date_range(start='2026-05-01', periods=50).strftime('%d-%m-%Y'),
    'TEMPERATURA': np.random.randint(20, 35, 50), # Inteiros para evitar bugs decimais no Oracle
    'UMIDADE': np.random.randint(40, 85, 50),
    'NIVEL_PH': np.random.randint(5, 8, 50)
}

# 2. Transformar numa tabela (DataFrame)
df_sensores = pd.DataFrame(dados)

# 3. Exportar para um ficheiro CSV imaculado
nome_ficheiro = 'Sensores_fazenda.csv'
df_sensores.to_csv(nome_ficheiro, index=False)

print(f"✅ Ficheiro '{nome_ficheiro}' gerado com sucesso!")

files.download(nome_ficheiro)