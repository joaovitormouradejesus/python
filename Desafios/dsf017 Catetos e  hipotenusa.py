#Faça um programa que leia o cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Digite o valor de cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h1 = hypot(co, ca)

print('A medida da Hipotenosa é {:.2f}.'.format(h1))