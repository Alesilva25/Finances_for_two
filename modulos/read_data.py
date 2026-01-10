# Exibe informações de receita, despesa e saldo total
def visualizar_saldo(usuarios):
    # variaveis locais de receita, despesa e saldo 
    receita_total = 0
    despesa_total = 0

    # loop para encontrar o valor em cada lista de receita 
    for i in range(len(usuarios[0]['receita'])):
        receita_usuario = usuarios[0]['receita'][i]['valor']
        receita_total += receita_usuario

    # loop para encontrar o valor em cada lista de despesa 
    for i in range(len(usuarios[0]['despesa'])):
        despesa_usuario = usuarios[0]['despesa'][i]['valor']
        despesa_total += despesa_usuario
    
    saldo = receita_total - despesa_total

    print(f"Usuario: {usuarios[0]['usuario1'].capitalize()}", f"Receita: {receita_total:,}", f"Despesa: {despesa_total:,}", f"Saldo: {saldo:,}", sep='\n')