salario = float(input('Digite seu salario: '))
casa_valor = float(input('Digite o valor da casa: '))
intervalo = int(input('Digite em quantos meses você vai pagar a casa. (Máx 480): '))

if 0 < intervalo <= 480:
    nome = input('Digite seu nome completo: ').strip()
    nome_1 = nome.split()[0]

    parcela = casa_valor / intervalo
    status = 'Aprovado' if parcela <= (salario * 0.30) else 'Negado'

    mensagem = (f'Parabéns, {nome_1}!' if status == 'Aprovado' else f'Sinto muito, {nome_1}. Tente novamente mais tarde.')

    print('--------------------------')
    print('Detalhamento do empréstimo')
    print('--------------------------')
    print(f'Nome: {nome.title()}')
    print(f'Valor da parcela por mês: R${parcela:.2f}')
    print(f'Status: {status}, {mensagem}')

else:
    print('\033[0;31;40mO número de meses excede o número fixado!\033[0m')