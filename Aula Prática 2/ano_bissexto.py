#Este código tem o intuito de receber o valor de um ano como valor inteiro, e indicar se ele é bissexto com base nas condições do mesmo ocorrer

ano = int(input("Digite um ano: "))  #input para variável ano, tipo int
if (ano % 4 == 0  and ano % 100 != 0) or (ano % 400 == 0): #Condição if usando comparações de acordo com condições matemáticas para o ano bissexto ocorrer.
    print(f"{ano} é um ano bissexto.") #retorno de resultado positivo. "F" após o print e antes da variável trás o valor atribuído à ela, ao invés do nome dela.
else: #continuando condição if
     print(f"{ano}  não é um ano bissexto.") #retorno de resultado negativo.
2016