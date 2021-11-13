a = str(input('Digite seu nome completo: ')).strip()
nome = a.split()
print('Prazer em te conhecer!'.format(a))
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))














