import os

mensagem = []

nome = input("Digite seu nome: ")

while True:

    #limpando terminal
    os.system('cls')

    if len(mensagem) > 0:
        for m in mensagem:
            print(m['nome'], "-", m['texto'])

    print("_______________")

    #Obtendo texto
    texto = input("mensagem: ")
    if texto == "fim":
        break

    #adicionando mensagem na lista
    mensagem.append({
        "nome": nome,
        "texto": texto
    })