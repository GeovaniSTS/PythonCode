N = int(input())

if(N < 0):
 N =  N * (-1)
 print((N%10) * (-1))
else:
 print(N%10)