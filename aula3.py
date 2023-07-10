valor = float(input("Qual o valor da hora trabalhada? "))
hora = float(input("Quantas horas foram trabalhadas? "))

salario = (valor * hora)

if (hora >= 100):
    salario = (salario + 500)

print (f"Você recebeu R$ {salario} por ter trabalhado {hora} horas neste mês.")