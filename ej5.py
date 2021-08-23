"""
Ejercicio 5:
Realizar una función recursiva que reciba una lista y que calcule el producto de los elementos de la lista:
"""

def productoLista(lista):
    if len(lista)==1:
        return lista[0]
    else:
        return lista[0] * productoLista(lista[1:])


numeros=[5,2,4]


print(productoLista(numeros))