salario = float(input('Digite o sálario: '))
if salario <= 3500:
    novo_salario = (salario * 0.15) + salario
    print(f'O novo sálario com o aumento fica: {novo_salario:.2f}R$')

else:
    novo_salario = (salario * 0.10) + salario
    print(f'O novo sálario com o aumento fica: {novo_salario:.2f}R$')