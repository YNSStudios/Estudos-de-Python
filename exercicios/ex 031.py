destinos = {
    'porto seguro': 180,
    'canavieiras': 300,
    'ilhéus': 190,
    'salvador': 150
}

print('Porto Seguro, Canavieiras, Ilhéus, Salvador.')
cidade = input('Para onde você quer ir: ').strip()
escolha = cidade.lower()
if escolha in destinos:
    distancia = destinos[escolha]
    
    if distancia <= 200:
        passagem = distancia * 0.45

        print('O valor da sua passagem é de: R${:.2f}.'.format(passagem))

    else:
        passagem = distancia * 0.50
        print('O valor da sua passagem é de: R${:.2f}.'.format(passagem))

else:
    print('Destino inválido!')