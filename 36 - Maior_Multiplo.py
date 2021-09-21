m = int(input())
n = int(input())
f = int(n/m)
if m*f > n or f == 0:
 print('sem multiplos menores que', n)
else:
 print(m*f)