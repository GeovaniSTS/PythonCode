A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

negativo = 0

print('Digite um Valor:', A)
if A < 0:
 negativo += 1
print('Digite um Valor:', B)
if B < 0:
 negativo += 1
print('Digite um Valor:', C)
if C < 0:
 negativo += 1
print('Digite um Valor:', D)
if D < 0:
 negativo += 1
print('Digite um Valor:', E)
if E < 0:
 negativo += 1

print(negativo, 'negativos')