# Variáveis de exemplo
tem_convite = True  # True se a pessoa tem convite, False se não tem
idade = 19          # Idade da pessoa
acompanhado = False # True se está acompanhado de um responsável, False se não está

# Verificação das condições de acesso
if tem_convite and (idade >= 18 or acompanhado):
    print("Pode entrar no evento.")
else:
    print("Acesso negado.")
