N = int(input())

Hora = N // 3600
Resto = N % 3600
Minuto = Resto // 60
Segundo = Resto % 60

resp = '%.0f:%.0f:%.0f' %(Hora,Minuto,Segundo)
print(resp)