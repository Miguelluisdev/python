import math # pode fazer assim from math import radians, sin , cos , tan
angulo = float(input('digite o angulo que voce deseja'))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('o angulo de {:.2f}, \n tem o seno de {:.2f}  \n o cos de {:.2f} \n e uma tangente de {} '.format(angulo,sen,cos,tan))