# Crie um vetor N que seja resultado da soma dos itens de outros dois vetores A e B.
#  Exemplo: A[0] + B[0] deverá ser salva em N[0].

vetor_a = [1,5,6,10,3,8]
vetor_b = [2,5,3,10,5,2]
vetor_n = []

if len(vetor_a) == len(vetor_b):
    for i in range(len(vetor_a)):
        vetor_n.append(vetor_a[i] + vetor_b[i])
else:
    print("Os dois vetores tem tamanho distinto.")


print(vetor_n)