N = int(input())
if N == 0:
 print('NULO')
elif N < 0:
 if N %2 == 0:
  print('NEGATIVO PAR')
 else:
  print('NEGATIVO IMPAR')
else:
 if N %2 == 0:
  print('POSITIVO PAR')
 else:
  print('POSITIVO IMPAR')