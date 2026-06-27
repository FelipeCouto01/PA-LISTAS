def filtrar_nomes(nomes):
    resultado = []
    for nome in nomes:
        if len(nome) > 5:
            resultado.append(nome)
    return resultado