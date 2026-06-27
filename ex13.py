def pares_matriz(matriz):
    return [n for linha in matriz for n in linha if n % 2 == 0]