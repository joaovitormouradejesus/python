#Leia quanto dinheiro uma pessoa tem e mostre quantos dólares ele pode comprar.
din = float(input('Quanto dinheiro você tem? '))
u = 4.98

dolar = din/u

print('Você pode comprar U${:.2f} dólares.'.format(dolar))