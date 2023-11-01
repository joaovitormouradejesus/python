#Leia quanto dinheiro uma pessoa tem e mostre quantos dólares ele pode comprar.
din = float(input('Quanto dinheiro você tem? R$'))
dolar = din/4.98

print('Você pode comprar U${:.2f} dólares com R${:.2f}.'.format(dolar, din))