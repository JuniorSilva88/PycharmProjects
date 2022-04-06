from time import sleep
print('\033[1;32m Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.\n '
      'Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.\n '
      'A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.\033[m')
print('\033[31;4mJrBank\033[m')
print('-*-' * 10)
imovel = float(input('Qual o Valor do imóvel ? '))
salário = float(input('Qual sua renda mensal ? '))
ano = int(input('Em quantos anos será as parcelas do financiamento ? '))
parcela = ano * 12
financiamento = imovel / parcela
print('O valor do financiameto é de R$ \033[34;1m{:.2f}\033[m; '.format(financiamento))
print('-*-' * 10)
print('Processando proposta...')
sleep(3)
if financiamento <= (salário * 30) / 100:
    print('Seu financiamento foi \033[32;4mAPROVADO\033[m\n'
          'Com em \033[34;1m{:.0f}\033[m x de R$ \033[34;1m{:.2f}\033[m'.format(parcela,financiamento))
else :
    print('Seu financiamento foi \033[31;4mREPROVADO\033[m\n'
          'As parcelas ultrapassam os 30% permitido para liberação do financiameto.'.format(parcela))
