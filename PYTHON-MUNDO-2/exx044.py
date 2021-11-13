preco = float(input('Preco das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] a vista cartao
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartao''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total /2
    print('Sua compra vai ser parcelada em 2x de R$ {:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparcel = int(input('Quantas parcelas? '))
    parcela = total / 3
    print(' Sua compra sera parcelada em {}x de {:.2f} com JUROS '.format(totparcel, parcela))
else:
    total = preco
    print('ERRO! OPCAO INVALIDA TENTE NOVAMENTE')
    print('Sua compra de {:.2f} vai custar  R${:.2f} no final'.format(preco, total))
















