import random

lista = []

for _ in range(20):
    x = random.randint(0,15)
    lista.append(x)

print(lista)

# inciso d) [:n]

lista_d = lista[:10]
print(f'lista_d: {lista_d}')

# Forma analoga

from itertools import islice

lista_d_equivalente = list(islice(lista, None, 10))

print(f'lista_d_equivalente: {lista_d_equivalente}')

'''

Syntax:

islice(iterable, start, stop, step)
de: https://www.geeksforgeeks.org/python-itertools-islice/

'''