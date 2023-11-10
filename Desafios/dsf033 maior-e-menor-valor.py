#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite o Primeiro valor: '))
n2 = int(input('Digite o Segundo valor: '))
n3 = int(input('Digite o Terceiro valor: '))
#Verificando qual é o menor número
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
#Verficando qual é o maior número
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O menor valor foi o {}'.format(menor))
print('O maior valor foi o {}'.format(maior))