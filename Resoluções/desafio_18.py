# Análise de Risco de Investimento:
# Uma corretora de investimentos classifica o risco de uma aplicação com base em dois critérios:
# tempo de aplicação (curto: até 1 ano; longo:mais de 1 ano) e o tipo de investimento (renda fixa ou variável).
# ○ Baixo Risco: Renda fixa com aplicação longa.
# ○ Médio Risco: Renda fixa com aplicação curta ou Renda variável com aplicação longa.
# ○ Alto Risco: Renda variável com aplicação curta.
# Crie um programa que leia o tempo de aplicação e o tipo de investimento e
# classifique o risco. Use match-case aninhado, se possível.


tempo_investimento = int(input("Por quanto tempo deseja manter o investimento (Anos): "))
tipo_investimento = input("Tipo de investimento (Renda variável ou fixa): ")

match tipo_investimento:
    case "renda fixa":
        match tempo_investimento:
            case 1:
                print("Investimento de médio risco")
            case _:
                print("Investimento de baixo risco")
    case "renda variável":
        match tempo_investimento:
            case 1:
                print("Investimento de alto risco")
            case _:
                print("Investimento de médio risco")
            