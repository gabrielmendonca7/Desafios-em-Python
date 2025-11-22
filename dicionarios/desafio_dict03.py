# Dado uma lista de dicionários, onde cada dicionário representa um produto com as chaves "nome", "preço"
# e "quantidade", crie um algoritmo que retorne o valor total do estoque. 
# Exemplo de entrada: [{'nome': 'maçã', 'preço': 2.0, 'quantidade': 5}, {'nome': 'banana', 'preço': 1.5, 'quantidade': 10}]
# Saída esperada: 25.0

estoque = [
    {'nome' : 'galaxy s25', 'preço' : 3.999, 'quantidade' : 8},
    {'nome' : 'iphone 16', 'preço' : 3.699, 'quantidade' : 10},
    {'nome' : 'galaxy book', 'preço' : 2.229, 'quantidade' : 5}
]

valor_em_estoque = 0

for x in estoque:
    valor_em_estoque += x['preço'] * x['quantidade']

print(f"O valor total em estoque é: R$ {valor_em_estoque}")