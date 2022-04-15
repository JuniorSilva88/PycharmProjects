print('''CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TELADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO
DIGITAR O VALOR 999, QUE É A CONDIÇÃO DE PARADA. NO FINAL MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS, E QUAL FOI É 
A SOMA DELES, ( DESCONSIDERA O FLAG)''')
print('-=' * 20)
contador = total = soma = numero = 0
while True:
    numero = int(input('Digite um número. Se quiser parar digite [999]: '))
    if numero == 999:
        break
    contador += 1
    total += numero
print(f'A soma dos {contador} números digitados, é {total}!')
print('-=' * 20)
print('Fim ')
# na linha 5 não é necessário utilizar declarar essas variáveis,
# somente total = contador = 0
