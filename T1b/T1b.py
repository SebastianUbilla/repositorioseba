#taller 1.b sebastian ubilla
lista = list()
lista = ['avion', 'perro', 'gato', 'avion', 'edificio', 'gato'] #aqui agregar la lista para probar el codigo
def ocurrencias(lista):
    dic = dict()
    for i in lista:
        if i in dic:
            dic[i]= dic[i] + 1
        else:
            dic[i]= 1

    items = dic.items()
    return (items)
print(ocurrencias(lista))
