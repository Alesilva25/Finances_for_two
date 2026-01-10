# Altera os dados de nome ou valor em uma receita ou despesa
def alterar_registro(usuarios):
    op = int(input("1 - Editar receita \n2 - Editar despesa: "))
    busca_nome = input("Digite o nome do registro que procura: ")

    if op == 1:
        for i in range(len(usuarios[0]['receita'])):
            nome = usuarios[0]['receita'][i]['nome']

            if busca_nome in nome:
                usuarios[0]['receita'][i]['nome'] = input("Digite o novo nome: ").casefold()

                novo_valor = input("Digite o novo valor: ")
                novo_valor = novo_valor.replace(',', '.')
                novo_valor = float(novo_valor)

                usuarios[0]['receita'][i]['valor'] = novo_valor
    elif op == 2:
        for i in range(len(usuarios[0]['despesa'])):
            nome = usuarios[0]['despesa'][i]['nome']

            if busca_nome in nome:
                usuarios[0]['despesa'][i]['nome'] = input("Digite o novo nome: ").casefold()

                novo_valor = input("Digite o novo valor: ")
                novo_valor = novo_valor.replace(',', '.')
                novo_valor = float(novo_valor)

                usuarios[0]['despesa'][i]['valor'] = novo_valor