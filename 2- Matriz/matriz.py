import random

m = 5
matriz = [[0 for x in range(m)] for y in range(m)]

for i in range(0, m):
    for j in range(0, m):
        matriz[i][j] = random.randint(1, 100)            

for i in matriz:
    print(i)

