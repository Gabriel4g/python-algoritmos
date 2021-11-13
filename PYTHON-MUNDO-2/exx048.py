soma = 0
cont = 0
for s in range(1, 501, 2):
    if s % 3 == 0:
        cont += 1
        soma += s
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))










