#10
#Calcule e apresente o valor do volume de uma lata de óleo, utilizando a
#fórmula: volume = π * raio ** 2 * altura. Considere o valor de π como 3.1415.

raio = float(input("Declare o raio da lata: "))
altura = float(input("Declare a altura da lata: "))

volume = (3.1415 * raio ** 2 * altura)

print (f"O volume da lata é {volume:.2f}")