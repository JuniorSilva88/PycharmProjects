print('''Repetições em Python (while)
Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python. 
Por exemplo:
c=1 while c !=10:
print(c)
c+=1
print(‘Acabou’)''')
for c in range(1, 10):
    print(c, end=' ')
print('Fim')
c = 1
while c < 10:  # equanto contador for menor que 10
    print(c, end=' ')
    c = c + 1  # ou c+= 1
print('Fim')

for c in range(1, 3):
    n = int(input('Digite um valor: '))
print("fim")
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print("fim")

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um Valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("digitou {} nº pares {} nº impares ".format(par, impar))
