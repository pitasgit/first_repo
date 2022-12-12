# variabila = zona din memoria unui calculator care tine date
# variabila = cutiuta in care punem valori (marca, model)

# am declarat si initializat variabila marca

marca_masina = 'Volvo'

#am declarat si initializat variabila model
model_masina = 'XC 60'

#nu putem sa punem spatiu in numele variabilei
#o variabila incepe cu litera mica
#loosely typed - nu trebuie sa specificam tipurile (in java, este strongly typed)

print(f'Am cumparat o masina marca: {marca_masina}')
print(f'Este modelul: {model_masina}')

#suprascriere
model_masina = 'XC60 FaceLift'

print(f'Am cumparat o masina marca: {marca_masina}')
print(f'Este modelul: {model_masina}')

# (f'') uneste o variabila de un string


nume = 'Ungureanu'
prenume = 'Petre'
varsta = 34
#print (prenume + ' ' +nume + varsta)
print (f'{prenume} {nume} si varsta de {varsta}')