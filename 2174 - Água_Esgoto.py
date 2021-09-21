entrada = input()
entrada = entrada.split()

X = float(entrada[0])
Y = float(entrada[1])

A = ((X*1000)*Y)
E = ((A*80)/100)
T = (A+E)

print('%.2f' %A)
print('%.2f' %E)
print('%.2f' %T)