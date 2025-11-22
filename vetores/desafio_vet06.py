# Dado uma lista de números, crie um algoritmo que retorne a soma dos números pares na lista. 
# Exemplo de entrada: [1, 2, 3, 4, 5, 6] 
# Saída esperada: 12

numeros = [1,2,3,4,5,10]
numeros_pares = [x for x in numeros if x % 2 == 0]


if len(numeros_pares) > 0:
    print(f"A soma dos números pares é: {sum(numeros_pares)}")
else:
    print("A lista não contém número par")