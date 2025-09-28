# Cálculo de Aumento Salarial:
# Uma empresa vai dar um aumento para seus funcionários.
# Se o salário for até R$ 1.500,00, o aumento é de 20%.
# Se for entre R$ 1.501,00 e R$ 2.500,00, o aumento é de 15%.
# Se for acima de R$ 2.500,00, o aumento é de 10%.
# Crie um programa que leia o salário atual e exiba o novo salário.

salario_atual = 5000

if salario_atual <= 1500:
    salario_atual += (salario_atual * 0.2)

elif salario_atual >= 1501 and salario_atual <= 2500:
    salario_atual += (salario_atual * 0.15)

elif salario_atual > 2500:
    salario_atual += (salario_atual * 0.10)


print(f"Seu salário atual é de: {salario_atual:.2f}")