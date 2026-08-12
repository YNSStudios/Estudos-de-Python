print('='*14)
print('\033[1;32;40mCalculadora\033[0m')
print('='*14)
print('\033[0;31;40mDigite apenas o numero equivalente a questao.\033[0m')
print('Escolha uma das opcoes: ')
print('''[1] Desconto
[2] Passagem
[3] Conversao de Temperatura
[4] Media
[5] Conversao de moedas

''')

escolha = int(input('Escolha: '))
if escolha == 1:

    print('O que voce vai manipular ? Aumento, Subtracao ou porcentagem ?')
    escolha = input('Escolha: ')

    if escolha.lower() == 'aumento':

        produto = float(input('Digite o valor do produto: '))
        desconto = float(input('Digite o valor da porcentagem do aumento: '))
        valor = (produto * (desconto / 100)) + produto
        print(f'O produto com o reajuste fica: \033[1;32m{valor}\033[0mR$.')

    elif escolha.lower() in ['subtracao', 'subtraçao', 'subtração', 'desconto']:

        produto = float(input('Digite o valor do produto: '))
        desconto = float(input('Digite o valor da porcentagem do desconto: '))
        valor = produto - (produto * (desconto / 100))
        print(f'O produto com o reajuste fica: \033[1;32m{valor}\033[0mR$.')

    elif escolha.lower() in ['porcentagem', 'porcentaguem']:

        produto = float(input('Digite o valor do produto: '))
        porcentagem = float(input('Digite a porcentagem desejada: '))
        valor = produto * (porcentagem / 100)
        print(f'O produto com o reajuste fica: \033[1;32m{valor}\033[0mR$.')

    else:
        print('\033[1;31;40mEscolha invalida !\033[0m')

elif escolha == 2:

    nome = input('Digite seu nome completo: ')
    idade = int(input('Digite sua idade: '))

    if idade <= 17:
        desconto = 0.15
        status = '\033[0;31;40mNecessario permissao do responsavel\033[0m'

    else:
        desconto = 0
        status = '\033[0;32;40mAprovado\033[0m'

    km = 0.1745

    print('''Sua viagem e:

    [1]Metropolitanas (Cidades vizinhas)
    [2]Viagens Intermunicipais (Dentro do mesmo estado)
    [3]Viagens Interestaduais (Para outro estado)
    Digite apenas o numero.''')

    viagem = int(input('Escolha: '))
    distancia = float(input('Digite a distancia entre seu local atual e a cidade de destino: '))
    
    while True:
        if viagem == 1:
            taxa = 1.50
            break
        elif viagem == 2:
            taxa = 3.75
            break
        elif viagem == 3:
            taxa = 9.08
            break
        else:
            print('\033[0;31;40mEscolha invalida\033[0m')
            viagem = int(input('Escolha novamente ! '))

    valor_bruto = (distancia * km) + taxa
    valor = valor_bruto - (valor_bruto * desconto)

    print('=-' * 8)
    print('Passagem')
    print('=-' * 8)
    print(f'''Nome: {nome.title()}.
Passagem: \033[0;32m{valor:.2f}\033[0mR$.
Desconto: {f'Sim, no valor de {desconto * 100:.0f}%' if idade <= 17 else 'Nao'}
Status: {status}
''')

elif escolha == 3:
    print('''Escolha uma opção: 
    [1] Celsius. 
    [2] Kelvin
    [3] Fahrenheit
    ''')

    while True:
        print('\033[0;31mDigite apenas números.\033[0m')
        entrada = int(input('Digite sua escolha: '))
        medida = float(input('Digite a quantidade de graus: '))
        saida = int(input('Digite para qual vai converter: '))
        
        if entrada == 1:
            if saida == 2:
                conversao = medida + 273.15 
                status = 'k'
                break

            elif saida == 3:
                conversao = (medida * 9/5) + 32
                status = '°F'
                break

            else:
                print('\033[1;31;40mEscolhas fora da lista ou que sejam iguais, não podem ser selecionadas.\033[0m')
                
        elif entrada == 2:
            if saida == 1:
                conversao = medida - 273.15
                status = '°C'
                break

            elif saida == 3:
                conversao = (medida - 273.15) * 9/5 + 32
                status = '°F'
                break

            else:
                print('\033[1;31;40mEscolhas fora da lista ou que sejam iguais, não podem ser selecionadas.\033[0m')
                entrada = int(input('Digite sua escolha: '))
                saida = int(input('Digite para qual vai converter: '))

        elif entrada == 3:
            if saida == 1:
                conversao = (medida - 32) * 5/9
                status = '°C'
                break

            elif saida == 2:
                conversao = (medida - 32) * 5/9 + 273.15
                status = 'K'
                break

            else:
                print('\033[1;31;40mEscolhas fora da lista ou que sejam iguais, não podem ser selecionadas.\033[0m')
                entrada = int(input('Digite sua escolha: '))
                saida = int(input('Digite para qual vai converter: '))

        else:
            print('\033[1;31;40mEscolhas fora da lista ou que sejam iguais, não podem ser selecionadas.\033[0m')
            entrada = int(input('Digite para qual vai converter: '))

    print(f'A conversão da temperatuda da: {conversao:.2f} {status}. ')

elif escolha == 4:
    lista = []

    valores = int(input('Quantos valores você tem para calcular a média: '))
    nome = input('Deseja adicionar nome aos valores ? [sim] [não]. ')

    while True:
        if nome.lower() == ['sim', 's']:
            for i in range(valores):
                nome_item = input(f'[{i + 1}]Digite o nome o nome: ')
                valor = float(input('Digite o valor: '))
                lista.append({'nome': nome_item, 'valor': valor})

            total = sum(item['valor'] for item in lista)
            media = total / valores
            break

        elif nome.lower() in ['não', 'nao', 'n']:
            for i in range(valores):
                valor = float(input(f'[{i + 1}]Digite o valor: '))
                lista.append(valor)

            media = sum(lista) / valores
            break

        else:
            print('\033[031mValor inválido, tente novamente! \033[0m')
            nome = input('Deseja adicionar nomes aos valoes ?: ')

    if media is not None:
        print(f'A média dos valores é: {media:.2f}')

elif escolha == 5:
    lista = {'real': 1,
             'euro': 5.89,
             'dolar': 5.09,
             'libra': 6.87,
             'peso': 294.80,
             'franco': 6.29,
             'btc': 330310.30} 

    cifrao = {'real': 'R$',
              'euro': '€',
             'dolar': '$',
             'libra': '£',
             'peso': 'PS$',
             'franco': 'FR$',
             'btc': '$BTC$'}

    print('''Esolha a sua moeda: 
    Real
    Euro
    Dolar
    Franco
    Libra
    Peso
    BTC
    ''')

    moeda = input('Escolha: ').strip().lower()
    if moeda in lista:

        valor = float(input('Digite a quantidade: '))
        moeda_saida = input('Para qual moeda: ').strip().lower()

        if moeda_saida in lista:

            entrada = lista[moeda] * valor
            saida = entrada / lista[moeda_saida]
        
            print(f'A conversão deu: {saida:.2f}{cifrao[moeda_saida]}.')
        else:
            print('\033[01;31mEsclha inválida !\033[0m')
    else:
        print('\033[01;31mEsclha inválida !\033[0m')
        
else:
    print('\033[01;31mEsclha inválida !\033[0m')