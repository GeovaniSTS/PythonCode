def fat(x):
    numero = int(x)
    if numero == 0:
        return 1
    elif numero > 0:
        return numero * fat(numero-1)
    else:
        print('ERROR')
