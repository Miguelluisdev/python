mt = int(input('digite sua matricula'))
n1 = float(input('digite sua nota 1'))
n2 = float(input('digite sua nota 2'))
n3 = float(input('digite sua nota 3'))
if (n1 > n2)  and (n1>n3):
    MP = (n1*4 +n2*3+n3*3)/10
else:
    if(n2 > n1) and (n2 > n3):
        MP = (n1*3 + n2*4 + n3*3 )/10
    else:
        MP = (n1*3 + n2*3 + n3*3)
print('media=', MP )

if MP>= 5:
    print('aprovado')
else:
    print('reprovado')
