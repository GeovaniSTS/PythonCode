def calcular_nivel(velocidades):
    if velocidades < 10:
        return 1
    elif 10 <= velocidades < 20:
        return 2
    else:
        return 3

while True:
    l = int(input())
    if l != 0:
        x = input().split()
        velocidades = 0
        for i in range(l):
            if int(x[i]) > velocidades:
                velocidades = int(x[i])
        vi = calcular_nivel(velocidades)
        print(vi)
    if l == 0:
        break