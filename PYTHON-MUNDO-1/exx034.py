salario = float(input('Qual é o salario do funcionario: R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 /100)
else:
    novo = salario + (salario * 15/100)
print('Quem ganhava {:.2f}R$ passa a ganhar {:.2f}'.format(salario, novo))


















