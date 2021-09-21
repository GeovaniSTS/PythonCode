turistas = 0
jipes = 0

info = input()
info = info.split()

while True:
 controle = int(info[0,1])
 if info[0] == ('SALIDA'):
  jipes += 1
  turistas += info[1]
 else:
  if info[0] == ('VUELTA'):
   jipes -= 1
   turistas -= info[1]
 break