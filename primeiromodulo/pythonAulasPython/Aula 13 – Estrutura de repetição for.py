print('''Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, 
que é uma estrutura versátil e simples de entender. Por exemplo:
for c in range(0, 4):
print(c)
print(‘Acabou’)''')
for c in range(1, 7): #ler até o nº6
    print('Hello')
print('The End')

for c in range(6, 0, -1): #ler do nº 6 até o nº 0
    print(c)

n = int(input('Digige um numero : '))
for c in range(0, n+1): # ler em ordem crescente a partir do nº digitado
    print(c)
print('Fim')

i = int(input('Início: '))
f = int(input(" Fim: "))
p = int(input(" passo: "))
for c in range(i, f+1, p):
    print(c)
print('Fim')

s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print('o somatorio de todos os valores {}'.format(s))