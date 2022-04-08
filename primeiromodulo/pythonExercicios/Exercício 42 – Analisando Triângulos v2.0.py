print('''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– \033[32;1mEQUILÁTERO\033[m: todos os lados iguais
– \033[34;1mISÓSCELES\033[m: dois lados iguais, um diferente
– \033[33;1mESCALENO\033[m: todos os lados diferentes''')
print('~'*50)
a = float(input('Digite o valor de Seguimento A: '))
b = float(input('Digite o valor de Seguimento B: '))
c = float(input('Digite o valor de Seguimento C: '))
if a < b + c and b < a + c and c < b + a:
    print('a soma dos seguimentos A, B e C: PODEM formar um Triângulo ', end='')  # end = junção das linhas
    if a == b == c:
        print('\033[32;1mEQUILÁTERO.\033[m')
    elif a != b != c != a:
        print('\033[33;1mESCALENO.\033[m')
    else:
        print('\033[34;1mISÓSCELES.\033[m')
else:
    print('A soma dos seguimentos A, B e C: \033[31;4;1mNÃO PODEM\033[m formar um Triângulo. ')
