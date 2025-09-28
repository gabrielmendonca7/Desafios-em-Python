# Conversor de Moeda:
# Crie um programa que converta um valor em Reais (R$) para Dólares Americanos (US$).
# A taxa de câmbio é uma constante.
# O programa deve receber o valor em R$ e exibir o valor convertido em US$.

DOLAR = 5.35

real = float(input("Quantos reais deseja converter? "))

conversor = DOLAR * real

print(f"Na conversão atual R${real} Reais, daria {conversor} Dólares.")