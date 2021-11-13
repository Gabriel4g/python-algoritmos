print('-=' * 20)
print('\033[1;34m Analisador de triangulos \033[0;0m')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os SEGMENTOS acima podem formar um TRIANGULO!')
else:
    print('Os segmentos acima não podem formar um triangulo!')










