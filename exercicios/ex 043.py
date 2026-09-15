print("Digite apenas números.")
peso = float(input("Digite seu peso (KG): "))
altura = float(input("digite sua altura(M): "))
imc = peso / (altura**2)

if imc < 18.5:
    print(f"Você está abaixo do peso: {imc:.2f}")

elif imc < 25:
    print(f"Você está no peso ideal: {imc:.2f}")

elif imc < 30:
    print(f"Você está em sobrepeso: {imc:.2f}")

elif imc < 40:
    print(f"Você está em obesidade: {imc:.2f}")

else:
    print(f"Você está em obesidade mórbida: {imc:.2f}")
