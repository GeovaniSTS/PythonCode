numero = int(input())
primos = 0
unidade = numero // 1 % 10
resto = numero // 10
conta = resto + (unidade * 5)
if primos == 2:
 print(conta)
 print('S')
else:
 if primos != 2:
  print('N')
 else:
  print(0)

'''numero = int(input())
primos = 0
for c in range(1, numero + 1):
 if numero % c == 0:
  print(end='')
  primos += 1
 else:
  print(end='')
 print('{} '.format(c), end='')

print(primos)'''