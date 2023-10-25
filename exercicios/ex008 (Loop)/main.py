notas = []

contador = 1

while contador <= 5:
    codiogo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codiogo_aluno, nota]
    notas.append(resultado)

    #Alternativa: contador += 1
    contador = contador + 1

print( "Quantidade de notas", len(notas) )

for n in notas:
    codiogo_aluno = n[0]
    nota = n[1]
    print("O RM", codiogo_aluno, "Tirou a nota",nota)
   
