import pandas as pd
from pathlib import Path
import modulos.create_entry as create #FUNCIONA
import modulos.read_data as read #FUNCIONA
import modulos.update_entry as update
import modulos.delete_entry as delete # FUNCIONA

arquivo = 'planilha_organizador_financeiro.xlsx'

print(f"{read.tabela(arquivo)} \n")

read.saldo(arquivo)