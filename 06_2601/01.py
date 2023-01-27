#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista = []

i = 0
while i < 5:
    lista.append(int(input('digite um número: ')))
    i = i + 1
print(lista[0], lista[1], lista[2], lista[3], lista[4])
