# Elabore um programa que leia quatro valores inteiros 
# (variáveis A, B, C e D). Ao final, o programa deve 
# apresentar o resultado da multiplicação/produto (variável P) do 
# primeiro com o terceiro valor, e o resultado da 
# soma (variável S) do egsundo com o quarto valor.

a = int(input("Defina o valor de A "))
b = int(input("Defina o valor de B "))
c = int(input("Defina o valor de C "))
d = int(input("Defina o valor de D "))       

p = a * c
s = b + d

print (f"O resultado da multiplicação de A e C é = {p}")
print (f"O resultado da soma de B e D é {s}.")