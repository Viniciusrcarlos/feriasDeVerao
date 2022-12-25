import random

class simuladorDeDado:
    def __init__(self):
        self.valorMinimo = 1
        self.valorMaximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '
    def Iniciar(self):
        resposta = input(self.mensagem)
        if resposta == 'sim':
            self.gerarValorDoDado()


    def gerarValorDoDado(self):
        print(random.randint(self.valorMinimo, self.valorMaximo))

simulador = simuladorDeDado()
simulador.Iniciar()