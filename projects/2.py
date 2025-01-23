'''
Criar um programa que calcula a quantidade de tinta necessária
para pintar uma parede. O usuário deverá fornecer as seguintes 
informações: Rendimento, altura, largura
O programa deve mostrar na tela a mensagem 'Você necessita de x 
latas de tinta'
'''

def tinta_necessaria(rendimento, altura, largura):
    area = altura * largura
    qnt_latas = -(-area / rendimento)
    return qnt_latas
    
rendimento = int(input('Qual é o rendimento da lata: '))
altura = int(input('Qual a altura da parede: '))
largura = int(input('Qual é a largura da parede: '))

resultado = tinta_necessaria(rendimento, altura, largura)

print(f'Você necessita de {resultado} latas de tinta')