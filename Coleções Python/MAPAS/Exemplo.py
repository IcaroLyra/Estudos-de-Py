"""
Mapas -> Conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves {}

# Iterar sobre dicionários

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

# Acessando as chaves
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores

print(receita.values())

for valor in receita.values():
  print(valor)

"""
receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)


