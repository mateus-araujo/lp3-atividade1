'''

@author: Mateus Araujo

'''

dict = {
    "inconstitucional": "não constitucional",
    "violino":"instrumento musical",
    "alcateia":"conjunto de lobos"
}

print(dict.items())
print(dict.keys())
print(dict.values())


entrada = str(input("\nEntrada: \nR- "))
if entrada == "":
    quit()

alter_e = str()
for item in dict.keys():
    if item in entrada and alter_e == "":
        alter_e = entrada.replace(item, dict.get(item))
    elif alter_e:
        alter_e = alter_e.replace(item, dict.get(item))

entrada = alter_e
print("Saída: ", str(entrada))