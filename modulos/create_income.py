# Crialoop para registro de receita
def adicionar_receita(usuarios):
    while True:
        op = int(input("1 - Adicionar Receita \n0 - Cancelar Operação: \n"))

        if op == 1:
            try:
                nome_receita = input("Nome da receita: ")
                valor = input("Valor da receita: ")
                # trata o valor para substutir virgula por ponto e tirar os espaços
                valor = valor.replace(',', '.')
                # transforma valor de string em float
                valor = float(valor)

                # dicionario com nome e valor da receita
                receita = {
                    "nome": nome_receita,
                    "valor": valor
                }

                # adiciona o dicionário na chave de receita em usuario
                usuarios[0]['receita'].append(receita)
            # exibe o erro
            except ValueError as e:
                print("Erro: {e}. Tente Novamente!")
        # interrompe loop
        elif op == 0:
            break
        # mensagem de alerta
        else:
            print("Opção inválida! Tente novamente!")