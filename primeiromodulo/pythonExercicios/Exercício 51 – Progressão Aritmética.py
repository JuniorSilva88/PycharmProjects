print('''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.''')
pr = int(input('Primeiro termo: '))  # determinando o termo
rz = int(input('Razão: '))  # determinando a razão
déc = pr + (10 - 1) * rz  # formula matematica para desobrir o enésimo termo
for c in range(pr, déc + rz, rz):
    print('{}'.format(c), end=' ➡️')
print('Fim')
