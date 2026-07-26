print('Digite seu nome, ele verificara se tem Silva ou não. ')
nome = input('Digite seu nome completo: ').strip()
print('silva' in nome[0:].lower() )