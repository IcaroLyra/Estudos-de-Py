#Faça um programa que receba dois números inteiros e mostre qual deles é o maior.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'O número maior é {n1}')
elif n2 > n1:
    print(f'O número maior é {n2}')
else:
    print('Os números são iguais')

