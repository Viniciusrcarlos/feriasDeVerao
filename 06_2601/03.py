#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

i = 0
while i < 4:
    notas.append(int(input('Digite a nota: ')))
    i = i + 1
print(len(notas))