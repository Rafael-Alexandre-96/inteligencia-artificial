import Funcoes

class Lutador:
  def __init__(self):
    self.nome = ""
    self.ataque = "0001"
    self.defesa = "0000"
    self.vida = "10000000"
    self.vidaInicial = "10000000"

  def getNome(self):
    return self.nome

  def getAtaque(self, retornaDecimal = False):
    if retornaDecimal:
      return Funcoes.paraDecimal(self.ataque)
    else:
      return self.ataque

  def getDefesa(self, retornaDecimal = False):
    if retornaDecimal:
      return Funcoes.paraDecimal(self.defesa)
    
    return self.defesa

  def getVida(self, retornaDecimal = False):
    if retornaDecimal:
      return Funcoes.paraDecimal(self.vida)
    
    return self.vida

  def receberDano(self, dano):
    if dano < 1:
      dano = 1
    vida = Funcoes.paraDecimal(self.vida) - dano
    if vida < 0:
      vida = 0
    self.vida = Funcoes.paraBinario(vida, 8)

  def checarVida(self):
    if self.getVida(True) > 0:
      return True
    
    return False

  def setNome(self, nome):
    self.nome = nome

  def setAtaque(self, valor, insereDecimal = False):
    if insereDecimal:
      if valor == 0:
        valor = 1
      self.ataque = Funcoes.paraBinario(valor)
    else:
      if valor == "0000":
        valor = "0001"
      self.ataque = valor

  def setDefesa(self, valor, insereDecimal = False):
    if insereDecimal:
      self.defesa = Funcoes.paraBinario(valor)
    else:
      self.defesa = valor

  def setVida(self, valor, insereDecimal = False):
    if insereDecimal:
      self.vida = Funcoes.paraBinario(valor, 8)
      self.vidaInicial = Funcoes.paraBinario(valor, 8)
    else:
      self.vida = valor
      self.vidaInicial = valor

  def reiniciaVida(self):
    self.vida = self.vidaInicial

  def print(self):
    print(self.nome + " / ATK:" + str(self.getAtaque(True)) + " DEF:" + str(self.getDefesa(True)) + " HP:" + str(self.getVida(True)))