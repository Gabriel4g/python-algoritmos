num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversao:
[ 1 ] converter para binario
[ 2 ] converter para OCTAL
[ 3 ] converter para hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} Convertido para binario é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} Convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('opção invalida!')




















