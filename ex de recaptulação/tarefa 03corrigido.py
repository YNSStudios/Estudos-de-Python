print('=-=' * 8)
print('\033[0;36mAnalisador de Crédito\033[0m')
print('=-=' * 8)

salario = float(input('Digite o valor do seu salário: R$ '))
casa = float(input('Digite o valor da casa: R$ '))
meses = int(input('Digite em quantos meses você deseja pagar (máx - 120): '))

# Validação do limite de meses
if meses > 120 or meses <= 0:
    print('=-=' * 8)
    print('\033[1;31mPrazo inválido!\033[0m O número máximo de parcelas é 120.')
else:
    prestacao = casa / meses
    condicao = salario * 0.30

    if prestacao <= condicao:
        print('=-=' * 8)
        print('\033[1;32mEmpréstimo Aprovado!\033[0m')
        print('=-=' * 8)
        print(f'O valor da parcela é de: \033[0;32mR$ {prestacao:.2f}\033[0m')
        print(f'Limite máximo permitido da parcela: R$ {condicao:.2f}')
    else:
        print('=-=' * 8)
        print('\033[1;31mEmpréstimo Negado!\033[0m')
        print('=-=' * 8)
        print(f'A parcela de \033[1;31mR$ {prestacao:.2f}\033[0m excede o limite de 30% do seu salário (\033[0;32mR$ {condicao:.2f}\033[0m).')