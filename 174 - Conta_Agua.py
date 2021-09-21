N = int(input())
taxa1 = 7
taxa2 = 20
taxa3 = 140

if N <= 10:
  valor = taxa1
if 11 <= N <= 30:
  valor = taxa1 + (1* (N-10))
if 31 <= N <= 100:
  valor = taxa1 + taxa2 + (2* (N-30))
if N >= 101:
  valor = taxa1 + taxa2 + taxa3 + (5* (N-100))
print(valor)