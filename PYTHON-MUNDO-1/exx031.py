distancia = float(input('Qual a distancia da sua viagem? '))
print('Voce esta prestes a começar uma viagem de {}Km'.format(distancia))
if distancia <=200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O valor da sua passagem é de R${:.2f}'.format(preco))













