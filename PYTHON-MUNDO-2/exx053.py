import math
print('-=' * 20)
print('APLICATIVO CALCULO DE VALORES ARITMETICOS')
print('-=' * 20)
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
adicao = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
print('''Suas opçoes: )
[ 1 ] Adição
[ 2 ] Subtração
[ 3 ] Multiplicação
[ 4 ] Divisão ''')
usuario = float(input('Escolha uma Opção: '))
if usuario == 1:
    print('A soma entre {:.0f} e {:.0f} é {:.0f} '.format(n1, n2, adicao))
elif usuario == 2:
    print('A subtração entre {:.0f} e {:.0f} é {:.0f}'.format(n1, n2, subtracao))
elif usuario == 3:
    print('A multiplicação entre {:.0f} e {:.0f} é {:.0f}'.format(n1, n2, multiplicacao))
elif usuario == 4:
    print('A divisão entre {:.0f} e {:.0f} é {}'.format(n1, n2, divisao))
elif usuario > 4:
    print('ERRO! Tente novamente')














