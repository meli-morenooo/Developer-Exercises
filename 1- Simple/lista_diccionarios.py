import random

def generar_lista_diccionarios():
    lista = []
    diccionario = {}
    
    for x in range(1,11):
        edad = random.randint(1, 100)
        diccionario[x] = edad
    
    lista.append(diccionario)
    return lista

def menor_mayor_edad(funcion):
    lista_ordenada = []
    
    for d in funcion:
        joven = min(d, key=d.get)
        viejo = max(d, key=d.get)
        dicc = sorted(d.items())
            
    print(joven)
    print(viejo)
    print(dicc)
    
    
if __name__ == '__main__':
    # print(generar_lista_diccionarios())
    menor_mayor_edad(generar_lista_diccionarios())

