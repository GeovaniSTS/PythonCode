comida = input().lower()
bebida = input().lower()
valor = 0

if comida == 'lasanha' and bebida == 'refrigerante':
  valor = 8 + 3
elif comida == 'lasanha' and bebida == 'suco':
  valor = 8 + 2.5
elif comida == 'estrogonofe' and bebida == 'refrigerante':
  valor = 11 + 3
elif comida == 'estrogonofe' and bebida == 'suco':
  valor = 11 + 2.5

print('%.2f'%valor)