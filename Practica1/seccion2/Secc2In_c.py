import random

lista = []

for _ in range(20):
    x = random.randint(0,15)
    lista.append(x)

print(lista)

# inciso c) [m:]

lista_c = lista[5:]
print(f'lista_c: {lista_c}')

# Forma analoga

inicio, final = 5, len(lista)  

lista_c_equivalente = []
for i in range(inicio, final):
    lista_c_equivalente.append(lista[i])

print(f'lista_c_equivalente: {lista_c_equivalente}')