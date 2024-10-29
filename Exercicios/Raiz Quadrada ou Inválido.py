#Faça um programa que leia um número inteiro fornecido pelo usuário. 
# Se esse número for positivo, calcule a raiz quadrada do número e apresente-a. 
# Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
import math

n1 = int(input('Digite um numero:'))

if n1 >= 0:
  raiz = math.sqrt(n1)
  print(f'A raiz quadrada de {n1} e igual a {raiz:.2f}')

else :
  print('Número inválido, não é possível calcular a raiz quadrada de um número negativo.')

