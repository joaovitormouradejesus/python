#Leia o slario atual de um funcionario e mostre qual sera o novo salario com 15% de aumento
salario = float(input('Digite o seu salário atual: R$'))
novo = salario+(salario*15 / 100)

print('Você recebeu um aumento, parabéns! O seu salario atual e de R${:.2f} mas com o aumento de 15% vai ficar R${:.2f}'.format(salario, novo))