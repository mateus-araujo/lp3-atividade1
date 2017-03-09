'''
Created on 9 de mar de 2017

@author: Mateus Araujo
'''
numero = int(input("Inteiro: \nR- "))
print(bin(numero))
n = int(input("Valor para N: \nR- "))

result = numero >> n

print(bin(result))