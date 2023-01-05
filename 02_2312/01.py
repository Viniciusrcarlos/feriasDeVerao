numeros = []

while True:
    numeros.append(int(input('Dig um num: ')))
    conf = str(input("cont?"))
    if conf == 's':
        continue
    elif conf == 'n':
        break

print(numeros)