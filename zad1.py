def sklej1(a_list, b_list):
    if len(a_list) != len(b_list):
        return "Listy nie są takiej samej długości!"
    else:
        suma = list()
        for i in range(len(a_list)):
            if i % 2 == 0:
                suma.append(a_list[i])
            else:
                suma.append(b_list[i])
        return suma


def sklej2(a_list, b_list):
    suma = list()
    for i in range(len(a_list)):
        if i % 2 == 0:
            suma.append(a_list[i])
            print("Indeks: {} | Wartość : {}".format(i, a_list[i]))
    for i in range(len(b_list)):
        if i % 2 !=0:
            suma.append(b_list[i])
            print("Indeks: {} | Wartość : {}".format(i, b_list[i]))
    return suma

lista1 = [1,1,1,1,1,1]
lista2 = [2,2,2,2,2,2]
lista12 = sklej2(lista1, lista2)
lista13 = sklej1(lista1, lista2)
print("Lista gdzie na parzystych indeksach znajdują się elementy listy 1, a na nie parystych elementy listy 2:")
print(lista13)
print("Lista elementów z indeksów parzystych listy 1 i elementów z indeksów nieparzystych listy 2:")
print(lista12)
