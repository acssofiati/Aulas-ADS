#16
# Em uma eleição sindical concorreram ao cargo de presidente três candidatos
# (A, B e C). Durante a apuração dos votos foram computados votos nulos e votos
# em branco, além dos votos válidos para cada candidato. Deve ser criado um
# programa de computador que efetue a leitura da quantidade de votos válidos para
# cada candidato, além de efetuar também a leitura da quantidade de votos nulos e
# votos em branco. Ao final o programa deve apresentar o número total de eleitores,
# considerando votos válidos, nulos e em branco; o percentual correspondente de
# votos válidos em relação à quantidade de eleitores; o percentual correspondente
# de votos válidos do candidato A em relação à quantidade de eleitores; o percentual
# correspondente de votos válidos do candidato B em relação à quantidade de
# eleitores; o percentual correspondente de votos válidos do candidato C em relação
# à quantidade de eleitores; o percentual correspondente de votos nulos em relação
# à quantidade de eleitores; e por último o percentual correspondente de votos em
# branco em relação à quantidade de eleitores.

a = int(input("Quantidade de votos que candidato A teve: "))
b = int(input("Quantidade de votos que candidato B teve: "))
c = int(input("Quantidade de votos que candidato C teve: "))
bra = int(input("Quantidade de votos em branco: "))
nul = int(input("Quantidade de votos nulos: "))

total = a + b + c + bra + nul
percent = total / 100

pa = a / percent
pb = b / percent
pc = c / percent
pbra = bra / percent
pnul = nul / percent

print (f"Candidato A:  {pa:.2f}%")
print (f"Candidato B:  {pb:.2f}%")
print (f"Candidato C:  {pc:.2f}%")
print (f"Votos em Branco:  {pbra:.2f}%")
print (f"Votos Nulos:  {pnul:.2f}%")

