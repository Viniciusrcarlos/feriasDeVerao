#Desenvolva um programa que tenha uma função que verifique se um número inteiro qualquer é par ou impar
def calculo():
    calculo = numero%2
    if calculo == 0:
        print('Par')
    else:
        print('Impar')


numero = int((input('Digite um número para saber se é par ou impar: ')))
calculo()