import pandas as pd

def receita(arquivo):
    df_antigo = pd.read_csv(arquivo)

    try:
        usuario = input("Digite o nome do usuário: ")
        nome_receita = input("Nome da receita: ")
        valor = input("Valor da receita: ")
        # trata o valor para substutir virgula por ponto e tirar os espaços
        valor = valor.replace(',', '.')
        # transforma valor de string em float
        valor = float(valor)

        # dicionario com nome e valor da receita
        receita = {
            'usuario': usuario,
            "nome": nome_receita,
            "receita": valor,
            "despesa": int(0)
        }

        receita_df = pd.DataFrame([receita])

        # adiciona o dicionário na chave de receita em usuario
        df_final = pd.concat([df_antigo, receita_df], ignore_index=True)

        salva_registro = df_final.to_csv(arquivo, index=False)

        return salva_registro
    # exibe o erro
    except ValueError as e:
        print("Erro: {e}. Tente Novamente!")

# Cria loop para registro de receita
def despesa(arquivo):
    df_antigo = pd.read_csv(arquivo)
    try:
        usuario = input("Digite o nome do usuário: ")
        nome_despesa = input("Nome da despesa: ")
        valor = input("Valor da despesa: ")
        # trata o valor para substutir virgula por ponto e tirar os espaços
        valor = valor.replace(',', '.')
        # transforma valor de string em float
        valor = float(valor)

        # dicionario com nome e valor da despesa
        despesa = {
            'usuario': usuario,
            "nome": nome_despesa,
            "receita": int(0),
            "despesa": valor
        }

        despesa_df = pd.DataFrame([despesa])

        # adiciona o dicionário na chave de despesa em usuario
        df_final = pd.concat([df_antigo, despesa_df], ignore_index=True)

        salva_registro = df_final.to_csv(arquivo, index=False)

        return salva_registro
    # exibe o erro
    except ValueError as e:
        print("Erro: {e}. Tente Novamente!")