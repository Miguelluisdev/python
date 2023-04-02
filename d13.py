aluguel = int(input('digite quantos dias  o carro foi alugado'))
carro = float(input('quantos quilometro o carro percorreu'))
dias = (aluguel * 60) + (carro * 0.15)
print('o valor a ser pago é R$ {:.2f}'.format(dias))

