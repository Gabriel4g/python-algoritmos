peso = float(input('Digite seu peso: Kg '))
altura = float(input('Digite sua altura: (m) '))
imc = peso/(altura ** 2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc <= 18.5:
    print('Voce esta abaixo do peso normal ')
elif 18.5 <= imc < 25:
    print('Voce esta no peso normal')
elif 25 <= imc < 30:
    print('Voce esta na faixa etaria de SOBREPESO')
elif 30 <= imc < 40:
    print('Cuidado! OBESIDADE')
elif imc >= 40:
    print('Tome muito cuidado! Obesidade morbida')










