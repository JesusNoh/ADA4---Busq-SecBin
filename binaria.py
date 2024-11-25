def busqueda_binaria(lista, objetivo):
    """Búsqueda binaria"""
    inicio = 0
    fin = len(lista) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        
        if lista[medio] == objetivo:
            return medio  
        elif lista[medio] < objetivo:
            inicio = medio + 1  
        else:
            fin = medio - 1  
            
    return -1 


lista_ordenada = [1, 3, 5, 7, 9]
numero_objetivo = 5
resultado = busqueda_binaria(lista_ordenada, numero_objetivo)

if resultado != -1:
    print(f"El número {numero_objetivo} se encuentra en la posición: {resultado}")
else:
    print(f"El número {numero_objetivo} NO se encuentra en la lista.")