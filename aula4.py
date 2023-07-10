num = int(input("Digite um número: "))

print ("TABUADA DO {num}.")

for i in range (1, 11):

    result = num * i
    print (f"{num} X {i} = {result}")