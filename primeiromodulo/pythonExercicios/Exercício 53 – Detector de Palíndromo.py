'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA,
O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA)
frase = str(input('Digite uma frase: ')).strip().upper()  # ler a frase e eliminar espaços
palavras = frase.split()  # splitar a frase lista
junto = ''.join(palavras)  # juntar a frase eliminar espaços
inverso = ''  # inverte a frase
for letra in range(len(junto) + 1, -1 - 1):  # inverter a frase
    inverso += junto[letra]
print('o inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('PALINDROMO')
else:
    print('NÃO É PALÍNDROMO')  # não funcionou, código igual ao do curso'''
print('')
frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('É PALÍNDROMO')
else:
    print('NÃO É PALÍNDROMO')  # funcionou corretamente com o fatiamento, com o for não deu certo
