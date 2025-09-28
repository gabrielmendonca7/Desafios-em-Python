# Determinação de Categoria de Produtos:
# Uma loja de eletrônicos precisa classificar seus produtos com base no preço e na categoria.
# ○ Se o preço for até R$ 500,00 e a categoria for "Acessórios", é um produto "Barato".
# ○ Se o preço for entre R$ 500,01 e R$ 2.000,00, é "Intermediário".
# ○ Se o preço for acima de R$ 2.000,00, é "Premium".
# ○ Se a categoria for diferente de "Acessórios", a regra de preço não se aplica e o produto é classificado como "Normal".
# Crie um programa que leia o preço e a categoria do produto e imprima a sua classificação.

preco = float(input("Digite o preço do seu produto: "))
categoria = input("Digite a categoria do seu produto: ")

if categoria != "acessórios":
    print("A classificação do seu produto é: Normal")

else:
    if preco <= 500:
        print("A classificação do seu produto é: Barato")

    elif preco <= 2000:
        print("A classificação do seu produto é: Intermediário")

    elif preco > 2000:
        print("A classificação do seu produto é: Premium")

