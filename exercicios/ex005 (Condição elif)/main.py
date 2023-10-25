salario = float(input("Informe seu salário: "))

if salario <= 3000:
    print("Programador junior.")
elif salario > 3000 and salario <= 6000:
    #o código "and" serve para acresentar outro valor.
    print("Programador pleno")
elif salario > 6000 and salario <= 15000:
    print("Programador senior")
#Se o valor da váriavel salario for maior que 6000 ou menor que 15000, ou seja se o valor estiver entre esses dois vai ser mostrado que ele é um programador senior.
else:
    print("Gerente de projeto")
#Caso o valor seja maior que 15000 vai ser mostrado que é o gerente do projeto.