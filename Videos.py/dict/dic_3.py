import random 
countries = ['pan', 'mex', 'ecua', 'col']

popularyti_v2 = {contrys: random.randint(1000, 8938) for contrys in countries}
print(popularyti_v2)

result = {contrys: pupulation for (contrys, pupulation) in popularyti_v2.items() if pupulation > 5000}
print(result)


texto = 'quisera que fueras el amor de mi vida  compai'

unique = {c: texto.count(c) for c in texto if c in 'aeiou'}
print(unique)
#este para contar cuantas veces existe la misma vocal en el texto