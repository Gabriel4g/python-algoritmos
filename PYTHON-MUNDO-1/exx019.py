from random import choice
p = str(input("Primeiro aluno: "))
s = str(input("Segundo aluno: "))
t = str(input("Terceiro aluno: "))
q = str(input("quarto aluno: "))
lista = [p, s, t, q]
escolhido = choice(lista)
print("O aluno escolhido foi {}".format(escolhido))













