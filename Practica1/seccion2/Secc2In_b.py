import random

lista = []

for _ in range(20):
    x = random.randint(0,15)
    lista.append(x)

print(lista)

# inciso b) [-m:n]

lista_b = lista[-5:] + lista[:10]
print(f'lista_b: {lista_b}')

# Forma analoga

inicio, final = -5, 10  

lista_b_equivalente = []
for i in range(inicio, final):
    lista_b_equivalente.append(lista[i])

print(f'lista_b_equivalente: {lista_b_equivalente}')