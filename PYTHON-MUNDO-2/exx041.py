from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('É considerado MIRIM')
elif idade <= 14:
    print('É considerado INFANTIL')
elif idade <= 19:
    print('É considerado JUNIOR')
elif idade <= 25:
    print('É considerado Sênior')
else:
    print('Classificação MASTER')
