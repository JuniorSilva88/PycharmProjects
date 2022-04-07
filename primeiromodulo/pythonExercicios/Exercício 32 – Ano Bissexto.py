from datetime import date
print('Faça um programa que leia um ano qualquer e mostre se ele é bissexto.')
ano = int(input('Qual ano você quer analisar? digite 0 para seu ano atual! '))  # 0 = ano atual
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO! '.format(ano))
else:
    print('O ano {}, NÃO É BISSEXTO .'.format(ano))
