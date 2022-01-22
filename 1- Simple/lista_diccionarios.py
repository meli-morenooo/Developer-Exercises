import random

def generar_lista_diccionarios():
    lista = []
    diccionario = {}
    
    for x in range(1,11):
        edad = random.randint(1, 100)
        diccionario[x] = edad
    
    lista.append(diccionario)
    return lista

if __name__ == '__main__':
    print(generar_lista_diccionarios())
    