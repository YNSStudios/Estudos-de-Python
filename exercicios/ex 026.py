frase = input('Digite uma frase: ').strip()
frase = frase.lower()
print('''Na sua frase, o A aparece: {}
Pela primeira posição foi: {}
É a ultima foi: {}'''.format(frase.count('a'), frase.find('a') + 1, frase.rfind('a') + 1))