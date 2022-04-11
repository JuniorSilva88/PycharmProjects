print('Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.')
for c in range(1, 50 + 1):
    if c % 2 == 0:  # se o C for divisiveu por 2 forma que usa mais memória
        print(c, end=' ')
print(' Acabou ')
print(' ')
for n in range(2, 51, 2):  # código enchuto, mesmo resultado, menos da memória
    print(n, end=' ')
print(' Acabou ')
