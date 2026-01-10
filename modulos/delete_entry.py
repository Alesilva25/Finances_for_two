# Exclui entradas em receitas ou despesas
def excluir_registro(usuarios):
    op = int(input("1 - Excluir receita \n2 - Excluir despesa: "))
    valor_procurado = input("Digite o nome que procura: ").casefold()

    if op == 1:
        for item in usuarios[0]['receita']:
            if item.get('nome') == valor_procurado:
                usuarios[0]['receita'].remove(item)
                break
    elif op == 2:
        for item in usuarios[0]['despesa']:
            if item.get('nome') == valor_procurado:
                usuarios[0]['despesa'].remove(item)
                break