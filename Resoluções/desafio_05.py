# Verificação de Idade para Votação:
# Crie um programa que leia a idade de uma pessoa e determine se ela pode votar.
# A condição é: se a idade for maior ou igual a 16 anos, a pessoa pode votar. Imprima a mensagem correspondente.

idade = int(input("Digite sua idade: "))

if idade >= 16:
    print("Pode votar.")

else:
    print("Não pode votar.")