# Calculadora Simples:
# Desenvolva uma calculadora que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números.
# O programa deve solicitar a operação desejada ao usuário e, usando a estrutura if/elif/else, 
# executar a operação e exibir o resultado.

number_1 = float(input("Digite o primeiro número: "))
number_2 = float(input("Digite o segundo número: "))

print()
print("Qual operação deseja realizar com os dois números: ")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

print()
escolha = int(input("Digite o número da opção: "))

if escolha == 1:
    print(f"{number_1} + {number_2} = {number_1 + number_2}")
elif escolha == 2:
    print(f"{number_1} - {number_2} = {number_1 - number_2}")
elif escolha == 3:
    print(f"{number_1} * {number_2} = {number_1 * number_2}")
elif escolha == 4:
    print(f"{number_1} / {number_2} = {number_1 / number_2}")
else:
    print("Opção invalida")