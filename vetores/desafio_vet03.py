# Ler um vetor Q de 10 posições (aceitar somente números positivos). Escrever a seguir:
# Dica: você pode pesquisar pela biblioteca randint para criar os valores de forma aleatória.
# a. o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
# b. o valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;


def maior(lista:list):
    maior_numero = max(lista)
    posicao = lista.index(maior_numero)
    print(f"O maior número é: {maior_numero} e sua posição é a {posicao}")

def menor(lista:list):
    menor_numero = min(lista)
    posicao = lista.index(menor_numero)
    print(f"O menor número é: {menor_numero} e sua posição é a {posicao}")

numeros = []

for x in range(1,11):

    while True:
        num = int(input(f"Digite um número ({x}): "))

        if num >= 0:
            numeros.append(num)
            break
        else:
            print("Apenas positivos")

maior(numeros)
menor(numeros)