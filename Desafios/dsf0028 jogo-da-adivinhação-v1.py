#Faça um programa que escolha aleatoriamente um numero ente 0 a 5, e nos peça para advinhar qual o número que ele escolheu, e faça ele dizer se vencemos ou perdemos.
from random import randint
from time import sleep

computador = randint(0, 5) #Faz o sortei ente um número e outro.
print('\033[31m-=-'*20)
print('\033[37mVou pensar em um número entre 0 a 5. Eente adivinhar...')
print('\033[31m-=-'*20)
r = int(input('\033[37mAdivinhe qual número to pensando? ')) #O Úsuario escreve a resposta.
print('\033[31mProcessando...')
sleep(1) #Faz o código parar pela quantidade de segundos que você determinar.
if r == computador:
    print('\033[34mParabens!! Você ACERTOU!')
else:
    print('\033[31mHahaha Você PERDEU!! Eu pensei no número {} e não no {}'.format(computador, r))