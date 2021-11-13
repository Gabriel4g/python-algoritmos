n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) /2
print('Tirando {}, e {} a media do aluno é {} '.format(n1, n2, media))
if 7> media >=5:
    print('Voce esta de RECUPERAÇÃO!')
elif media <5:
    print('Voce esta REPROVADO!')
elif media >7:
    print('Voce esta APROVADO!')
quit()



