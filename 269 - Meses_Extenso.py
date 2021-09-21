Mês = ["janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
Data = int(input())

if (1<= Data <=12):
 print(Mês[Data - 1])
else:
 print('invalido')