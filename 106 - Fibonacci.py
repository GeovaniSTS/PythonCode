def fibo(x):
    numero = int(x)
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibo(numero - 1) + fibo(numero - 2)

x = int(input())
resultado = fibo(x)
print(resultado)