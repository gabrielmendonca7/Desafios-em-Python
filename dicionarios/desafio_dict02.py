# Use um dicionário para armazenar os números favoritos de algumas pessoas.
# Escolha cinco colegas, e pergunte quais seus número favoritos.
# Use seus nomes para serem as chaves de cada número favorito. Ao final, exiba o nome de cada pessoas e seu número favorito.

numero_favorito = {"Alê" : 7, "Jayne" : 10, "Lucas" : 6, "João" : 244, "Weslly" : 8}

for key,value in numero_favorito.items():
    print(f"O número favorito de {key} é {value}")
