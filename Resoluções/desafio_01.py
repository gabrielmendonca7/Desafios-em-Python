# Cálculo de Desconto em E-commerce:
# Uma loja virtual oferece 10% de desconto em compras acima de R$ 100,00.
# Crie um programa que leia o valor total de uma compra e, usando uma estrutura condicional, calcule e exiba o valor final com o desconto, se aplicável.

valor_total = float(input("Valor da compra: "))

if valor_total > 100:
   print(f" Valor com desconto: {valor_total - (valor_total * 0.1)}")

else:
   print("Nessa compra não tem desconto")