#13
# Elabore um programa que efetue a apresentação do valor da conversão em
# dólar de um valor lido em real. O programa deve solicitar a cotação do
# dólar e também a quantidade de reais disponível com o usuário, para que
# seja apresentado o valor em moeda americana.

real = float(input("Valor atual da cotação do Dólar em relação ao Real: "))
valor = float(input("Valor em Dólar que você irá converter para Reais: "))

dol = valor * real

print (f"Seus Dólares convertidos irão valer R${dol:.2f} Reais.")