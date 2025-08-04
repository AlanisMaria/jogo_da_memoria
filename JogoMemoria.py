import random
from carta import Carta
import time

            
#classe que gerencia o jogo da memória
class JogoDaMemoria:
    def __init__(self):
#lista de caracteres especiais, cada um duplicado para formar pares
        caracteres = ['@', '#', '$', '%', '&', '*', '!', '?']
        #cria as cartas, duas de cada caractere
        cartas = [Carta(c) for c in caracteres for _ in range (2)]
#embaralha as cartas para distribuir aleatoriamente
        random.shuffle(cartas)
#cria uma grade 4x4 com as cartas embaralhadas
        self.tabuleiro = [cartas[i*4:(i+1)*4] for i in range(4)]
        self.pontuacao = 0 #pontuação do jogador (quantos pares encontrou)
        self.cartas_viradas = [] #lista para guardar as cartas viradas atualmente

    def exibir_tabuleiro(self):
        #metodo para mostrar o estado atual do tabuleiro
        print("Tabuleiro:")
        for i, linha in enumerate(self.tabuleiro):
             #converte cada carta da linha para sau representação visivel
             linha_str = '  '.join([c.mostrar() for c in linha])
             print(f"{i+1} {linha_str}")
        print()

    def jogar(self):
        #método principal que controla o fluxo do jogo
        while self.pontuacao < 8:
            self.exibir_tabuleiro() #mostra o tabuleiro a cada rodada
            # verifica se o jogador já virou duas cartas
            if len(self.cartas_viradas) < 2:
                try:
                    #solicita ao jogador que escolhe uma linha e coluna
                    linha = int(input("Escolha a linha (1-4): ")) - 1
                    coluna = int(input("Escolha a coluna (1-4): ")) - 1
                    #Acessa a carta na posição escolhida
                    carta = self.tabuleiro[linha] [coluna]
                    #Verifica se carta já está virada
                    if carta.virada:
                        print("Carta já virada. Tente outra.")
                        continue
                    #vira a carta e adiciona á lista de cartas viradas
                    carta.virar()
                    self.cartas_viradas.append(carta)
                except (IndexError, ValueError):
                    #trata entradas inválidas
                    print("Entrada inválida. Tente novamente.")
                    continue
            #quando duas cartas estiverem viradas, verifica se formam um par
            if len (self.cartas_viradas) == 2:
                self.exibir_tabuleiro() #mostra o tabuleiro com duas cartas viradas
                c1,c2 = self.cartas_viradas #pega as duas cartas da lista de cartas viradas para compará-las

                #verifica se o caracteres das duas cartas são iguais
                if c1.caractere == c2.caractere:
                    print("Você encontrou um par! Você ganhou!")
                else:
                    print("Não é um par. Memorize as carta e tente novamente!")
                    #pausa o jogo por 5 segundos para o jogador memorizar as cartas
                    time.sleep(4)
                    #esconde as cartas novamente, pois não eram um par
                    c1.esconder()
                    c2.esconder()
                #limpa a lista de cartas da rodada para preparar para a proxima rodada
                self.cartas_viradas.clear()
         