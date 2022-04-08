from time import sleep
print('''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) 
e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida''')
print('=-=' * 10)
peso = float(input('Digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso / (altura ** 2)
print('Processando ... ')
sleep(2)
print('=-=' * 10)
if imc < 18.5:
    print('Seu IMC é {:.2f}: VOCÊ ESTÁ \033[31;1mABAIXO DO PESO IDEAL.\033[m '.format(imc))
elif 18.5 <= imc <= 25:
    print('Seu IMC é {:.2f}: VOCÊ ESTÁ COM \033[32;1mPESO IDEAL.\033[m '.format(imc))
elif 25 <= imc <= 30:
    print('Seu IMC é {:.2f}: VOCÊ ESTÁ COM \033[33;1mSOBREPESO.\033[m '.format(imc))
elif 30 <= imc <= 40:
    print('Seu IMC é {:.2f}: VOCÊ ESTÁ COM \033[34;1mOBESIDADE.\033[m '.format(imc))
else:
    print('Seu IMC é {:.2f}: VOCÊ ESTÁ COM \033[35;1mOBESIDADE MÓRBIDA.\033[m '.format(imc))
print('=-=' * 10)
