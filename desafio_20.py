# Classificação de Funcionários por Nível:
# Uma empresa precisa classificar seus funcionários por nível, baseando-se no tempo de casa (em anos) e na área de atuação.
# ○ Nível Júnior: Menos de 2 anos de casa, em qualquer área.
# ○ Nível Pleno: De 2 a 5 anos de casa, na área "Desenvolvimento" ou "Suporte".
# ○ Nível Sênior: Mais de 5 anos de casa, na área "Desenvolvimento".
# ○ Nível Especialista: Mais de 5 anos de casa, na área "Pesquisa".
# ○ Outro: Qualquer outra combinação.
# Crie um programa que leia o tempo de casa e a área de atuação do funcionário e imprima seu nível.

tempo_contrato = 3
area_atuacao = "Suporte"

if tempo_contrato < 2:
    print("Seu nível é: Júnior")

elif 2 <= tempo_contrato <= 5:

    if area_atuacao == "Desenvolvimento" or area_atuacao == "Suporte":
        print("Seu nível é: Pleno")
    else:
        print("Você é de outro nível.")

elif tempo_contrato > 5:

    if area_atuacao == "Desenvolvimento":
        print("Seu nível é: Sênior")
    elif area_atuacao == "Pesquisa":
        print("Seu nível é Especialista.")
    else:
        print("Você é de outro nível.")

else:
    print("Não foi possível obter dados.")