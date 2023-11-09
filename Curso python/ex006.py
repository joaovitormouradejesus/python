nome = str('Joazin mil grau').strip()

print(nome[2:7])

print(nome[::2])

print('No nome {} tem a letra "a" {} vezes.'.format(nome, nome.count('a')))

print(nome.upper())
print(nome.lower())
print(nome.capitalize())

print('Esse nome tem {} letras.'.format(len(nome) - nome.count(' ')))
print(nome.strip())

print('Seu nome tem Silva? {}'.format('Silva' in nome.upper()))