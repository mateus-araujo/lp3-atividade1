'''

@author: Mateus Araujo

'''

entrada = -1
while entrada < 0:
    if entrada < 0:
        entrada = int(input("Digite um inteiro maior ou igual a zero: \nR- "))

x = entrada
cont = 0
print("Binário gerado: ", bin(x))
while x > 0:
    x >>= 1
    cont += 1

saida = cont

print("\n{0} => {1}" .format(entrada, saida))