import random

#classe que gerencia o jogo da memória
class JogoDaMemoria:
    def _init_(self):
#lista de caracteres especiais, cada um duplicado para formar pares
        caracteres = ['@', '#', '$', '%', '&0', '*', '!', '?']
        #cria as cartas, duas de cada caractere
        cartas = [Carta(c) for c in caracteres for _ in range (2)]
#embaralha as cartas para distribuir aleatoriamente
        random.shuffle(cartas)
#cria uma grade 4x4 com as cartas embaralhadas
        self.tabuleiro = [cartas[i*4:(i=1)*4] for i in range(4)]