'''nome =str(input('Qual é o seu nome? '))
if nome == 'Junior':
    print('E ai Junior')
else :
    print('Qua pena volte depois')
print('Fim')'''
n1 = float(input('Digite uma nota : '))
n2 = float(input('Digite outra nota : '))
n = (n1 + n2)/2
print('A sua nota foi {:.2f}'.format(n))
if n >= 5.0:
    print('Sua média foi boa ! Aprovado.')
else:
    print('Sua média foi ruin! Seu burro.')
print('Fim')
