def calcular_saldo(entrada):
    saldo = 0

    # TODO: Iterar sobre cada transação e somar ao saldo
    for item in entrada:
        saldo += item

    # TODO: Retornar o saldo formatado com duas casas decimais
    return f"Saldo: R$ {saldo:.2f} "  # Complete aqui

# Entrada de dados
entrada = [100, -50, 200]


# Chamar a função e exibir o resultado
resultado = calcular_saldo(entrada)
print(resultado)
