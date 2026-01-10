# Cria função com loop para registro de despesa
def adicionar_despesa(usuarios):
    while True:
        op = int(input("1 - Adicionar Despesa \n0 - Cancelar Operação: \n"))

        if op == 1:
            try:
                nome_despesa = input("Nome da despesa: ")
                valor = input("Valor da despesa: ")
                # trata o valor para substutir virgula por ponto e tirar os espaços
                valor = valor.replace(',', '.')
                # transforma valor de string em float
                valor = float(valor)

                # dicionario com nome e valor da despesa
                despesa = {
                    "nome": nome_despesa,
                    "valor": valor
                }

                # adiciona o dicionário na chave de despesa em usuario
                usuarios[0]['despesa'].append(despesa)
            # exibe o erro
            except ValueError as e:
                print("Erro: {e}. Tente Novamente!")
        # interrompe loop
        elif op == 0:
            break
        # mensagem de alerta
        else:
            print("Opção inválida! Tente novamente!")