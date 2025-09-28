# Simulação de Pedágio:
# Uma estrada de pedágio tem tarifas diferenciadas.
# Carros de passeio pagam R$ 5,50; caminhões pagam R$ 12,00.
# Crie um programa que, usando a estrutura match-case, leia o tipo de veículo ("carro" ou "caminhão") e calcule o valor a ser pago.

transporte = input("Qual o veículo (carro ou caminhão): ")
transporte.upper()

match transporte:
    case "caminhão":
        print("Tarifa de R$ 12,00 aplicada.")
    case "carro":
        print("Tarifa de R$ 5,50 aplicada.")
    case _:
        print("Tarifa padrão de R$ 5,00 aplicada.")

