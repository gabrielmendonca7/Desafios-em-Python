# Verificação de Ano Bissexto:
# Crie um programa que leia um ano e determine se ele é um ano bissexto.
# Um ano é bissexto se for divisível por 4, exceto se for divisível por 100, a menos que também seja divisível por 400.

ano = int(input("Digite o ano que deseja verificar se é bissexto: "))

if ano % 4 == 0 or ano % 400 == 0:
    print(f"O ano de {ano} é bissexto")
else:
    print(f"O ano de {ano} não é bissexto")