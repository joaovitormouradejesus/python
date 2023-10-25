#codigo sem funcao

fluxo_caixa = []

print("------------")
print("@ Fluxo caixa")
print("-----------")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("\n# Digite outro numero para encerrar #\n")

def adicionar_transacao():
    nome = input("Nome: ")
    valor = float( input("valor: "))
    fluxo_caixa.append({
        "nome": nome,
        "valor": valor,
    })

while True:
    opcao = int(input("Digite a opcao: "))

    if opcao == 1:
        adicionar_transacao()
    elif opcao == 2:
        adicionar_transacao()
    else:
        break

#Nota fiscal
total = 0
for fc in fluxo_caixa:
    print("nome:", fc['nome'], ", Valor: R$", fc['valor'])
    total = total + fc['valor']

print("Saldo atua: R$", total)