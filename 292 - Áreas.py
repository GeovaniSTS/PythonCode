entrada = input()
entrada = entrada.split()

A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

pi = 3.14159

tri = (A*C)/2
cir = (pi*(C*C))
tra = ((A + B) * C)/2
qua = (B*B)
ret = (A*B)

print('TRIANGULO:', '%.3f' %tri)
print('CIRCULO:', '%.3f' %cir)
print('TRAPEZIO:', '%.3f' %tra)
print('QUADRADO:', '%.3f' %qua)
print('RETANGULO:', '%.3f' %ret)