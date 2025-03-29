def calcular_produto(numeros):
    produto = 1

    # TODO: Iterar sobre cada número e multiplicar pelo produto acumulado
    for n in numeros:
        produto = produto * n
    # TODO: Retornar o produto final
    return produto

# Entrada de dados
entrada = [2, 3, 4]

# Chamar a função e exibir o resultado
resultado = calcular_produto(entrada)  
print(resultado)
