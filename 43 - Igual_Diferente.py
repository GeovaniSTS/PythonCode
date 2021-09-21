N1 = int(input())
N2 = int(input())
N3 = int(input())

if N1 == N2 == N3:
 print(1)
elif (N1 == N2) or (N1 == N3) or (N2 == N3):
 print(3)
else:
 print(2)