nome =  input('Digite seu nome: ').strip()
nome_1 = nome.find(' ')
print('''Seu nome com todas as letras minusculas fica: {}
Com todas as letras maiusculas fica: {}
O  total de letras é de: {}
É o total do primeiro nome é de: {}'''.format(nome.lower(), nome.upper(), len(nome) - nome.count(' '), nome_1))