#Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números maiores que 0.

contador = 0  # Contador para contar os múltiplos de 3
numero = 1    # Começamos com o número 1

while contador < 5:  # Repetir até encontrar 5 múltiplos
    if numero % 3 == 0:  # Verificar se o número é múltiplo de 3
        print(numero)
        contador += 1  # Incrementar o contador se for múltiplo
    numero += 1  # Passar para o próximo número

 
