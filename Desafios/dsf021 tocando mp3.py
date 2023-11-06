#Abra e reproduza um audio de um arquivo mp3.
import pygame
import os

pygame.init()
caminho_arquivo = os.path.join('C:/Programação/Estudos/python/Desafios/ex021.mp3')
pygame.mixer.music.load('C:/Programação/Estudos/python/Desafios/ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

