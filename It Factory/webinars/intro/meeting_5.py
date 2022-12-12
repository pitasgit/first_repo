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
# string_masini = input('Scrie o lista de masini despartite cu ,:')
# print(string_masini)
# lista_masini = string_masini.split(',')


# def returneaza_litera(portocala, mar = 5):
#     print(mar)
#     for masina in portocala:
#         if masina == 'Tractor':
#             for indexLitera in range(len(masina)):
#                 if masina[indexLitera] == 'b':
#                     return (masina[indexLitera])
#                 elif masina[indexLitera] == 't':
#                     return (masina[indexLitera])
#
# print(returneaza_litera(lista_masini,8))

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

index = 0
while index < 5:
    list1 = [0, 1, 2, 3, 4]
    print(list1[index])
    index = index+1
