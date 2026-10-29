def calcular(a, operacao, b):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        if b == 0:
            return "Erro: divisão por zero"
        return a / b
    else:
        return "Operação inválida"


while True:
    print("\n--- Calculadora ---")
    try:
        a = float(input("Primeiro número: "))
        operacao = input("Operação (+, -, *, /): ")
        b = float(input("Segundo número: "))
    except ValueError:
        print("Digite apenas números válidos.")
        continue

    print("Resultado:", calcular(a, operacao, b))

    de_novo = input("Calcular de novo? (s/n): ").lower()
    if de_novo != "s":
        print("Até mais!")
        break