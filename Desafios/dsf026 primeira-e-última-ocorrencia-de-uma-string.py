#faça um programa que leia uma frase  pelo teclado e mostra: 1- Quantos vezes aparece a letra 'A'; 2- Em que posição ela aparece a primeira vez; 3- Em que posição ela aparece e a última vez.
f= str(input('Digite uma frase: ')).upper().strip()

print('A letra "A" apareeu {} vez na frase.'.format(f.count('A')))
print('A primeira letra "A" apareceu na posição {}.'.format(f.find('A')+1))
print('A última letra "A" apareceu na posição {}.'.format(f.rfind('A')+1))