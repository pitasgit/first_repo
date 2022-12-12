# lista_numere = [1, 2, 3, 56, 86]
# print(type(lista_numere))
# lista_numere[2] = 75
# print(lista_numere)
# var_str = "abc"
# noua_lista = lista_numere + list(var_str)
# print(noua_lista)

# ----------------------------------------------------------------------------------------------------------------------
lista_lista = [43, 21, [65, 23, (1, 2, 3)]]

print(lista_lista)
print(lista_lista[2])
print(lista_lista[2][1])

print(type(lista_lista[2][2][0]))

# --------------------------------------------------------------------------------------------------------------------

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict.keys())
# print(thisdict.get("brand"))

# json_dict = {
#     "1": {
#         "title": "example glossary",
# 		"2": {
#             "title": "S",
# 			"3": {
#                 "4": {
#                     "ID": "SGML",
# 					"SortAs": "SGML",
# 					"GlossTerm": "Standard Generalized Markup Language",
# 					"Acronym": "SGML",
# 					"Abbrev": "ISO 8879:1986",
# 					"GlossDef": {
#                         "para": "A meta-markup language, used to create markup languages such as DocBook.",
# 						"GlossSeeAlso": ["GML", "XML"]
#                     },
# 					"GlossSee": "markup"
#                 }
#             }
#         }
#     }
# }
#
# print(json_dict.get("1").get("2").get("3").get("4").get("ID"))
# print(json_dict.pop("ID"))

# ---------------------------------------------------------------------------------------------------------------------
# a = {1, 56, 43, 43, 76, 3, 90, 56, 23}
# print(a)
# print(a)
# print(a)
# print(a)
# --------------------------------------------------------------------------------------------------------------------

# a = (1, 56, 43, 43, 76, 3, 90, 56, 23)
# print(a)
# print(a[2])
# print(a[3])
#
# x = (765, 452) #stie deja ca este tuplu datorita parantezelor rotunde si a virgulei
# b = ()
# c = b.__add__(x)
# print(c)
# print(a.__add__(x))
# print(a + x)
# a = a+x
# print(a)
#
# lista1 = [1, 2, 3, 4]
# lista1.reverse()
# print(lista1)
# print(a.__reversed__(a))

# ctrl + alt + L rearanjeaza codul

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "old_year": 1964,
#     "year": {
#         "year": 2020
#     }
# }
# key_lev = "ionica"
# value = 2
# dict_1 = {}
# dict_1[key_lev] = value
# # dict_1["ionica"] = 2  # am adaugat key si valoare in dictionar
# print(dict_1)

# Python3 code to demonstrate working of
# Getting first key in dictionary
# Using keys() + list()

# initializing dictionary de pe internet
# test_dict = {'Gfg': 1, 'is': 2, 'best': 3}
#
# # printing original dictionary
# print("The original dictionary is : " + str(test_dict))
#
# # Using keys() + list()
# # Getting first key in dictionary
# res = list(test_dict.keys())[0]
#
# # printing initial key
# print("The first key of dictionary is : " + str(res))

