# Efetue o cálculo da quantidade de litros de combustível 
# gasta em uma viagem, utilizando um automóvel que faz 12 Km 
# por litro. Para obter o cálculo, o usuário deve fornecer o 
# tempo gasto (TEMPO) e a velocidade média (VELOCIDADE) 
# durante a viagem. Desta forma, será possível obter a 
# distância percorrida com a fórmula 
# DISTANCIA = TEMPO * VELOCIDADE. 
# Possuindo o valor da distância, basta calcular a quantidade 
# de litros de combustível utilizada na viagem com a fórmula 
# LITROS_USADOS = DISTANCIA / 12. Ao final, o programa deve 
# apresentar os valores da velocidade média (VELOCIDADE), 
# tempo gasto na viagem (TEMPO), a distância percorrida 
# (DISTANCIA) e a quantidade de litros (LITROS_USADOS) 
# utilizada na viagem.

tempo = float(input("Digite a distância percorrida (em km): "))
veloc = float(input("Digite o tempo gasto no trajeto (em minutos) "))

dist = tempo * veloc
#cons = round((dist / 12),2)
cons = dist / 12

print (f"Nessa viagem,percorremos a distância de {dist:.2f} quilômetros a {veloc:.2f}km/h,  em {tempo:.2f} minutos. \n Consumindo {cons:.2f} litros de gasolina")


#a função round limita o número de casas decimais, utilizando virgula + número
#de casas desejadas entre parênteses, com a fórmula dentro, também em parênteses

#1f e 2f substituem a função round, limitando as casas decimais dos valores float direto na string