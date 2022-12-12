masina = 1
print(masina)

casa = 'frumoasa'
print(casa[1])
print(casa[1:])

prop = 'suntem la cursu40'
print(len(prop))
n = prop[15:17]
print(type(n))
n = int(n)

zero_patru = prop[:10:-1]
print(zero_patru[::-1])
print(prop[:10:-1][::-1])

masina = input('Te rog introdu textul: ')
print(masina)

casa = 25.4
casa_int = int(casa.__round__())
print(casa_int)

assert type(int(casa)) == type(casa_int)

variabila_false = True
assert variabila_false

ana_are_mere = 'ana are mere'
variabila2 = (ana_are_mere.upper())
print(variabila2)
print(len(variabila2))
print(variabila2[0:len(variabila2) - 2] + ana_are_mere[10:len(ana_are_mere)])
print(variabila2[:-2] + ana_are_mere[10:] + ' aici printez')
print('--------intalnirea 1 a luat sfarsit')
a = 5
print(a)
a += 3 + a
a = a + 3 + a
print(a)
if a == 12:
    print('am ajuns aici')
elif a == 29:
    print('Aici e 29')
else:
    print('Am ajuns in else')

qwer = 'taste'
if qwer.__contains__('as'):
    qwer += '123'
    print('Exista a si e')
    print(qwer[5])
    print(type(qwer[5]))
    if int(qwer[5]) == 1:
        print('Este int 1')

variabila = 40
if variabila in range(30, 50):
    print('se afla')
else:
    print('nu se afla')
numar = str(variabila) + ' ani'
print(numar)
if numar.__contains__(' '):
    print('are spatiu')
if numar[2] == ' ':
    print('corect')
if numar.find(' '):
    print('corect')

pret = 678
if pret >= 678:
    elev = 'Ionel a luat nota 6'
    # nota = len(elev[::-1])
    nota = int(elev[len(elev) - 1:len(elev):1])
    # print(a[:len(a) - 2:-1])
    print(nota)
    print(type(nota))
    nota = float(nota)
    if nota >= 4.5:
        print('ai trecut')
print("-----intalnirea 2 a luat sfarsit -------")

lista_numere = [1, 2, 3, 56, 86]
print(type(lista_numere))
lista_numere[2] = 75
print(lista_numere)
var_str = "abc"
noua_lista = lista_numere + list(var_str)
print(noua_lista)

# ----------------------------------------------------------------------------------------------------------------------
lista_lista = [43, 21, [65, 23, (1, 2, 3)]]

print(lista_lista)
print(lista_lista[2])
print(lista_lista[2][1])

print(type(lista_lista[2][2][0]))

# --------------------------------------------------------------------------------------------------------------------

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict.keys())
print(thisdict.get("brand"))

