'''

@author: Mateus Araujo

'''

salario = float(input("Salario? \nR- "))
imposto = input("Imposto em % (ex: 27.5)? \nR- ")
if imposto:
    imposto = float(imposto)
else:
    imposto = 27.5

print("Salário real {}".format(salario - (salario * imposto * 0.01)))