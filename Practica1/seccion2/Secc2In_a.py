import random

lista = []

for _ in range(20):
    x = random.randint(0,15)
    lista.append(x)

print(lista)

# inciso a) [m:n]

lista_a = lista[5:10]

print(f'lista_a: {lista_a}')

# Forma analoga

from itertools import islice

lista_a_equivalente = list(islice(lista, 5, 10))

print(f'lista_a_equivalente: {lista_a_equivalente}')

'''

Syntax:

islice(iterable, start, stop, step)
de: https://www.geeksforgeeks.org/python-itertools-islice/

'''
