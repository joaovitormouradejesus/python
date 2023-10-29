n = (input('Digite algo: '))

print('O tipo primitivo desse valor é {} é um número? {}, é alfabetico? {}, é um décimal? {}, ta em minusculo? {}, ta em maiusculo? {}, só tem espaços? {}, Ta capitalizada? {}, e alfanúmerico? {} '.format(type(n), n.isnumeric(), n.isalpha(), n.isdecimal(), n.islower(), n.isupper(), n.isspace(), n.istitle(), n.isalnum()))
