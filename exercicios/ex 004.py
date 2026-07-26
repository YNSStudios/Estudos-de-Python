a = input('digite algo ')
print('é um numero? ', a.isnumeric())
print('tem espaço? ', a.isspace())                           
print('É maiucusla? ', a.isupper())
print('É minucuslo? ', a.islower())
print(f'''Esta capitalizado ? {a.istitle()}
É alphanumerico ? {a.isalpha()} 
''')