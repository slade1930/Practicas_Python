set_a = {'col' , 'bra', 'pr'}
set_b = {'suz' , 'col'}

set_c = set_a.union(set_b)
print(set_a | set_b)
print(sorted(set_c))
#maneras para unir 

set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)
#muestra los elemntos en comun 

set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)
#dejamos solo los elemntos de a

set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)