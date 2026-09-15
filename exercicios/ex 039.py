nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if idade <= 17:
    print(f'Você ainda vai se alistar. Faltam {18 - idade} para se alistar.')

elif idade >= 18:
    print('Você deve se alistar.')

elif 20 <= idade <= 30:
    print('já passou a hora de se alistar.')

elif 31 <= idade <= 44:
    print('\033[0;31;40mComparessa a uma junta militar urgentemente.\003[0m')

else:
    print('Você não precisa fazer, sua idade já se isenta.')