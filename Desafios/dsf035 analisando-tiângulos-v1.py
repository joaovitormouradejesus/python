#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-=-'*20)
print('Analisador Triângulo')
print('-=-'*20)

seg1 = float(input('Digite o primeiro segmento: '))
seg2 = float(input('Digite o segundo segmento: '))
seg3 = float(input('Digite o terceiro segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg2 + seg3 and seg3 < seg1 + seg2:
    print('Os segminetos PODEM formar um triângulo!')
else:
    print('Os segmentos NÃO PODEM formar um triângulo!')