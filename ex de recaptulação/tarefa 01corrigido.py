import random

ano_atual = 2026

# 1. ENTRADA DE DADOS
nome = input('Digite seu nome completo: ').strip()
nome_social = nome.split()[0]
print(f'Olá {nome_social}!')

distancia = float(input('Digite a distância da sua viagem (em KM): '))

print('Digite sua data de nascimento por etapas (apenas números):')
nascimento_dia = int(input('Dia: '))
nascimento_mes = int(input('Mês: '))
nascimento_ano = int(input('Ano: '))
idade = ano_atual - nascimento_ano

numero_cliente = random.randint(1000, 9999)

# 2. PROCESSAMENTO 
# Define o preço base por distância
if distancia <= 200:
    preco_passagem = distancia * 0.50
else:
    preco_passagem = distancia * 0.45

# Verifica a regra de idade para desconto e status
if idade < 18:
    preco_final = preco_passagem * 0.90 # Aplica 10% de desconto
    status = "\033[1;33;40mAutorização dos pais necessária\033[0m"
else:
    preco_final = preco_passagem # Preço cheio
    status = "\033[1;32;40mEmbarque Aprovado\033[0m"

# 3. SAÍDA DE DADOS 
print('\n' + '=' * 40)
print('\033[1;31;40m          BILHETE DE EMBARQUE          \033[0m')
print('=' * 40)
print(f'Bilhete Nº: \033[1;33m{numero_cliente}\033[0m')
print(f'Passageiro: \033[1;30;47m{nome}\033[0m')        
print(f'Sobrenome Silva: {"Sim" if "silva" in nome.lower() else "Não"}')
print(f'Nascimento: {nascimento_dia}/{nascimento_mes}/{nascimento_ano} ({idade} anos)')
print(f'Distância: {distancia} KM')
print(f'Total pago: \033[0;32;47mR$ {preco_final:.2f}\033[0m')
print(f'Status: {status}')
print('=' * 40)