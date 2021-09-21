A = int(input())
B = int(input())
C = int(input())

if A != B and A != C:
  print('A')
if B != A and B != C:
  print('B')
if C != A and C != B:
  print('C')
if A == B and B == C:
  print('* ')