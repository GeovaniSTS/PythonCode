X = float(input())

A = (X*1.5)
B = (A*0.15)
C = A-B

print('Valor a ser pago: R$', '%.2f' %A, 'reais')
print('Valor a ser pago com desconto: R$', '%.2f' %C, 'reais')