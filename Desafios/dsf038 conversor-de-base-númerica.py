#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um númeor inteiro: '))
print('''Esolha uma das bases para a sua conversão:
[1] para BINÁRIO 
[2] para OCTAL 
[3] para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('O número {} convertido para Binário fica: {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {} convertido para Octal fica: {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {} convertido para Hexadecimal fica: {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida!')

