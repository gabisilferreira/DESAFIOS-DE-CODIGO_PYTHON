def calcular_media(numeros):
    # TODO: Calcular a média dos valores na lista
    soma = sum(numeros)
    media = soma/len(numeros)

    # TODO: Retornar a média formatada com duas casas decimais
    return f'{media:.2f}'

# Entrada de dados
entrada = [10, 20, 30, 40, 50]

# Chamar a função e exibir o resultado
resultado = calcular_media(entrada)  
print(resultado)
