# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
#

# 2. Verifică și afișează dacă x este număr natural sau nu.
x = 11
if x >= 0 and type(x) == int:
    print('numarul x este numar natural')
else:
    print('numarul x NU este natural')

# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
if x > 0:
    print('x este pozitiv')
elif x < 0:
    print('x este negativ')
else:
    print('x este neutru')

# 4. Verifică și afișează dacă x este între -2 și 13.
if -2 < x < 13:
    print('numarul se afla intre -2 si 13')
else:
    print('numarul NU se afla intre -2 si 13')

# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
y = 11
if x-y < 5:
    print('diferenta intre x si y este mai mica de 5')
else:
    print('diferenta intre x si y NU este mai mica de 5')
# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.

if not 5 < x < 27:
    print('x NU se afla intre 5 si 27')
else:
    print('x se afla intre 5 si 57')
# 7. x și y (int) Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare

if int(x) == int(y):
    print('x si y sunt egale')
elif int(x) > int(y):
    print('x este mai mare')
else:
    print('y este mai mare')

# 8. X, y, z - laturile unui triunghi. Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
z = 6
if x == y == z:
    print('triunghiul este echilateral')
elif x == y and x >= z and y >= z:
    print('triunghiul este isoscel')
else:
    print('triunghiul este oarecare')

# Citește o literă de la tastatură. Verifică și afișează dacă este vocală sau nu
Vocala =