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

