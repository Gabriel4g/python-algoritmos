from random import randint
computador = randint(0, 5) #Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um numero de 0 a 5. Tente adivinhar...')# Faz o computador pensar
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))# Jogador tenta adivinhar
if jogador == computador:
    print('PARABENS man, vc me venceu!')
else:
    print('PERDEU kkkkkkkkk, pensei no numero {} e nao no {}'.format(computador, jogador))









