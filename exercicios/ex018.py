from math import radians, sin, cos, tan
angulo = float(input('Digite o Angulo que deseja'))
seno = sin(radians(angulo))
print('O angulo de {} tem o Seno de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O angulo de {} tem o Cosseno de {:.2f}'.format(angulo,cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem a Tangente de {:.2f}'.format(angulo, tangente))