import random
a = input('digite o nome do primeiro aluno')
b = input('digite o nome do segundo aluno')
c = input('digite o nome do terceiro aluno')
d = input('digiteo nome do quarto aluno')
# para criar uma lista basta por colchetes depois dlo =
lista = [a,b,c,d]
# pode por assim tambem escolhido = random.choice(lista) e depois um print
print(' o aluno escolhido foi {}'.format(random.choice([a,b,c,d])))

