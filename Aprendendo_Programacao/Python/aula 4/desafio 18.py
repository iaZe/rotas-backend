import math
angulo = int(input('Qual valor do angulo? '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(sen, cos, tan))