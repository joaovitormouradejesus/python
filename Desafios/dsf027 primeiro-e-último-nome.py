#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo: ')).strip()
sep = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(sep[0]))
print('seu último nome é {}'.format(sep[len(sep)-1]))