print('-=' * 20)
print('\033[1;32m Analisador de triagunlos v2 \033[0;0m')
print('-=' * 20)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos podem formar um triangulo ', end='')
    if s1 == s2 == s3:
        print('EQUILATERO!')
    elif s1 != s2 != s3 != s1:
            print('ESCALENO!')
    else:
        print('ISOSCELES')
else:
    print('Os segmentos nao podem formar um triangulo')
    









