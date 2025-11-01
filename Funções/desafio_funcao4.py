#Crie uma função chamada "verifica_primo" que receba um número inteiro como parâmetro e verifique se ele é um número primo.
# A função deve retornar True se o número for primo e False caso contrário.

def verifica_primo(numero):
    if numero <= 1:
        return False

    for num in range(2,numero):
        if numero % num == 0:
            return False
        
    return True

print(verifica_primo(2))
print(verifica_primo(7))
print(verifica_primo(5))
print(verifica_primo(9))
print(verifica_primo(25))
print(verifica_primo(11))

