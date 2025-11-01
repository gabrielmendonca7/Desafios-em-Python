# Crie uma função chamada "calcula_fatorial" que receba um número inteiro como parâmetro e retorne o seu fatorial.
# O fatorial de um número é o produto de todos os números inteiros de 1 até o próprio número.

def calcula_fatorial(numero):

    for x in range(1,numero):
        numero *= x  

    return numero
  


print(calcula_fatorial(5))
print(calcula_fatorial(10))
print(calcula_fatorial(13))
print(calcula_fatorial(20))