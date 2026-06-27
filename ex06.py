def contar_vogais(texto):
    return sum(1 for char in texto if char.lower() in 'aeiou')