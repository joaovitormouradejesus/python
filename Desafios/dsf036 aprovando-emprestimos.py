#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Qual é o valor da casa que deseja comprar? R$'))
salário = float(input('Qual é seu salário? R$'))
anos = int(input('Em quantos anos você pretende financiar? R$'))
prestação = casa / (anos * 12)
minimo = salário * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestação))
if prestação <= minimo:
    print('Emprestimo CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')

