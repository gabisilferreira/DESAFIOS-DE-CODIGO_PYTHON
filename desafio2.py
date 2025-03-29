def somar_positivos(numeros):
    soma = 0

    # TODO: Iterar sobre cada número e somar apenas os positivos
    for item in numeros:
        if item > 0:
            soma += item
    # TODO: Retornar a soma dos números positivos
    return soma

# Entrada de dados
entrada = [10, -5, 7, -2, 8]

# Chamar a função e exibir o resultado
resultado = somar_positivos(entrada)  
print(resultado)
