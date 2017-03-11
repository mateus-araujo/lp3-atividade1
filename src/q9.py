'''

@author: Mateus Araujo

'''

nomes_proprios = ["carlos", "antonio", "paulo", "pedro", "maria", "chico", "chica"]

s1 = "Antonio comprou dois livros sobre a vida de chico"
s2 = "paulo joga muito bem, mas pedro joga melhor"
s3 = "antonio não sabe brincar, é um brutamonte..."


def capitalize_names(s, lista):
    alter_e = str()
    for item in lista:
        if item in s and alter_e == "":
            alter_e = s.replace(item, item.capitalize()) + "\n"
        elif alter_e:
            alter_e = alter_e.replace(item, item.capitalize())
    return alter_e

entrada = str(input("Entrada: \nR- "))
alter_e = capitalize_names(entrada, nomes_proprios)
print("Saída: ", alter_e)

'''
as1 = capitalize_names(s1, nomes_proprios)
as2 = capitalize_names(s2, nomes_proprios)
as3 = capitalize_names(s3, nomes_proprios)

print(s1)
print(as1)
print(s2)
print(as2)
print(s3)
print(as3)
'''