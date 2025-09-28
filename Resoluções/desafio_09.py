# Cálculo de Juros Compostos:
# Uma pessoa aplicou um valor inicial em um investimento.
# Crie um programa que calcule o valor final após um determinado número de meses, comuma taxa de juros mensal constante.
# O programa deve ler o capital inicial, a taxa de juros e o número de meses, e exibir o valor final.

valor_presente = float(input("Valor que deseja investir: "))
TAXA_JUROS = float(input("Taxa de juros no periodo: "))
periodo = int(input("Número de meses em que deseja investir: "))

valor_futuro = valor_presente * ((1 + TAXA_JUROS)**periodo)
rendimento = valor_futuro - valor_presente

print(f"Seu investimento renderia: {rendimento:.2f} e ao todo daria: {valor_futuro:.2f}")