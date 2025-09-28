# Cálculo de Salário Líquido:
# Uma empresa precisa calcular o salário líquido de seus funcionários.
# O cálculo é feito subtraindo 15% de imposto de renda do salário bruto.
# Escreva um programa que receba o salário bruto e imprima o salário líquido.

salario_bruto = float(input("Qual o seu salário? "))
salario_liquido = salario_bruto - (salario_bruto * 0.15)

print(f"Seu salário bruto é de R${salario_bruto} e o seu líquido é de R${salario_liquido}")