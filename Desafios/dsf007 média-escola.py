#Calcule a média de um aluno e mostre o resultado
nome = input('Qual o nome do aluno? ')
u1 = int(input('Digite a nota da unidade 1: '))
u2 = int(input('Digite a nota da unidade 2: '))
u3 = int(input('Digite a nota da unidade 3: '))

m = u1+u2+u3/2
print('A média do aluno {} foi {:3},'.format(nome, m), end=' ')
if m >= 15:
    print('o aluno foi aprovado.')
else:
    print('O aluno foi reprovado.')
