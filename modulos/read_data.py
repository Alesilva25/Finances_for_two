import pandas as pd

def saldo(arquivo):
    consulta_arquivo = pd.read_csv(arquivo)
    arquivo = consulta_arquivo[consulta_arquivo['usuario'] == 'alexandro']

    usuario_alexandro = arquivo['usuario'].loc[0]
    # variaveis locais de receita, despesa e saldo 
    receita_total = float(arquivo['receita'].sum())
    despesa_total = float(arquivo['despesa'].sum())
    saldo = receita_total - despesa_total

    print(f"Usuario: {usuario_alexandro.capitalize()}", f"Receita: {receita_total:,}", f"Despesa: {despesa_total:,}", f"Saldo: {saldo:,} \n", sep='\n')

def tabela(arquivo):
    novo_df = pd.read_csv(arquivo)
    novo_df = pd.DataFrame(novo_df)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    return novo_df