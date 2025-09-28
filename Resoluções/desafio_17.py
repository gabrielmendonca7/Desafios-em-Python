# Cálculo de Preço de Passagem Aérea:
# Uma agência de viagens precisa calcular o preço de uma passagem.
# Se a distância da viagem for até 200 km, o preço por km é de R$ 0,50.
# Se for acima de 200 km, o preço por km é de R$ 0,45. Crie um programa que leia a distância e exiba o valor da passagem.


distancia = int(input("Qual a distância da sua viagem: "))

if distancia <= 200:
    print(f"O preço da sua passagem ficou em: {distancia * 0.50:.2f}")
else:
    print(f"O preço da sua passagem ficou em: {distancia * 0.45:.2f}")