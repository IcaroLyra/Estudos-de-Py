# Mapas em Python (Dicionários)

# Dicionários são estruturas que armazenam pares chave:valor
# Representados por chaves {}

# Exemplo de dicionário:
receita = {"jan": 100, "fev": 250, "mar": 400}

# Iterando sobre dicionários
for chave in receita:
    print(chave)  # Exibe apenas as chaves

for chave in receita:
    print(receita[chave])  # Exibe os valores correspondentes

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')  # Exibe chave e valor formatados

# Acessando as chaves do dicionário
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores do dicionário
print(receita.values())

for valor in receita.values():
    print(valor)

# Exibindo o dicionário completo
print(receita)
