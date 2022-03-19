print('Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de '
      'tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados. ')
larg = float(input('Qual é a Largura da parede? '))
alt = float(input('Qual é a Altura da parede? '))
area = larg * alt
tinta = area / 2
print('Éssa é a área calculada da sua parede {:.2f}m²,\nSerá necesspario {:.2f} '
      'Litros de tinta para pinta-la.'.format(area, tinta))