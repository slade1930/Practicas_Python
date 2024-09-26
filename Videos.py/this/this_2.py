set_countries = {'pan', 'mex', 'canada'}
size = len(set_countries)
print(size)
# len sirve para devolver el tamaño del conjunto patra saber cuantos hay 
print(sorted(set_countries))
# sorted y sirve para ordenar en orden alfabetico
print('pan' in 
      set_countries)
print('col' in 
      set_countries)
#in sirve para verificar si el dato  esta dentro del conjunto y si lo esta es True y si no false

set_countries.add('pe')
set_countries.add('pe')
print(set_countries)
# el add sirve para añadir elementos del conjunto

set_countries.update({'ecu', 'pr', 'cub' })
print(sorted(set_countries))
#añde cualquier tipo de objetos iterables como listas o tuplas

set_countries.remove('pe')
print(set_countries)

#set_countries.remove('per')
#print(set_countries)

set_countries.discard('per')
print(set_countries)
#elimina un elemnto del conjunto aunque no exista sigue corriendo sin marcar ningun error



print(set_countries.pop())
print(set_countries)
#elige un elemento aleatorio y lo elimina 

set_countries.clear()
print(set_countries)
print(len(set_countries))
#elimina todo los elemntos que esten dentro del conjunto









