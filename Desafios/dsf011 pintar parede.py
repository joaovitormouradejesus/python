#Lei a largura e a altura de uma parede e calcule qual é a sua area e a quantidade tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta 2m2.
lag = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = lag*alt

print('A parede tem a propoção de {}x{} e sua àrea é de {}m².'.format(lag, alt, area))
tinta = area/2
print('E para pintar essa parede vai ser preciso {:.1f}L de tinta'.format(tinta))