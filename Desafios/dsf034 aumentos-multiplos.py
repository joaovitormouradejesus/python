#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. para salários superiores a R$1.250,00, calculer um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sa = float(input ('Qual é o sálario de um funcionário? R$'))
if sa <= 1250.00:
    up = sa + (sa*15 / 100)
else:
    up = sa + (sa*10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(sa, up))