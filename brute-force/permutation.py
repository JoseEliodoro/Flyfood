""" def permut(elements, perm = []):
    list_permutation = list()
    if len(elements) == 0:
        return [perm]
    else:
        
        for i in range(len(elements)):
            new_element = list((elements[:i])) + list((elements[(i+1):]))
            new_perm = list((perm) + [elements[i]])
            list_permutation.extend(permut(new_element, new_perm))
        return list_permutation
 """

def permut(lista):
    if len(lista) <= 1:
        return [lista]
    lista_aux = []
    for i, atual in enumerate(lista):
        elementos_restantes = lista[:i] + lista[i+1:]
        for p in permut(elementos_restantes):
            lista_aux.append([atual] + p)
            
    return lista_aux

