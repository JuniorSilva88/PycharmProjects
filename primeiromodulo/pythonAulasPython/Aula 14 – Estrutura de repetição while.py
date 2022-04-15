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

for c in range(1, 3):  # laço no intervalo entre 1, 3
    n = int(input('Digite um valor: '))
print("fim")
n = 1
while n != 0:  # enaquanto n for diferente de 0, pede pra repetir a opção de digitar um nº
    n = int(input('Digite um valor: '))
print("fim")

r = 'S'
while r == 'S':  # enquanto a opção não for igual a S pede para repetir a operação e digitar novamente a opção. [S/N]
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')

n = 1
par = impar = 0
while n != 0:  # enquanto a opção for diferente de 0-(condição deparada), pede pra repetir a digitação de um valor n
    n = int(input('Digite um Valor: '))
    if n != 0:  # se a opção for diferente de 0-(condição de parada)
        if n % 2 == 0:  # verifica se a opção é par (divisivel por 2 com resto 0
            par += 1
        else:
            impar += 1
print("digitou {} nº pares {} nº impares ".format(par, impar))
