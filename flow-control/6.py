# Enviar email com os detalhes de compra online (Máxixo 3 tentativas)
# para compras confirmadas

compra_confirmada = True
dados_compra = 'Compra no valor de R$12,50 entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para seu email')
        break
else:
    print('Falha na compra')