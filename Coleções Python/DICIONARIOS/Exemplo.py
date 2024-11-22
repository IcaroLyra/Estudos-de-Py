"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

print(type({}))

OBS: Sobre dicionários
- Chave e valor são separados por dois pontos 'chave:valor';
- Tanto chave quanto valor podem ser de qualquer tipo de dado;
- Podemos misturar tipos de dados;
"""

# Criação de dicionários

# Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 (Menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
# print(paises['ru'])  # Caso a chave 'ru' não exista, o código lança um KeyError

# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendada
print(paises.get('br'))  # Saída: Brasil
print(paises.get('ru'))  # Saída: None

# Podemos definir um valor padrão para caso não encontremos a chave informada
pais = paises.get('ru', 'Não encontrado')
print(f'Encontrei o país {pais}')  # Saída: Encontrei o país Não encontrado

# Verificando se um país existe antes de tentar acessá-lo
pais = paises.get('ru')
if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

# Verificar se determinada chave se encontra em um dicionário
print('br' in paises)  # Saída: True
print('ru' in paises)  # Saída: False
print('Estados Unidos' in paises)  # Saída: False (chaves e valores são diferentes)

# Exemplo de condicional para verificar e acessar
if 'ru' in paises:
    russia = paises['ru']  # Este trecho só será executado se 'ru' estiver em paises

# Outro exemplo de adicionar um país ao dicionário
paises['ru'] = 'Rússia'
print(paises)  # Adiciona uma nova entrada ao dicionário

"""
Resumo das vantagens dos dicionários:
- Permite acesso rápido aos valores através das chaves.
- Flexibilidade de tipos para chaves e valores.
- Podem ser modificados facilmente (adicionar, atualizar ou remover elementos).
"""
