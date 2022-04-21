from time import sleep
print('''CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODTOS. O PROGRAMA DEVE PERGUNTAR SE O USUÁRIO VAI 
CONTINUAR, NO FINAL MOSTRAR: 
A) => QUAL TOTAL DE GASTO NA COMPRA: B) => QUATOS PRODUTOS CUSTAMA MAIS DE R$ 1.000,00:  C) => QUAL O NOME DO PRODUTO 
MAIS BARATO: ''')
total = produto1mil = valor = menor = contador = 0
barato = ' '
print('{:=^25}'.format(' MERCADO JR '))
while True:
    iten = str(input('Nome item: ')).strip().upper()
    valor = float(input('Preço do item? R$ '))
    contador += 1
    total += valor
    if valor > 1000:
        produto1mil += 1
    if contador == 1 or valor < menor:  # modo simplificado
        menor = valor
        barato = iten
    # else:  modo robusto
    #  if valor < menor:
    #  menor = valor
    #  barato = iten
    ask = ' '
    while ask not in 'SN':
        ask = str(input('Quer continuar [S / N] ? ')).strip().upper()[0]
    if ask == 'N':
        break
print('{:-^30}'.format('CALCULANDO COMPRA'), end='')
sleep(1)
print('-', end='')
sleep(1)
print('-', end='')
sleep(1.5)
print('-')
print(f'Total da compra ficou em R${total:10.2f} ')
print(f'temos {produto1mil} iten tem valor acima de R$ 1.000,00: ')
print(f'E o Item de menor valor é o {barato} que custa R${menor:10.2f}.')
