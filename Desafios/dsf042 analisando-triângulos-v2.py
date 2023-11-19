#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: – EQUILÁTERO: todos os lados iguais – ISÓSCELES: dois lados iguais, um diferente – ESCALENO: todos os lados diferentes
print('-=-'*20)
print('Analisador Triângulo')
print('-=-'*20)

seg1 = float(input('Digite o primeiro segmento: '))
seg2 = float(input('Digite o segundo segmento: '))
seg3 = float(input('Digite o terceiro segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg2 + seg3 and seg3 < seg1 + seg2:
    print('Os segminetos PODEM formar um triângulo ', end='')
    if seg1 == seg2 == seg3:
        print('EQUILÁTERO!')
    elif seg1 != seg2 != seg3 != seg1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Os segmentos NÃO PODEM formar um triângulo!')