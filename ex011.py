# Faça um programa que leia a largura e a altura de uma parede em metros e calcule sua area e a qtd de tintas necessaria
# para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m²

lp = float(input('Largura da parede: '))
ap = float(input('Altura da parede: '))

area = lp * ap
tinta = area / 2

print('Sua parede tem a dimensão de {}x{} e sua area é de {}m².'.format(lp, ap, area))

print('Para pintar essa parede, você precisá {}L de tinta.'.format(tinta))
