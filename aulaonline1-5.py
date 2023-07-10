#Elabore um programa que efetue a leitura de três valores (A, B e C)
#e apresente como resultado final o quadrado da soma dos três valores lidos

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

res = a + b + c
res = res * res

print (f"O resultado da soma de A, B e C ao quadrado é {res:.2f}")