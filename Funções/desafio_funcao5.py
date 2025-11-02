# Escreva uma função chamada "encontra_palavras" que receba uma lista de palavras e uma letra como parâmetros
# E retorne uma nova lista contendo apenas as palavras que começam com a letra fornecida.

def encontra_palavras(lista:list, letra:str):

    palavras_encontradas = []

    for palavra in lista:
        if palavra[0].lower() == letra.lower():
            palavras_encontradas.append(palavra)

    if len(palavras_encontradas) >= 1:
        for encontrado in palavras_encontradas:
            print(encontrado)
    else:
        print("Nenhuma palavra encontrada")


palavras = ["C#", "C++", "Java", "JavaScript", "HTML", "CSS", "Ruby", "SQL", "Json", "Python", "PHP", "PostgreSQL"]

letra = "C"
encontra_palavras(palavras,letra)