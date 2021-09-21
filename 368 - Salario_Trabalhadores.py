salario = float(input())

if salario > 500:
  salario = salario + (salario * 0.10)
elif salario > 300:
  salario = salario + (salario * 0.07)
else:
  salario = salario + (salario * 0.05)
print('%.2f'%salario)