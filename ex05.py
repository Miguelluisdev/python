import math
# hypot() para sfazer a hipotenusa
cateto1 = float(input('digite o valor do cateto oposto'))
cateto2 = float(input('digite o valor do cateto adjacente'))
hi = math.hypot(cateto1, cateto2)
print(' a hipotenusa é {:.2f}'.format(hi))














# maneira tradicional
'''
cateto1 = float(input('digitre o  valor do cateto oposto'))
cateto2 = float(input('digite oi valor co cateto adjascente'))
hi = (cateto1 ** 2 + cateto2 ** 2) ** (1/2)
print('a hipotenusa vai medir {:.2f}'.format(hi)) '''