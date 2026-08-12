print('=-=' * 8)
print('\033[0;36mAnalisador de Crédito\033[0m')
print('=-=' * 8)

salario = float(input('Digite o valor do seu salário: '))
casa = float(input('Digite o valor da casa: '))
meses = int(input('Digite em quantos meses você deseja pagar. (máx - 120): '))

prestacao = casa / meses
condicao = salario * 0.30

if prestacao <= condicao:
    print('=-=' * 8)
    print('\033[1;32mEmpréstimo aprovádo\033[0m')
    print('=-=' * 8)
    print(f'O valor da parcela é de: \033[0;32m{prestacao:.2f}\033[0mR$')

else:
    print('=-=' * 8)
    print('\033[1;31mEmpréstimo negado\033[0m')
    print('=-=' * 8)
    print('O valor das parcelas ecendem o mínimo esperado para o pagamento')