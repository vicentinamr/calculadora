def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return 0

# Exemplos de uso
resultado1 = calculadora(10, 5, 1)  # Soma: 10 + 5 = 15
resultado2 = calculadora(10, 5, 2)  # Subtração: 10 - 5 = 5
resultado3 = calculadora(10, 5, 3)  # Multiplicação: 10 * 5 = 50
resultado4 = calculadora(10, 5, 4)  # Divisão: 10 / 5 = 2.0
resultado5 = calculadora(10, 5, 5)  # Operação inválida: resultado = 0

print(resultado1)  # Saída: 15
print(resultado2)  # Saída: 5
print(resultado3)  # Saída: 50
print(resultado4)  # Saída: 2.0
print(resultado5)  # Saída: 0
