#Código para calcular o preço total de um produto utilizando multiplicação baseado na quantia do mesmo

nome_produto = "Cadeira infantil" #var string do produto
preço_unitario = 12.40 #var float do preço unitário
quantidade = 3 #var int da quantia
preço_total = preço_unitario * quantidade #cálculo realizado para obter o preço total

#Resultado detalhado da conta feita
print(f"O produto ({nome_produto}) , tendo como preço unitário ({preço_unitario:.2f}) e calculando a multiplicação da quantiedade ({quantidade}), resulta em seu preço total de ({preço_total:.2f})" )