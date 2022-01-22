import random
from pprint import pprint

def buscar_secuencia(matriz, n, long_secuencia, horizontal=True):
    h = []
    ant = 0
    r = range(n)

    for i in r:
        for j in range(0, n - long_secuencia + 1):
            ant = matriz[i][j] if horizontal else matriz[j][i]
            h = [{
                    'p': (i, j) if horizontal else (j, i),
                    'v': matriz[i][j] if horizontal else matriz[j][i]
                }]

            for k in range(j + 1, j + long_secuencia):
                e = matriz[i][k] if horizontal else matriz[k][i]
                if e - ant == 1:
                    h.append({
                        'p': (i, k) if horizontal else (k, i),
                        'v': e
                    })
                    ant = e
                else:
                    h = []
                    break
            if h:
                break
        if h:
            break
    return h


def imprimir_resultado(direccion, h, long_secuencia):
    print(f"Se encontró una secuencia {direccion}.")
    print("Comienza en la posición:", h[0]['p'])

    print("Termina en la posición:", h[long_secuencia - 1]['p'])

    s = [d['v'] for d in h]
    print("La secuencia es:", s, "\n")


def main():
    n = 5
    c = 4
    h = []
    assert c <= n, "La cantidad de números consecutivos a buscar es inválida."

    r = range(n)
    
    matriz = [[random.randint(0, 12) for x in r] for y in r]
    # matriz = [[0, 4, 5, 6, 2], [1, 2, 3, 4, 8], [4, 0, 2, 2, 9], [3, 0, 1, 0, 10], [2, 3, 2, 3, 11]]
    
    print("La matriz es:")
    pprint(matriz)
    print()
    
    # Busca alguna secuencia horizontal
    h = buscar_secuencia(matriz, n, c)
    if h:
        imprimir_resultado("horizontal", h, c)
    else:
        print("No hay secuencias horizontales en las filas.")

    # Busca alguna secuencia vertical
    h = buscar_secuencia(matriz, n, c, False)
    if h:
        imprimir_resultado("vertical", h, c)
    else:
        print("No hay secuencias verticales en las columnas.")
        
        
        
if __name__ == "__main__":
    main()