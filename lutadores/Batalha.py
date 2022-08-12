from Lutador import Lutador
import random

class Batalha:
  def __init__(self):
    self.reinicia()

  def reinicia(self):
    self.lutadorA = None
    self.lutadorB = None
    self.vencedor = None

  def selecionaLutadoresAleat(self, lutadores):
    if len(lutadores) == 0:
      return False
      
    self.setLutadores(lutadores.pop(random.randint(0, len(lutadores) - 1)), lutadores.pop(random.randint(0, len(lutadores) - 1)))
    return True
    
  def setLutadores(self, lutadorA, lutadorB):
    self.lutadorA = lutadorA
    self.lutadorB = lutadorB

  def realizarTurno(self):
    if self.lutadorA != None and self.lutadorB != None:
      dano = self.__calculaDano(self.lutadorA, self.lutadorB)
      self.lutadorB.receberDano(dano)

      if self.__checarVida(self.lutadorB):
        dano = self.__calculaDano(self.lutadorB, self.lutadorA)
        self.lutadorA.receberDano(dano)

        if not(self.__checarVida(self.lutadorA)):
          self.vencedor = self.lutadorB
          self.vencedor.reiniciaVida()
          
      else:
        self.vencedor = self.lutadorA
        self.vencedor.reiniciaVida()

  def getVencedor(self):
    return self.vencedor
  
  def __calculaDano(self, lutadorA, lutadorB):
    if lutadorA != None and lutadorB != None:
      dano = (lutadorA.getAtaque(True) * 2) - (lutadorB.getDefesa(True))
      if dano < 0:
        dano = 1
      dano = dano + random.randint(-int(dano/2), int(dano/2))
      if dano < 0:
        dano = 1
      return dano

    return 0

  def __checarVida(self, lutador):
    if lutador.getVida(True) > 0:
      return True
    
    return False