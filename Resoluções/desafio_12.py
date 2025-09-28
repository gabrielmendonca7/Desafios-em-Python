# Cálculo de IMC:
# O Índice de Massa Corporal (IMC) é calculado pela fórmula: peso /(altura * altura). 
# Crie um programa que leia o peso e a altura de uma pessoa e classifique o resultado em:
# ○ Abaixo de 18.5: Abaixo do peso
# ○ Entre 18.5 e 24.9: Peso normal
# ○ Entre 25.0 e 29.9: Sobrepeso
# ○ Acima de 30.0: Obesidade

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

print(f"Seu IMC foi de: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 24.9:
    print("Peso normal")
elif imc < 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")
