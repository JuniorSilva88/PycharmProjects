from datetime import date
print('''Crie um programa que leia o ano de nascimento de sete pessoas. 
No final mostre quantas pessoas ainda não atingiram a maioridade e 
quantas já são maiores''')
atual = ano = date.today().year  #saber o ano atual
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nsc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = atual - nsc  # saber qual a idade atualizada
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Das pessoas entrevistadas, \033[34;1m{}\033[m já são de maioridade.'.format(totmaior))
print('E e \033[32;1m{}\033[m ainda são de menoridade. '.format(totmenor))
