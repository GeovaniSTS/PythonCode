A = 0
N1 = int(input())
N2 = int(input())
N3 = int(input())

if  N1 > N2:
 A = N2
 N2 = N1
 N1 = A
if N1 > N3:
 A = N3
 N3 = N1
 N1 = A
if N2 > N3:
 A = N3
 N3 = N2
 N2 = A

print(N3)
print(N2)
print(N1)