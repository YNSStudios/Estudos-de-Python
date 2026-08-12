velocidade = float(input('Digite sua velocidade de condução: '))
if velocidade <= 80: 
    print('Pode seguir, obrigado!')

else: 
    multa = (velocidade - 80) * 7
    print('Você será multado em: {}R$'.format(multa))