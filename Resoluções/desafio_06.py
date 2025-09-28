# Sistema de Avaliação de Alunos:
# Se a nota for maior ou igual a 7,0, a situação é "Aprovado". Caso contrário, a situação é "Reprovado".
# Crie um programa que leia a nota e exiba a situação do aluno.

nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Aprovado")

else:
    print("Reprovado")