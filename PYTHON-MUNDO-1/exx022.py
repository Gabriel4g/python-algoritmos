a = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(a.upper()))
print("Seu nome em minusculas é {}".format(a.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(a) - a.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(a.find(' ')))
separa = a.split()
print('Seu primeiro nome é {}, e ele tem {} letras'.format(separa[0], len(separa[0])))












































