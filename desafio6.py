def contar_ocorrencias(palavras):
    contagem = {}

    # TODO: Percorrer a lista e contar quantas vezes cada palavra aparece
    for palavra in palavras:  # Corrigido: iterar sobre as palavras diretamente
        if palavra in contagem:
            contagem[palavra] += 1  # Corrigido: incrementar a contagem existente
        else:
            contagem[palavra] = 1   # Corrigido: inicializar a contagem para 1

    # TODO: Retornar o dicionário com a contagem
    return contagem

# Entrada de dados
entrada = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

# Chamar a função e exibir o resultado
resultado = contar_ocorrencias(entrada)
print(resultado)
