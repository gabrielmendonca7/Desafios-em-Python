# Escreva uma função chamada "converte_tempo" que receba um valor inteiro representando um tempo em segundos
# Retorne uma string formatada como "horas:minutos:segundos".

def converte_tempo(entrada):

    horas = entrada // 3600
    minutos = (entrada % 3600) // 60
    segundos = (entrada % 3600) % 60
    print(f"{horas}:{minutos}:{segundos}")


tempo = 7856
converte_tempo(tempo)