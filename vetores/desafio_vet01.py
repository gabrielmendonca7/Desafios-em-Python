# Escreva um algoritmo que permita a leitura dos nomes de 5 clubes de futebol e armazene os nomes lidos em um vetor.
# Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI,
# se o nome estiver entre os 5 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.


def buscador(lista:list, buscar_time:str):
        
    if buscar_time.lower() in lista:
        print("ACHEI")
    else:
        print("NÃO ACHEI")

times = []

for time in range(1,6):
    clube = input(f"Digite o nome do time {time}: ")
    times.append(clube)

print()
padrao_nomes_times = [item.lower() for item in times]
time_desejado = input("Digite o nome do time que deseja: ").lower()

buscador(padrao_nomes_times,time_desejado)