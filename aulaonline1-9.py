#09
#Leia o valor correspondente ao salário mensal (variável SM) de um
#trabalhador e também o valor do percentual de reajuste (variável PR)
#a ser atribuído. Apresente o valor do novo salário (variável NS).

sm = float(input("Digite o valor do salário mensal: "))
pr = float(input("Digite o valor do percentual de reajuste:"))

pr = (sm / 100) * pr
ns = sm + pr

print (f"O salário reajustado é de R$ {ns:.2f}")