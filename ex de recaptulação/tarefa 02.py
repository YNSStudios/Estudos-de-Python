gasolina = 5.80
alcool = 4.10

print('Digite qual conbustível você deseja')
tipo = input('Digite gasolina ou álcool: ').lower()

print('\033[1;31mDigite apenas números\033[0m')
litros = float(input('Digite quantos litros você deseja: '))

if tipo == 'gasolina':
    valor = litros * gasolina
    print(f'O total foi de: \033[0;32m{valor:.2f}\033[0mR$ ')

elif tipo == 'álcool':
    valor = litros * alcool
    print(f'O total foi de: \033[0;32m{valor:.2f}\033[0mR$ ')

else:
    print('\033[1;31mValor inválido !\033[0m')