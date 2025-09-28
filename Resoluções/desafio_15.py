# Sistema de Pontuação para Jogo:
# Crie um sistema de pontuação para um jogo. O jogador recebe 100 pontos por cada inimigo derrotado e perde 50 pontos por cada vida perdida. 
# Se a pontuação final for negativa, ela deve ser zerada.
# O programa deve ler o número de inimigos derrotados e o número de vidas perdidas, e exibir a pontuação final.

inimigos_derrotados = int(input("Quantos inimigos foram derrotados: "))
vida_perdida = int(input("Vidas perdidas: "))

resultado = (inimigos_derrotados * 100) - (vida_perdida * 50)

if resultado < 0:
    print("Pontuação final: 0")
else:
    print(f"Sua pontuação foi de: {resultado}")