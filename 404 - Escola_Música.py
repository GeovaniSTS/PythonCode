def ClassificaAluno(n_media, n_falta):
    media = float(n_media)
    falta = int(n_falta)
    if falta <= 10 and media >= 9.5:
        return('APROVADO COM LOUVOR')
    elif falta <= 10 and media >= 7.0:
        return('APROVADO')
    else:
        if media < 7.0:
            return('REPROVADO')
        if falta > 10:
            return('REPROVADO POR FALTAS')

n_media = input()
n_falta = input()
resultado = ClassificaAluno(n_media, n_falta)
print(resultado)