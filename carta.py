#Classe que representa uma carta do jogo
class Carta:
   def __init__(self, caractere):
      self.caractere = caractere # caractere que identifica a carta
      self.virada = False #estado da carta : virada ou escondida 

   def virar (self):
      #método para virar a carta ( mostrar o caractere)
      self.virada = True

   def esconder(self):
      #metodo para esconder a carta (mostrar 'x')
      self.virada = False

   def mostrar(self):
      #retorna o caractere se a carta virada, caso contrário, mostra 'x'
      return self.caractere if self.virada else "x"
            
            