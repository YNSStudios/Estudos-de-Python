print("\033[0;31m=\033[0m\033[0;32m=\033[0m" * 10)
print("\033[0;35mLoja de emporios\033[0m")
print("\033[0;31m=\033[0m\033[0;32m=\033[0m" * 10)
valor = float(input("Digite o valor do Seu produto: "))
print("""Digite a forma de pagamento: 
[1] dinheiro/cheque
[2] boleto
[3] Cartão
apenas números.""")
pagamento = int(input("Digite seu método de pagamento: "))
if pagamento == 1:
    print("Você recebera 10% pelo pagamento á vista. ")
    desconto = valor - (valor * 0.10)
    print(f"O valor a pagar é de: \033[0;32m{desconto:.2f}R$.\033[0m")
elif pagamento == 2:
    prazo = int(input("Em quantas vezes você quer parcelar: "))
    valor_final = valor + ((valor * 0.06) * prazo)
    print(
        f"O valor final pago será de: {valor_final:.2f}R$ ou {prazo}X de {valor_final / prazo:.2f}R$."
    )
elif pagamento == 3:
    print(
        "Pagamentos á vista tem desconto de 5%, pagamentos em até 2X não tem acrescimos, e pagamentos acima de 3X tem juros de 6%. "
    )
    print("""Como você vai pagar: 
    [1] Á vista
    [2] até 2X 
    [3] 3X +
    """)
    while True:
        metodo = int(input("Digite sua escolha: "))
        if metodo == 1:
            desconto = valor - (valor * 0.05)
            print(f"O valor a pagar é de: \033[0;32m{desconto}R$.\033[0m")
            break
        elif metodo == 2:
            prazo = int(input("Digite em quantas vezes você quer: "))
            if prazo == 2:
                print(f"O valor a pagar é de: {valor / 2:.2f}R$ em 2 parcelas.")
                break
            elif prazo == 1:
                desconto = valor - (valor * 0.05)
                print(f"O valor a pagar é de: \033[0;32m{desconto:.2f}R$.\033[0m")
                break
            else:
                print("\033[0;31mNúmero de parcelas inválida !\033[0m")
        elif metodo == 3:
            print("Min 3X, Máx 24")
            prazo = int(input("Digite em quantas parcelas você vai pagar: "))
            if 3 <= prazo <= 24:
                valor_final = valor + ((valor * 0.06) * prazo)
                print(
                    f"O valor a pagar é de: {valor_final:.2f}, dividido em {prazo} parcelas de {valor_final / prazo:.2f}"
                )
                break
            else:
                print(
                    "\033[0;31mNúmero de parcelas inválida ou não condiz com o intervalo.\033[0m"
                )
