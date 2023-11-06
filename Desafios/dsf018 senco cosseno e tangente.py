#Leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
an = float(input('Digite um ângulo qualquer: '))
seno = sin(radians(an))
coseno = cos(radians(an))
tangente = tan(radians(an))

print('A ângulo de {} tem o SENO de {:.2f}'.format(an, seno))
print('A ângulo de {} tem o COSENO de {:.2f}'.format(an, coseno))
print('A ângulo de {} tem a TANGENTE de {:.2f}'.format(an, tangente))