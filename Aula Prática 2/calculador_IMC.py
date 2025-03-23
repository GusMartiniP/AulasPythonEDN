#Código para calcular IMC usando valores do tipo float. Retorna valor do IMC como tipo float limitado à um digito após casa decimal.

peso = float(input("Insira seu peso em KG: ")) #input para variável peso, tipo float
altura =float(input("Insira a altura em metros: ")) #input para variável ano, tipo float

imc = peso / (altura ** 2) #Cálculo matemático entre variáveis para receber o valor do IMC 

if imc <18.5: #Criação de condição if-elif-else para classificar IMC de acordo com valor obtido.
    print(f"seu IMC é de {imc:.1f}. Está abaixo do peso, valor menor que o ideal.") # Trás classificação e valor do IMC limitado a um digito após casa decimal, usando ":.1f" dentro da chamada da variável.
elif 18.5 <= imc < 24.9: #Condição elif para resultados diferentes pedidos pelo if
     print(f"seu IMC é de {imc:.1f}.Está com peso normal, valor ideal.")  #Mesma coisa que o primeiro print, outra condição.
elif 25 <= imc < 29.9: # Outracondição elif para resultados diferentes pedidos pelo if ou o primeiro elif
     print(f"seu IMC é de {imc:.1f}.Está com sobrepeso. Valor mais alto que o ideal")  #Mais um print de acordo com as condições.
else: #Condição final caso o valor não seja o pedido por nenhuma das outras três condições declaradas
     print(f"seu IMC é de {imc:.1f}.Está com obesidade. Valor muito acima do normal")  #print caso a condição else seja cumprida.