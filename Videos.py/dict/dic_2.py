'''
dic = {}
for i in range(1,11):
    dic[i] = i * 2

#print(dic) 

dic_v2 = {i: i*2 for i in range(1,5) }
print(dic_v2)
#esta es una manera mas corta de hacer la secuencia en bucle con diccionarios
'''

'''
import random 
countries = ['pan', 'mex', 'ecua', 'col']
popularyti = {}
for contrys in countries:
    popularyti[contrys] = random.randint(1000, 8938)

#print(popularyti)

popularyti_v2 = {contrys: random.randint(1000, 8938) for contrys in countries}
print(popularyti_v2)
'''

name = ['alma', 'slade', 'fer', 'ana']
edades = [12, 43, 19, 20]

print(list(zip(name, edades)))
#une listas con zip 
new_dic = {name: edades for(name, edades) in zip(name, edades)}
print(new_dic)
#crea un diccionario con zip de manera sencilla

#new_dic = {name[i]: edades[i] for i in range(len(name))}

