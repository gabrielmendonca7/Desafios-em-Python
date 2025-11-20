# Escreva um algoritmo que permita a leitura das notas de uma turma de 5 alunos. Depois responda:
# a. Qual a média da turma?
# b. Quantos alunos obtiveram nota acima da média da turma?
# c. Imprimir a média da turma e o resultado da contagem.

def media(nota:list):
    return sum(nota) / len(nota)

def alunos_acima(nota:list):
    contador = 0

    for x in nota:
        if x > media(nota):
            contador += 1
    return contador

notas = []

for n in range(1,6):
    aluno = float(input(f"Digite a nota do aluno {n}: "))
    notas.append(aluno)

print(f"{media(notas):.2f}")
print(alunos_acima(notas))
print(f"A média da turma foi: {media(notas):.2f} e a quantidade de alunos com nota maior que a média foi: {alunos_acima(notas)}")