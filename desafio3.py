def contar_vogais(texto):
    contador = 0
    
    # TODO: Iterar sobre cada caractere e contar as vogais
    for i in texto:
        if i in "aeiou":
            contador +=1
        
    # TODO: Retornar o total de vogais encontradas
    return contador

# Entrada de dados
entrada = "programacao"

# Chamar a função e exibir o resultado
resultado = contar_vogais(entrada)  
print(resultado)
