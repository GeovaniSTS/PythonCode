N = int(input())

A = N // 100
Resto = N % 100
B = Resto // 50
Resto_1 = Resto % 50
C = Resto_1 // 20
Resto_2 = Resto_1 % 20
D = Resto_2 // 10
Resto_3 = Resto_2 % 10
E = Resto_3 // 5
Resto_4 = Resto_3 % 5
F = Resto_4 // 2
Resto_5 = Resto_4 % 2
G = Resto_5 // 1
Resto_6 = Resto_5 % 1

print(N)
print(A,'nota(s) de R$ 100,00')
print(B,'nota(s) de R$ 50,00')
print(C,'nota(s) de R$ 20,00')
print(D,'nota(s) de R$ 10,00')
print(E,'nota(s) de R$ 5,00')
print(F,'nota(s) de R$ 2,00')
print(G,'nota(s) de R$ 1,00')