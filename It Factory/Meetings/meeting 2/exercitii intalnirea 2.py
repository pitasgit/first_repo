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
