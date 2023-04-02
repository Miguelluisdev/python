# calculo de porcentagem
#desconto 5%
# para fazero descoto basta pegar o preço vezes a porcentagem divididop por 100 com o resultado diminui com o pr3eço
preço = float(input('qualk é o preço do produto  R$ '))
novo = preço - (preço * 5 / 100  )
print('o produto que cutsa {}, com 5% de desconto custa agora {:.2f}'.format(preço,novo))


# segunda forma de fazer esse exercicio, sem desconto fixo, o cliente coloca o desconto
# preço = float(input('Qual o preço do produto ?R$'))
# Desconto = float(input('Qual o desconto?'))
# Descontado = Preço-(Preço*Desconto/100)
# print('O valor com desconto é:{}' .format(Descontado))



