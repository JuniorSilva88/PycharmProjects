from time import sleep
print('''CRIE UM PROGRAMA QUE LEIA, IDADE, SEXO DE VÁRIAS PESSOAS. A CADA PESSOA CADASTRADA O PROGRAMA DEVERÁ PERGUNTAR,
SE O ÚSUÁRIO QUER OU NÃO CONTINUAR. NO FINAL MOSTRE:
A) => PESSOA MAIOR DE 18 ANOS:  B) => QUANTOS HOMENS FORAM CADASTRADOS: C) => QUANTAS MULHERES TEM MENOS DE 20 ANOS:''')
maioridade = homem = totmulher20 = 0
print('-*' * 10)
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digeite o sexo [F / M] ? ')).strip().upper()[0]
    if idade <= 18:
        maioridade += 1
    if sexo == 'M':
        homem += 1
    if sexo in 'Ff' and idade < 20:  # quais mulheres tem > 20 anos
        totmulher20 += 1
    ask = ' '
    while ask not in 'SN':
        ask = str(input('Quer continuar [S / N] ? ')).strip().upper()[0]
    if ask == 'N':
        break
    print('-*' * 10)
print('=-' * 10)
sleep(1)
print('ANALISANDO OS DADOS.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1.5)
print('.')
print(f'Temos {maioridade}, pessoas com 18 anos ou infeior: ')
print(f'Temos {homem}, pessoas do sexo Masculino: ')
print(f'Temos {totmulher20} mulheres com idade abaixo de 20 anos. ')
print('Fim')
