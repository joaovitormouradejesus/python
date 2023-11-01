#Escreva um valor em m e converta em cm e mm
m = float(input('Digita um valor em metro: '))

print('O valor {}m, em cm fica {:.0f},  em mm fica {:.0f}, '.format(m, m*100, m*1000))