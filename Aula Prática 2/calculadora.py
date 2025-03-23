num1 = input("Digite o primeiro Número: ")

num2 = input("Digite o segundo Número: ")

if not num1.replace('.', '', 1).isdigit() or not num2.replace('.', '', 1).isdigit():
    print("Erro: Entrada Invalida. Por favor, insira Números válidos.")
    exit()

num1 = float(num1)
num2 = float(num2)

operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 == 0:
        print("Erro: Divisão por Zero não é permitida")
        exit()
    resultado = num1 / num2
else:
    print("Erro: Operação invalida. Tente Novamente.")
    exit()

print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")