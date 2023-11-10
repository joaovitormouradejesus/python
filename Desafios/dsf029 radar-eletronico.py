#
velo = float(input('Qual é a velocidade atual do seu carro? '))
if velo > 80:
    multa = (velo-80) * 7
    print('MULTADO! Você excedeu o limite permitido de 80km/h \nVocê deve pagar uma multa de R$ {:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')