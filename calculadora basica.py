print("\ncalculate\n")

num1 = float(input("Digite o primeiro número: "))
operacao = input("Escolha a operação (+, -, *, /, random): ")
num2 = float(input("Digite o segundo número: "))

def calculate(num1, num2, operacao):
    if operacao == "+":
        return num1 + num2

    elif operacao == "-":
        return num1 - num2

    elif operacao == "*":
        return num1 * num2

    elif operacao == "/":
        return num1 / num2

    else:
        return None


resultado = calculate(num1, num2, operacao)

if resultado is None:
    print("Operação inválida")
else:
    print("Resultado:", resultado)