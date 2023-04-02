# leia 3 valores a,b,c a sehuir enconte 0 maior dos 3 valores e o escreva com a mensagem maior
a = int(input('Digite o valor de A:'))
b = int(input('Digite o valor de B:'))
c = int(input('Digite o valor de C:'))

if a > b and c:
    print('O valor de a: {} é maior que b:{} e c:{} '.format (a,b,c)  )
elif b > c:
    print('O valor de b: {} é maior que a:{} e c:{} '.format (b,a,c) )
else:
    print('O valor de c: {} é maior que a:{} e :b{} '.format (c,a,b))