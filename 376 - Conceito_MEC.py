livros = int(input())
alunos = int(input())
calculo = 0

calculo = alunos//livros
if calculo <= 8:
  print('A')
if 9 <= calculo <= 12:
  print('B')
if 13 <= calculo <= 18:
  print('C')
if calculo > 18:
  print('D')