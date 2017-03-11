'''

@author: Mateus Araujo

'''

import string

entrada =  int(input("Inteiro: \nR- "))
print("Binário Gerado:", bin(entrada))
n = int(input("Valor de N: \nR- "))

result = entrada >> n
print(bin(result))
result = bin(result)

a = True
while a:
    alt = str(input("\nAlteração de tamanho N: \nR- "))

    x1 = True
    x2 = True

    if len(alt) != n:
        x1 = False

    for char in alt:
        if char != "0" and char != "1":
            x2 = False

    if x1 == False or x2 == False:
        print("\nAlteração inválida!")
        if x1 == False:
            print("Tamanho de alteração diferente de {}".format(n))
        if x2 == False:
            print("Somente 0's e 1's")

    if x1 and x2:
        a = False

result += alt
print("Resultado:", result)