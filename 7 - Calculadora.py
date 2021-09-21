print('Bem-Vindo à Calculadora Python')

continuar = 'y'
resultado = []

def calculadora(a, b, operador) :
    if operador == '+':
        return a + b
    elif operador == '*':
        return a * b
    elif operador == '/':
        return a / b
    elif operador == '-':
        return a - b

while continuar == 'y':
    operacao = input('Escolha uma operação [+, -, *, /] ou digite [0] para encerrar o programa! ')
    if operacao == '0':
        print('ENCERRANDO PROGRAMA ...')
        break
    elif operacao != '+' and operacao != '-' and operacao != '*' and operacao != '/':
        print('ERRO DE OPERADOR!!!')
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    resposta = calculadora(num1, num2, operacao)
    resultado.append(resposta)
    print('A resposta é', resposta)
print('Os resultados obtidos foram:', resultado)
