V = float(input())
A = int(input())
T = 0

if A == 1:
 T = V * 0.03
elif A == 2:
 T = V * 0.05
Total = V + T

print ("%.2f" %Total)