json_dict = {
    "1": {
        "title": "example glossary",
        "2": {
            "title": "S",
            "3": {
                "4": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": ["GML", "XML"]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
}

print(json_dict.get("1").get("2").get("3").get("4").get("ID"))
print(json_dict.pop("ID"))

print("-----------------------------------------------------------------------------------------------------------")
a = {1, 56, 43, 43, 76, 3, 90, 56, 23}
print(a)
print(a)
print(a)
print(a)
print("--------------------------------------------------------------------------------------------------------------")

a = (1, 56, 43, 43, 76, 3, 90, 56, 23)
print(a)
print(a[2])
print(a[3])

x = (765, 452)  # stie deja ca este tuplu datorita parantezelor rotunde si a virgulei
b = ()
c = b.__add__(x)
print(c)
print(a.__add__(x))
print(a + x)
a = a + x
print(a)

lista1 = [1, 2, 3, 4]
lista1.reverse()
print(lista1)
# print(a.__reversed__(a))

# ctrl + alt + L
# rearanjeaza
# codul

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "old_year": 1964,
    "year": {
        "year": 2020
    }
}
key_lev = "ionica"
value = 2
dict_1 = {}
dict_1[key_lev] = value
# dict_1["ionica"] = 2  # am adaugat key si valoare in dictionar
print(dict_1)
#
# Python3
# code
# to
# demonstrate
# working
# of
# Getting
# first
# key in dictionary
# Using
# key_lev(value) + list()

# initializing
# dictionary
# de
# pe
# internet
test_dict = {'Gfg': 1, 'is': 2, 'best': 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using keys() + list()
# Getting first key in dictionary
res = list(test_dict.keys())[0]

# printing initial key
print("The first key of dictionary is : " + str(res))
print("------------------intalnirea 3 a luat sfarist -----------------------------")

propozitie = "Ana are meRe"
for litera in propozitie:
    # if litera == "R" or litera == "r":
    if litera.upper() == "R":
        print(litera)
# index = 1
# while 23 >= index:
#     index += 1
#     print(index)
#     if index <= 25:
#         print("Maine este vineri")
#         if index == 25:
#             break
#     print(index)
# else:
#     print("am terminat de rulat")

# propozitie2 = "Ana are mere"
# for index in range(10):
#     if index == 5:
#         continue
#     print(propozitie2[index])
# else:
#     print("am terminat de rulat")
paine = ['paine alba', 'paine Graham', 'paine secara']
lista_cumparaturi = ['lapte', 'oua', 'apa', ['creion', 'pix', 'radiera'], paine]
for cumparatura in lista_cumparaturi:
    # print(lista_cumparaturi)  # face print ori de cate ori gaseste un produs. Aici, 4
    if type(cumparatura) == list:
        cumparatura_clona = cumparatura
        lista_cumparaturi.remove(cumparatura)
        lista_cumparaturi.extend(cumparatura_clona)
    print(type(cumparatura))
print(lista_cumparaturi)
print("---------------------- intalnirea 4 a luat sfarsit ------------------------------")

# a = 4
# b = 2
#
# def sum(numar1,numar2):
#     numar3 = numar1+numar2
#     return numar3
# sum(a,b)
# print(sum(a,b))
# #
# def hi():
#     print("am inceput tema!")
#
# hi()
# print(sum(a,b))
# def verifica_prezenta():
#     lista = ['Ionel', 'Gicu', 'Popescu']
#     index = 0
#     for index in range(len(lista)-1):
#         print(lista[index])
#         # assert lista[index] == 'Ionel'
# verifica_prezenta()
# ------------------------------------------------
# string_masini = input('Scrie o lista de masini despartite cu ,:')
# print(string_masini)
# lista_masini = string_masini.split(',')
# print(lista_masini)
# for masina in lista_masini:
#     print(masina)
#     if masina == 'Tractor':
#         for indexLitera in range(len(masina)):
#             print(masina[indexLitera])

# Volvo,Dacia,Audi,Tractor,Testla
string_masini = input('Scrie o lista de masini despartite cu ,:')
print(string_masini)
lista_masini = string_masini.split(',')


def returneaza_litera(portocala, mar=5):
    print(mar)
    for masina in portocala:
        if masina == 'Tractor':
            for indexLitera in range(len(masina)):
                if masina[indexLitera] == 'b':
                    return (masina[indexLitera])
                elif masina[indexLitera] == 't':
                    return (masina[indexLitera])

print(returneaza_litera(lista_masini, 8))


# list1 = [0,1,2,3]
# list2 = [0,1,4,5]
# list3 = list1 + list2
# print(list(set(list3)))

# index = 0
# while index <= 5:
#     list1 = [0, 1, 2, 3, 4]
#     print(list1[index])
#     index = index+1
#     if index <= 5:
#         break

# index = 0
# while index < 5:
#     list1 = [0, 1, 2, 3, 4]
#     print(list1[index])
#     index = index+1
print("------------------------------intalnirea 5 a luat sfarist------------------------------")

