#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
'''– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros'''
print('{:=^40}'.format(' LOJAS JOAZIN '))
pro = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO:
[1] Á vista dinheiro/cheque:
[2] À vista no cartão:
[3] 2x no cartão:
[4] 3x ou mais no cartão: ''')
metodo = str(input('Qual é a opção? ')).strip()

if metodo == '1':
    desc = pro - (pro * 10 / 100)
elif metodo == '2':
    desc = pro - (pro * 5 / 100)
elif metodo == '3':
    total = pro
    par = total / 2
    print('Sua compra vai ser parcelada em 2x de R${:.2f} no final.'.format(par))
elif metodo == '4':
    total = pro + (pro * 20 / 100)
    pa = int(input('Em quantas parcelas? '))
    parcela = total / pa 
    print('Sua compra será parcelada em {}x de R${} COM JUROS'.format(pa, parcela))
else:
    total = pro
    print('OPÇÂO INVALIDA, tente novamente.')
print('Sua compra de R${} vai custar R${} no final.'.format(pro, total))