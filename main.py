import pandas as pd
from pathlib import Path
import modulos.create_entry as create 
import modulos.read_data as read
import modulos.update_entry as update
import modulos.delete_entry as delete

arquivo = '../Finances_for_two/planilha_organizador_financeiro.csv'

read.saldo(arquivo)

print(read.tabela(arquivo))