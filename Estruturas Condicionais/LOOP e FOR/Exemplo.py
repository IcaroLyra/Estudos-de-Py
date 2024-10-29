"""
Loop-> Estrutura de repetição
For-> Uma dessas estruturas

for item in interavel:
   //execução do loop

Utilizamos loops para iterar sobre seguencias ou sobre valores interáveis

Exemplos de interáveis:
-String
-Lista
-Range
"""
nome = 'icaro'
lista = {1, 3, 5, 7, 9}
numeros = range(1, 10) # Temos que transforma em uma lista

# Exemplo de for 1 (Iterando em uma string)

for letra in nome:
  print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)

for numero in lista:
  print(numero)

# Exemplo de for 3 (Iterando sobre um range)
"""
range(Valor_inicial, Valor_Final)

OBS: O valor final não e inclusive
"""
for numero in range(1, 10):
  print(numero)

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num

print(f'A soma é {soma}')
