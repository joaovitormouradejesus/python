nome = str(input('Qual é seu nome? ')).strip()

if nome == 'João':
    print('Que nome lindo!')
else:
    print('Que nome normal!')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1 + n2)/2

print('A sua média foi {:.1f}!'.format(m))
if m >= 6.0:
    print('Você foi aprovado! PARABÊNS!')
else:
    print('Você foi reprovado... ESTUDE MAIS!')

