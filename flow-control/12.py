valor = int(input('Digite o valor do produto em R$: '))

while valor >= 20:
    valor = (valor * 0.1) + valor
    print(f'Valor: R${valor}')
    break