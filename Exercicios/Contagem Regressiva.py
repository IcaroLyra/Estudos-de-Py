#Faça um programa que utilize o comando while para mostrar na tela uma contagem 
# regressiva, iniciando em 10 e terminando em 0. 
# Mostre também uma mensagem "FIM!" após a contagem.

contador = 10  # Inicializa a contagem em 10

while contador >= 0:  # Continua enquanto o contador for maior ou igual a 0
    print(contador)
    contador -= 1  # Decrementa o contador em 1 a cada iteração

print("FIM!")  # Exibe "FIM!" após a contagem
