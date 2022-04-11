from time import sleep  # importação de biblioteca tempo
print('\033[36;1mContagem Regressiva\033[m ')
print('')
print('Preparando ⏲️')  # cronômetro fixo
print('')
for c in range(10, -1, -1):  # forma para contagem regressiva, de 10 ao 0
    sleep(1)
    print(c)
print('')
print('\033[33;1m🎆  🎆  🎆  🎆  🎆  🎆  🎆  🎆 \033[m')  # fogos de artifício

