import pandas as pd
from datetime import date

# conhecendo o nosso dataframe
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?dataInicial=27/09/2015&formato=json"
df_selic = pd.read_json(url)

# verificar duplicidade
df_selic.drop_duplicates(keep='last', inplace=True)

# criar colunas para data de extração e responsável
data_extracao = date.today()

df_selic['data_extracao'] = data_extracao
df_selic['responsavel'] = "Sergio Merces"

print(df_selic.info())
print(df_selic.head())

# extração usando filtros
# método .loc[]
print('\n\n')
print(df_selic.loc[0])
print('\n\n')
print(df_selic.loc[[0, 20, 70]])

# usando teste booleano
teste = df_selic['valor'] < 0.01
print('')
print(type(teste))