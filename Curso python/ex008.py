nome = str(input('Digite seu nome: '))
if nome == 'Gustavo':
    print('Que nome BONITO!!')
elif nome == 'João' or nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Creusa Ana Jéssica Rose':
    print('Que belo nome feminino!')

print('Tenha um bom dia, {}!'.format(nome))