A = float(input())
B = float(input())
C = float(input())

media = (A + B + C) / 3

sup = 0
if A > media:
    sup += 1
if B > media:
    sup += 1
if C > media:
    sup += 1
print(sup)