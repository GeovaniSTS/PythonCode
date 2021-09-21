mes = int(input())
ano = int(input())
dia = 31
bissexto = 0

if ano%400==0:
   bissexto = 1
else:
   if ano%4==0 and ano%100!=0:
      bissexto = 1
   else:
      bissexto = 0

if mes == 2:
   if bissexto == 1:
      dia = 29
   else:
      dia = 28
  
if mes == 4 or mes == 6 or mes == 9 or mes == 11:
   dia = 30
   
print(dia)