from Lutador import Lutador
from Batalha import Batalha
import Geracao

def realizarBatalhas(lutadores):
  batalha = Batalha()
  novosFilhos = []

  while(batalha.selecionaLutadoresAleat(lutadores)):
    while(batalha.getVencedor() == None):
      batalha.realizarTurno()

    novosFilhos.append(batalha.getVencedor())
    batalha.reinicia()

  return novosFilhos

pais = [Geracao.gerarLutador('Raf-Rur'), Geracao.gerarLutador('Khor-Kul'), Geracao.gerarLutador('Tyr-Tous'), Geracao.gerarLutador('Lif-Lost')]
print("PAIS")
for pai in pais:
  pai.print()

filhos = Geracao.gerarFilhos(pais)
print("FILHOS")
for filho in filhos:
  filho.print()

filhos = realizarBatalhas(filhos)
filhos = realizarBatalhas(filhos)

i = 0

while(i < 10):
  print("Geração: " + str(i))

  print("PAIS")
  for filho in filhos:
    filho.print() 

  filhos = Geracao.gerarFilhos(filhos)
  print("FILHOS")
  for filho in filhos:
    filho.print() 

  filhos = realizarBatalhas(filhos)
  filhos = realizarBatalhas(filhos)
  i += 1

print("MELHORES")
for filho in filhos:
  filho.print()