gasolina = 5.80
alcool = 4.10

print('\033[1;36m=== POSTO DE COMBUSTÍVEL ===\033[0m')
tipo = input('Digite qual combustível deseja [Gasolina/Álcool]: ').strip().lower()

if tipo in 'gasolina álcool alcool':
    litros = float(input('Digite quantos litros você deseja: '))
    
    if tipo == 'gasolina':
        valor = litros * gasolina
    else:
        valor = litros * alcool
        
    print(f'O total a pagar é: \033[0;32mR${valor:.2f}\033[0mR$')
    
else:
    print('\033[1;31mOpção inválida! Escolha apenas Gasolina ou Álcool.\033[0m')