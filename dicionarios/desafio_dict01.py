# Use um dicionário para armazenar informações sobre uma pessoa que você conheça.
# Armazene seu primeiro nome, o sobrenome, a idade e a cidade em que ela vive.
# Você deverá ter chaves como primeiro_nome, sobrenome, idade, e cidade. Por fim, mostre cada informação armazenada em seu dicionário.

informacoes = {}
informacoes["primeiro_nome"] = "Gabriel"
informacoes["sobrenome"] = "Mendonça"
informacoes["idade"] = 21
informacoes["cidade"] = "João Pessoa"

for key,value in informacoes.items():
    print(f"{key}: {value}")