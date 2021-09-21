L1 = float(input())
L2 = float(input())
L3 = float(input())

if L1 == L2 and L1 == L3 and L2 == L3:
 print('equilatero')
else:
 if L1 == L2 or L1 == L3 or L2 == L3:
  print('isosceles')
if L1 != L2 and L1 != L3 and L2 != L3:
 print('escaleno')