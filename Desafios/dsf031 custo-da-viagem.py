#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
km = float(input('Qual é a distância da sua viagem? '))
print('Você está preste a fazer uma viagem de {}Km.'.format(km))

if km <= 200:
    passagem = km * 0.50
else:
    passagem = km * 0.45
print('O valor da sua passagem vai ser de R${:.2f}'.format(passagem))