dias = int(input())
km = int(input())

diaria = 90
kmbonus = 100
kmvalor = 0
kmtotal = 0

if dias > 1:
  kmbonus = kmbonus * dias
  diaria = diaria * dias

if km > kmbonus:
  kmtotal = km - kmbonus

if 0 < kmtotal:
  kmvalor = (kmtotal * 12)

valor = (diaria + kmvalor)
print('%.2f'%valor)