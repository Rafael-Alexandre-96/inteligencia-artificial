import Funcoes

class Lutador:
  def __init__(self):
    self.ataque = "0000"
    self.defesa = "0000"

  def getAtaque(self, retornaDecimal = False):
    if retornaDecimal:
      return Funcoes.paraDecimal(self.ataque)
    else:
      return self.ataque

  def getDefesa(self, retornaDecimal = False):
    if retornaDecimal:
      return Funcoes.paraDecimal(self.defesa)
    
    return self.defesa

  def setAtaque(self, valor, insereDecimal = False):
    if insereDecimal:
      self.ataque = Funcoes.paraBinario(valor)
    else:
      self.ataque = valor

  def setDefesa(self, valor, insereDecimal = False):
    if insereDecimal:
      self.defesa = Funcoes.paraBinario(valor)
    else:
      self.defesa = valor