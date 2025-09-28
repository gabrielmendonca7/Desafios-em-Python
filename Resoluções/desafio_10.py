# Aprovação de Crédito Bancário:
# Um banco analisa pedidos de crédito. 
# O critério de aprovação é: o valor da parcela não pode ultrapassar 30% da renda mensal do solicitante.
# Crie um programa que leia a renda mensal, o valor do empréstimo e o número de meses, e determine se o empréstimo pode ser concedido ou não.


renda_mensal = float(input("Digite sua renda mensal: "))
valor_emprestimo = float(input("Valor do emprestimo que necessita: "))
parcelas = int(input("Número de parcelas: "))

if valor_emprestimo / parcelas > renda_mensal * 0.3:
    print(f"Emprestimo não pode ser concedido pois ultrapassa 30% da sua renda mensal.")
    print(f"Valor da parcela: {valor_emprestimo / 12:.2f} | 30% da sua renda mensal: {renda_mensal * 0.3:.2f}")

else:
    print(f"Emprestimo pode ser concedido, pois a parcela fica abaixo dos 30% da sua renda mensal.")
    print(f"Valor da parcela: {valor_emprestimo / parcelas:.2f}")

