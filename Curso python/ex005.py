n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = (n1+n2)
sub = (n1-n2)
m = (n1*n2)
d = (n1/n2)
di = (n1//n2)
e = (n1**n2)

print('A soma dos valores vale {}!\n A subtração vale {}! A multiplicação vale {}!'.format(s, sub, m), end=' ')
print('A divisão vale {}! A divisão inteira vale {}! A pontência vale {}!'.format(d, di, e))
