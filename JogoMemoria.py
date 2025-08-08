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
             #converte cada carta da linha para sua representação visivel
             linha_str = '  '.join([c.mostrar() for c in linha])
             print(f"{i+1} {linha_str}")
        print()

    def jogar(self):
      while self.pontuacao < 8:
        # Só exibe o tabuleiro se menos de 2 cartas estiverem viradas
        if len(self.cartas_viradas) < 2:
            self.exibir_tabuleiro()
            try:
                linha = int(input("Escolha a linha (1-4): ")) - 1 #mostra ao usuário para escolher uma linha
                coluna = int(input("Escolha a coluna (1-4): ")) - 1 #mostra ao usuário para escolher uma coluna
                carta = self.tabuleiro[linha][coluna]
                if carta.virada: #verifica se a carta já foi virada
                    print("Carta já virada. Tente outra.")
                    continue
                carta.virar()
                self.cartas_viradas.append(carta)
            except (IndexError, ValueError): #verifica se há erro de valor válido, ou tentativa de acessar um ítem que não existe  
                print("Entrada inválida. Tente novamente.")
                continue

        if len(self.cartas_viradas) == 2: 
            self.exibir_tabuleiro()  # Exibe as duas cartas viradas
            c1, c2 = self.cartas_viradas
            if c1.caractere == c2.caractere: # verifica se as duas cartas viradas são iguais
                print("Você encontrou um par!") 
                self.pontuacao += 1
                self.cartas_viradas.clear() # limpa a lista 
            else: # verifica se o que está a cima não aconteceu e printa essa mensagem
                print("Não é um par. Memorize as cartas e tente novamente!")
                time.sleep(3) # dá uma pausa do tabuleiro aberto por 3 segundos 
                c1.esconder() # esconde a carta 1 
                c2.esconder() # esconde a carta 2 
                self.cartas_viradas.clear() # limpa a lista 
  
