# Escreva uma função chamada "conta_vogais" que receba uma string como parâmetro e retorne o número de vogais presentes nessa string.
# Considere que a string pode conter letras maiúsculas e minúsculas.

def conta_vogais(palavra:str):
    lista_vogais = ['a','e','i','o','u']
    contador = 0

    for vogal in lista_vogais:
        if vogal in palavra.lower():
            contador += 1
    return contador
    

nome_1 = "Gabriel"
nome_2 = "Corinthians"
nome_3 = "Mendonça"

print(f"O nome {nome_1} tem: {conta_vogais(nome_1)} vogais")
print(f"O nome {nome_2} tem: {conta_vogais(nome_2)} vogais")
print(f"O nome {nome_3} tem: {conta_vogais(nome_3)} vogais")