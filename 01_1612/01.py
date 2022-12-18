#Desenvolva um programa que tenha uma função que verifique se um número inteiro qualquer é par ou impar
numero = int
def calculo():
    calculo = numero/2
    if calculo == type(int):
        print('Par')
    elif calculo == type(float):
        print('Impar')


numero = (input('Digite um número para saber se é par ou impar: '))
print(numero)
calculo()