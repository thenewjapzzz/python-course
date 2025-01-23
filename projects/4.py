'''
Cálculo IMC - Índice de Massa Corporal

- menor que 18.5 -> MAGREZA
- entre 18,5 e 24,9 -> NORMAL
- entre 25,0 e 29,9 -> SOBREPESO
- entre 30.0 e 39,9 -> OBESIDADE
- maior que 40 -> OBESIDADE GRAVE
'''

peso = float(input('Qual seu peso em kg: '))
altura = int(input('Qual sua altura em cm: '))

altura_em_m = altura / 100

imc = peso / (altura_em_m * altura_em_m)

if imc < 18.5:
    print('MAGREZA')
elif imc >= 18.5 and imc < 24.9:
    print('NORMAL')
elif imc >= 24.9 and imc < 29.9:
    print('SOBREPESO')
elif imc >= 29.9 and imc < 39.9:
    print('OBESIDADE')
else:
    print('OBESIDADE GRAVE')