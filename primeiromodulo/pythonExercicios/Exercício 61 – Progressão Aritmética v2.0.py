print('\033[40;1;7mREFAÇA O DESAFIO 51, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA, MOSTRANDO OS 10 PRIMEIROS TERMOS '
      'DA PROGRESSÃO, USANDO A ESTRUTURA WHILE\033[m')
primeiro = int(input('Digite o Primeiro termo: '))
razão = int(input('Digite sua Razão: '))
termo = primeiro
contador = 1
while contador <= 10:
    print('{}  ➡️'.format(termo), end='')
    termo += razão
    contador += 1
print('\nFim')
