print('''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
Caso esteja errado, peça a digitação novamente até ter um valor corre''')
sexo = str(input('Qual seu sexo? [F/M] ')).strip().upper()[0]
while sexo not in 'MmFf':  # enquanto sexo for diferente
    sexo = str(input('Digite uma opção válida: ')).strip().upper()[0]  # repetir a solicitação
print('Sexo {} informado!'.format(sexo))
