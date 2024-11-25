def busqueda_secuencial(lista, objetivo):
    """Búsqueda secuencial"""
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1 


lista = [3, 5, 2, 8, 6]
numero_objetivo = 8
resultado = busqueda_secuencial(lista, numero_objetivo)

if resultado != -1:
    print(f"El número {numero_objetivo} se encuentra en la posición: {resultado}")
else:
    print(f"El número {numero_objetivo} NO se encuentra en la lista.")