print('Aula 7 – Operadores Aritméticos \n'
      '     Nessa aula, vamos aprender quais são os operadores\n'
      'aritméticos do Python e também sua ordem de precedência\n'
      'dentro de expressões matemáticas. Veja como funcionam os\n'
      'operadores de adição, subtração, multiplicação, divisão,\n'
      'exponenciação e quociente na linguagem Python.!')

nome = input('Qual é o se nome ? ')
print('Prazer em te conhecer{:^20}'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma é {}, o pruduto é {} e a divisão é {}\n '.format(s, m, d), end='')
print('divisão inteira {} e potência {} '.format(di, e))