import random

class simuladorDeDado:
    def __init__(self):
        self.valorMinimo = 1
        self.valorMaximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '
    def Iniciar(self):
        resposta = input(self.mensagem)
        if resposta == 'sim' or resposta == 's':
            self.gerarValorDoDado()
        elif resposta == 'nao' or resposta == 'n':
            print('Obrigado, até mais.')
        else:
            print('Erro')


    def gerarValorDoDado(self):
        print(random.randint(self.valorMinimo, self.valorMaximo))

simulador = simuladorDeDado()
simulador.Iniciar()