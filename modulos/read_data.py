import pandas as pd

def saldo():
    tabela = 'planilha_organizador_financeiro.xlsx'

    consulta_tabela = pd.read_excel(tabela)
    tabela = consulta_tabela[consulta_tabela['usuario'] == 'alexandro']

    usuario_alexandro = tabela['usuario'][1]
    # variaveis locais de receita, despesa e saldo 
    receita_total = int(tabela['receita'].sum())
    despesa_total = int(tabela['despesa'].sum())
    saldo = receita_total - despesa_total

    print(f"Usuario: {usuario_alexandro.capitalize()}", f"Receita: {receita_total:,}", f"Despesa: {despesa_total:,}", f"Saldo: {saldo:,}", sep='\n')