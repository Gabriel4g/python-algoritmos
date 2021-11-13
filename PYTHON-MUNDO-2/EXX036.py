casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de {}R$ em {} anos'.format(casa, anos))
print('A prestação sera de {}'.format(prestacao))
if prestacao <= minimo:
    print('O emprestimo pode ser CONSEDIDO')
else:
    print('O emprestismo não pode ser CONCEDIDO')







