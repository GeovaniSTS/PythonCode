D = int(input())
medidas = input()
medidas = medidas.split()

A = float(medidas[0])
L = float(medidas[1])
P = float(medidas[2])

if D <= A and D <= L and D <= P:
  print('S')
else:
  print('N')