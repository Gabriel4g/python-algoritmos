from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opçoes:)
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 20)
print('Computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=' * 20)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('Computador Vence')
    else:
        print('Jogada invalida!')
elif computador == 1:
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador venceu')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')














