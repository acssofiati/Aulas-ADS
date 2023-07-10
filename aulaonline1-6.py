#06
#Elabore um programa que efetue a leitura de três valores (A, B e C)
#e apresente como resultado final a soma dos quadrados dos três valores lidos.a = float(input("Digite o valor de A: "))

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

a = a * a
b = b * b
c = c * c

res = a + b + c


print (f"O resultado da soma dos valores ao quadrado de A, B e C  {res:.2f}")