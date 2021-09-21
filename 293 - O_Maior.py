def maiorAB(num1, num2, num3):
    a = int(num1)
    b = int(num2)
    c = int(num3)
    Maior = (a+b+abs(a-b))/2
    if a > Maior:
     return(a, 'eh o maior')
    elif b > Maior:
     return(b, 'eh o maior')
    else:
     return(c, 'eh o maior')

Maior = input()
Maior = Maior.split()
num1 = int(Maior[0])
num2 = int(Maior[1])
num3 = int(Maior[2])
resultado = maiorAB(num1, num2, num3)
print(resultado)