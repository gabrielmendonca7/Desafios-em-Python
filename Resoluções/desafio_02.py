# Validação de Senha Simples:
# Desenvolva um programa que solicite ao usuário uma senha. 
# Se a senha for "Python123", imprima "Acesso concedido". Caso contrário, imprima "Acesso negado".


senha = str(input("Digite a senha de acesso: "))

if senha != "Python123":
    print("Acesso negado")
    
else:
    print("Acesso concedido")