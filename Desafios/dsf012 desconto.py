#Leia o preço de um produto e mostre seu novo valor só que com 5% de desconto.
preço = float(input('Digita o valor do produto: R$'))

desconto = preço-(preço * 5 / 100)
print('O produto que custava R${:.2f}, com a promoção de 5% de desconto vai custar R${:.2f}.'.format(preço, desconto))