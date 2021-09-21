def AnalisarSituacao(num1, num2, num3, num4):
    nota1 = float(num1)
    nota2 = float(num2)
    nota3 = float(num3)
    nota4 = float(num4)
    ponderada = (nota1*1 +nota2*2 + nota3*3 + nota4*4) / (1 + 2 + 3 + 4)
    if ponderada >= 9:
        return('aprovado com louvor')
    elif ponderada >= 7:
        return('aprovado')
    else:
        if ponderada <= 3:
            return('reprovado')
        if 3 <= ponderada < 7:
            return('prova final')

entrada = input()
entrada = entrada.split()
num1 = float(entrada[0])
num2 = float(entrada[1])
num3 = float(entrada[2])
num4 = float(entrada[3])
resultado = AnalisarSituacao(num1, num2, num3, num4)
print(resultado)