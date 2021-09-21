entrada = input()
entrada = entrada.split()

num1 = int(entrada[0])
num2 = int(entrada[1])
num3 = int(entrada[2])
num4 = int(entrada[3])

if (num2 > num3) and (num4 > num1) and ((num3 + num4) > (num1 + num2)) and (num3 > 0 and num4 > 0) and (num1%2 == 0):
  print('Valores aceitos')
else:
  print('Valores nao aceitos')