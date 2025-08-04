import random
from JogoMemoria import JogoDaMemoria #Importa do arquivo JogoMemoria a classe JogaDaMemoria

def main():
    jogo = JogoDaMemoria() #cria uma instancia do jogo
    print("Bem-vindo ao Jogo da Memória!")
    jogo.jogar() #chama o método 'jogar' para iniciar a partida

if __name__ == '__main__':
    main()   

    
    