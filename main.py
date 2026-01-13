import pandas as pd
from pathlib import Path
import modulos.create_entry as create #FUNCIONA
import modulos.read_data as read #FUNCIONA
import modulos.update_entry as update
import modulos.delete_entry as delete


# exibe tabela
novo_df = pd.read_excel('planilha_organizador_financeiro.xlsx')
print(novo_df)

read.saldo()
create.receita()

novo_df = pd.read_excel('planilha_organizador_financeiro.xlsx')
print(novo_df)