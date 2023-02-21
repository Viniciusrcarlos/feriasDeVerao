#Desenvolva um programa que tenha uma função que verifique se um número inteiro qualquer é par ou impar

numero = int(input('Digite um número: '))
parImpar = numero%2
if parImpar == 0:
    print('Par')
else:
    print('Impar')