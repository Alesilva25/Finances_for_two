import pandas as pd

# Exclui entradas em receitas ou despesas
def excluir_registro(arquivo):
    arquivo = pd.read_excel('../Finances_for_two/planilha_organizador_financeiro.xlsx')
    df = pd.DataFrame(arquivo)

    #recebe valor para procurar
    valor_procurado = input("Digite o valor que procura: ").casefold()

    # retorna index do valor procurado
    i_valor_procurado = df[df['nome'].str.casefold() == valor_procurado].index
    # exclui index
    df = df.drop(i_valor_procurado)
    # atualiza arquivo
    return df.to_excel('planilha_organizador_financeiro.xlsx', index=False)