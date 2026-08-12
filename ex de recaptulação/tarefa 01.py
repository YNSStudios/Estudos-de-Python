import random

ano_atual = 2026

nome = input('Digite seu nome completo: ')
nome_social = nome.split()[0]
print(f'óla {nome_social}.')

distancia = float(input('Digite a distancia da sua viajem. Apenas números: '))

print('Digite sua data de nascimento por etapas, dia, mês, e ano. Digite apenas números')
nasciemento_dia = int(input('Digite seu dia de nascimento: '))
nasciemento_mes = int(input('Digite seu mês de nascimento: '))
nasciemento_ano = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - nasciemento_ano

numero_cliente = random.randint(1000, 9999)

if distancia <= 200:
    if idade <=17:
        passaguem = distancia * 0.45
        desconto = (passaguem * 0.10) - passaguem
        print('=' * 20)
        print('\033[1;31;40mBILHETE DE EMBARQUE\033[0m.')
        print('=' * 20)
        print(f'Nome do passagueiro: \033[1;30;47m{nome}\033[0m.')        
        print(f'Tem Silva no nome: {'Sim' if 'silva' in nome.lower() else 'Não'}.')
        print(f'Data de nascimento: {nasciemento_dia}/{nasciemento_mes}/{nasciemento_ano}.')
        print(f'O total da passaguem para {distancia}KM é: \033[0;32;47m{desconto}\033[0m.')
        print(f'Status: \033[1;31;40mAprovado\033[0m.')

    else:
        passaguem = distancia * 0.45
        print('=' * 20)
        print('\033[1;31;40mBILHETE DE EMBARQUE\033[0m.')
        print('=' * 20)
        print(f'Nome do passagueiro: \033[1;30;47m{nome}\033[0m.')        
        print(f'Tem Silva no nome: {'Sim' if 'silva' in nome.lower() else 'Não'}.')
        print(f'Data de nascimento: {nasciemento_dia}/{nasciemento_mes}/{nasciemento_ano}.')
        print(f'O total da passaguem para {distancia}KM é: \033[0;32;47m{passaguem}\033[0m.')
        print(f'Status: \033[1;31;40mAprovado\033[0m.')

else:
    if idade <=17:
        passaguem = distancia * 0.50
        desconto = (passaguem * 0.10) - passaguem
        print('=' * 20)
        print('\033[1;31;40mBILHETE DE EMBARQUE\033[0m.')
        print('=' * 20)
        print(f'Nome do passagueiro: \033[1;30;47m{nome}\033[0m.')        
        print(f'Tem Silva no nome: {'Sim' if 'silva' in nome.lower() else 'Não'}.')
        print(f'Data de nascimento: {nasciemento_dia}/{nasciemento_mes}/{nasciemento_ano}.')
        print(f'O total da passaguem para {distancia}KM é: \033[0;32;47m{desconto}\033[0m.')
        print(f'Status: \033[1;31;40mAprovado\033[0m.')

    else:
        passaguem = distancia * 0.50
        print('=' * 20)
        print('\033[1;31;40mBILHETE DE EMBARQUE\033[0m.')
        print('=' * 20)
        print(f'Nome do passagueiro: \033[1;30;47m{nome}\033[0m.')        
        print(f'Tem Silva no nome: {'Sim' if 'silva' in nome.lower() else 'Não'}.')
        print(f'Data de nascimento: {nasciemento_dia}/{nasciemento_mes}/{nasciemento_ano}.')
        print(f'O total da passaguem para {distancia}KM é: \033[0;32;47m{passaguem}\033[0m.')
        print(f'Status: \033[1;31;40mAprovado\033[0m.')