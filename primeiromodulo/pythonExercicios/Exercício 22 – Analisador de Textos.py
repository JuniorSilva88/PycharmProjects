print('Crie um programa que leia o nome completo de uma pessoa e mostre:'
      '– O nome com todas as letras maiúsculas e minúsculas.'
      '– Quantas letras ao todo (sem considerar espaços).'
      '– Quantas letras tem o primeiro nome.')
nome = str(input('Digite um nome completo : ')).strip()
print('Seja bem vindo {}, Após analisar seu nome vemos que : '.format(nome))
print('Em letra maiúscula: {}'.format(nome.upper()))
print('Em letra minúscula: {}'.format(nome.lower()))
#print('Tem {} letras : '.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {}, e tem {} Letras.'.format(separa[0], len(separa[0])))
