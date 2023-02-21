#pedra papel e tesoura;

print("----------***----------")
print("    Jogo da velha")
print("----------***----------")
jogador1 = str(input("Jogador 1, digite sua ação: "))
jogador2 = str(input("Jogador 2, digite sua ação: "))

# pedra, papél e tesoura

if ((jogador1 == 'pedra') and (jogador2 == 'tesoura')):
    print('Jogador 1 ganhou')
if ((jogador1 == 'papel') and (jogador2 == 'tesoura')):
    print('Jogador 2 ganhou')
if ((jogador1 == 'tesoura') and (jogador2 == 'tesoura')):
    print('Empate')

if ((jogador1 == 'pedra') and (jogador2 == 'papel')):
    print('Jogador 2 ganhou')
if ((jogador1 == 'papel') and (jogador2 == 'papel')):
    print('Empate')
if ((jogador1 == 'tesoura') and (jogador2 == 'papel')):
    print('Jogador 1 ganhou')
