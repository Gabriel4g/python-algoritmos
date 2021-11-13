velocidade = float(input('Digite a velocidade atual do carro: '))
if velocidade >80:
    print('Vc foi multado! Vc ultrapassou os 80km/h')
    multa = (velocidade-80) *7
    print('Vc deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança')




