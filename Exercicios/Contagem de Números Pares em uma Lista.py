valores = [int(input(f"Digite o valor {i+1}: ")) for i in range(10)]
pares = sum(1 for v in valores if v % 2 == 0)
print("Quantidade de valores pares:", pares)
