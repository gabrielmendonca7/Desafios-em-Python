# Ler um vetor A de 10 números. Após, ler mais um número e guardar em uma variável x.
# Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X.
# Logo após, imprimir o vetor M.


numeros = []
resultados = []
x = int(input("Digite um número para realizar a multiplicação: "))


for i in range(0,10):
    num = int(input("Digite um número para o vetor: "))
    numeros.append(num)
    resultados.append(num * x)

print(resultados)
