#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa
# Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso em Kg: '))
alt = float(input('Digite sua altura em m: '))
imc = peso / (alt ** 2)
print('Seu IMC é: {:.2f}'.format(imc))
if imc <= 18.5:
    print('Cuidado você está Abaixo do peso.')
elif imc <= 25:
    print('Parabêns você está com Peso ideal.')
elif imc <= 30:
    print('Você esta com Sobrepeso')
elif imc <=40:
    print('Atenção você esta Obeso.')
else:
    print('CUIDADO OBESIDADE MORBIDA')
