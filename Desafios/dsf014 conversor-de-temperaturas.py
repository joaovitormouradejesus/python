#Escreva um programa que conver uma temperatura de ºC para ºF
c = float(input('Escreva qual é a temperatura em °C: '))
f = ((9 * c) / 5)+ 32

print('A temperatura de {:.1f}°C correspondem a {:.1f}°F!'.format(c, f))