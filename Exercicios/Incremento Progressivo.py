#Aqui, você precisa declarar uma variável inteira e começar com o valor 0. 
# O programa deve incrementar essa variável em passos de 1000 e imprimir o valor atualizado a cada etapa. 
# O processo continua até que o valor da variável atinja 100000, momento em que o loop termina.

numero = 0  # Inicializa o número com 0

while numero <= 100000:  # Continua enquanto o número for menor ou igual a 100000
    print(numero)
    numero += 1000  # Incrementa o número em 1000 a cada iteração
