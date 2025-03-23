num1 = input("Digite o primeiro Número: ")
num2 = input("Digite o segundo Número: ")

num1 = float(num1){{num1}:{ ,.2f}.format(num1)
num2 = float(num2){{num2}:{ ,.2f}.format(num2)

operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
else:
    print("Erro: Operação invalida. Tente Novamente.")
   

print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")