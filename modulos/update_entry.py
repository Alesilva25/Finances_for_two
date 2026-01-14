import pandas as pd

# Altera os dados de nome ou valor em uma receita ou despesa
def alterar_registro(arquivo):
    df = pd.read_csv(arquivo)
    valor_procurado = input("Digite o nome que deseja atualizar: ").casefold()

    # retorna linha do valor procurado
    filtro = df[df['nome'].str.casefold() == valor_procurado]

    i = int(filtro.index[0])

    if int(filtro['receita'].iloc[0]) > 0:
        usuario = input("Nome do usuário: ")
        item = input("Nome da receita: ")
        valor_receita = int(input("Digite o valor da receita: "))
        valor_despesa = 0

        df.loc[i, ['usuario', 'nome', 'receita', 'despesa']] = [usuario, item, valor_receita, valor_despesa]

    elif int(filtro['despesa'].iloc[0]) > 0:
        usuario = input("Nome do usuário: ")
        item = input("Nome da despesa: ")
        valor_receita = 0
        valor_despesa = int(input("Digite o valor da despesa: "))

        df.loc[i, ['usuario', 'nome', 'receita', 'despesa']] = [usuario, item, valor_receita, valor_despesa]

    df.to_csv(arquivo, index=False)