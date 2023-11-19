#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura') #Jogadas provaveis
computador = randint(0, 2) #Escolha da jogada do computador
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogada = int(input('Qual é sua jogada? '))
print('JO')
sleep (1)
print('KEN')
sleep (1)
print('PO!!!!')
print('-='*13)
print('Computador jogou {}.\nJogador jogou {}. '.format(itens[computador], itens[jogada]))
print('-='*13)
if computador == 0: #Jogou Pedra
    if jogada == 0:
        print('EMPATE!!!')
    elif jogada == 1:
        print('JOGADOR VENCEU!!!')
    elif jogada == 2:
        print('COMPUTADOR VENCEU!!!')
elif computador == 1: #Jogou Papel
    if jogada == 0:
        print('COMPUTADOR VENCEU!!!')
    elif jogada == 1:
        print('EMPATE!!!!')
    elif jogada == 2:
        print('JOGADOR VENCEU!!')
elif computador == 2: #Jogou Tesoura
    if jogada == 0:
        print('JOGADOR VENCEU!!!')
    elif jogada == 1:
        print('COMPUTADOR CENCEU!!!')
    elif jogada == 2:
        print('EMPATE!!!')
