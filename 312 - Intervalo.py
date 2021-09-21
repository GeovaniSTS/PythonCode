ponto = float(input())

if 0 <= ponto <= 25:
 print('Intervalo [0,25]')
if 25 < ponto <= 50:
 print('Intervalo (25,50]')
if 50 < ponto <= 75:
 print('Intervalo (50,75]')
if 75 < ponto <= 100:
 print('Intervalo (75,100]')
if ponto < 0 or ponto > 100:
 print('Fora do Intervalo')