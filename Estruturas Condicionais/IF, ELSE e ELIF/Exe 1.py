# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Verifica a faixa etária usando estruturas condicionais
if idade < 0:
    print("Idade inválida.")
elif idade <= 12:
    print("Você é uma Criança.")
elif idade <= 17:
    print("Você é um Adolescente.")
elif idade <= 64:
    print("Você é um Adulto.")
else:
    print("Você é um Idoso.")
