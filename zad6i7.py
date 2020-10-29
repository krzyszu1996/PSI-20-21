lista = []
for i in range(10):
    lista.insert(i,i + 1)

print(lista)

lista2 = lista[:5]
print(lista2)
lista3 = lista[5:10]
print(lista3)

lista4 =[0] + lista2 + lista3
print(lista4)

lista4_odw = lista4
lista4_odw.sort(reverse=True)
print(lista4_odw)