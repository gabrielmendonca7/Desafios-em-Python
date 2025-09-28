# Classificação de Triângulos:
# Crie um programa que leia o comprimento de três lados de um triângulo e determine se ele é equilátero, isósceles ou escaleno.
# Lembre-se: equilátero (três lados iguais), isósceles (dois lados iguais) e escaleno (três lados diferentes).

lado_1 = float(input("Digite o primeiro lado do triângulo: "))
lado_2 = float(input("Digite o segundo lado do triângulo: "))
lado_3 = float(input("Digite o terceiro lado do triângulo: "))

if lado_1 == lado_2 == lado_3:
    print("Triângulo equilátero")

elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    print("Triângulo isósceles")

else:
    print("Triângulo escaleno")