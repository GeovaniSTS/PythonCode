tabela = {'suco de laranja':120, 'morango fresco':85, 'mamao':85, 'goiaba vermelha':70, 'manga': 56, 'laranja':50, 'brocolis':34}

while True:
    t = int(input())
    if t == 0:
        break
    energia = 0
    for i in range(t):
        lista = input().split()
        quantidade = int(lista[0])
        alimentos = ' '.join(lista[1:])
        energia += tabela[alimentos]*quantidade
    if energia > 130:
        energia = energia-130
        print('Menos',energia, 'mg')
    elif energia < 110:
        energia = 110-energia
        print('Mais',energia, 'mg')
    else:
        print(energia, 'mg')