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

      if self.lutadorB.checarVida():
        dano = self.__calculaDano(self.lutadorB, self.lutadorA)
        self.lutadorA.receberDano(dano)

        if not(self.lutadorA.checarVida()):
          self.vencedor = self.lutadorB
          self.vencedor.reiniciaVida()
      else:
        self.vencedor = self.lutadorA
        self.vencedor.reiniciaVida()
    else:
      raise Exception("Batalha realizarTurno(): Lutadores não setados")

  def getVencedor(self):
    return self.vencedor
  
  def __calculaDano(self, lutadorA, lutadorB):
    if lutadorA != None and lutadorB != None:
      dano = (lutadorA.getAtaque(True) * 2) - (lutadorB.getDefesa(True))
      if dano < 0:
        dano = 1
      dano = dano + random.randint(-int(dano/2), int(dano/2))
      return dano
    else:
      raise Exception("Batalha __calculaDano(): Lutadores não setados")