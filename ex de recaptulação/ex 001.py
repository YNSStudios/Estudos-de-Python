#Etrada
nome = str(input('Digite seu nome: ')).strip()
idade = int(input('Digite sua idade: '))
comfirmacao = input(f'olá {nome}, você tem {idade} anos certo ? (sim ou não): ').strip()
#Processamento
if comfirmacao.lower == "sim":
    print("Ok, obrigado por participar!")
else:
    idade = int(input('Digite sua idade: '))
    print(f'sua idade é {idade}. obrigado por participar')