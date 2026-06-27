# sem compreensões:

def achatar(lista):
    resultado = []
    for item in lista:
        if isinstance(item, list):
            resultado.extend(achatar(item))
        else:
            resultado.append(item)
    return resultado

# com compreensões:

def achatar(lista):
    return [elemento for item in lista for elemento in (achatar(item) if isinstance(item, list) else [item])]