#Cire um programa que laia o nome completo de uma pessoa e mostre: 1- O nome com todas as letras maiúsculas e minúsculas; 2- Quantas letras ao todo (Sem considerar espaços); 3- Quantas letras tem o primeiro nome;
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maíusculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))