num1 = 0
num2 = 0
while num2 >= num1:
    n = input()
    m = input()
    num1 = int(n)
    num2 = int(m)
    if n % 2 == 0:
        print('Par')
    else:
        print('Impar')
print(num2/num1)
print(num1/num2)