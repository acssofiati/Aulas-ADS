#03
#Leia dois valores (inteiros, reais ou caracteres)
#para as variáveis valor1 e valor2, e efetue a troca dos valores
#de forma que a valor1 passe a possuir o valor de valor2 e passe 
#a possuir o valor de valor1

valor1 = input("Digite o valor de A ")
valor2 = input("Digite o valor de B ")

aux = valor1
valor1 = valor2
valor2 = aux

print ("Os valores digitados, invertidos são:")
print (f"A = {valor1}")
print (f"B = {valor2}")