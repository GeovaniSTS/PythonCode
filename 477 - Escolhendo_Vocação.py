forca = int(input())
inteligencia = int(input())
destreza = int(input())
furtividade = int(input())
peso = int(input())

if forca < 5:
  print('Mage')
elif destreza < 5:
  print('Orc')
elif peso < 5:
  print('Paladin')
else:
  print('Knight')