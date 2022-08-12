from Lutador import Lutador
from Batalha import Batalha

lutadorA = Lutador()
lutadorB = Lutador()

lutadorA.setNome("Rafael")
lutadorA.setAtaque(5, True)
lutadorA.setDefesa(5, True)

lutadorB.setNome("João")
lutadorB.setAtaque(5, True)
lutadorB.setDefesa(5, True)

lutadorA.print()
lutadorB.print()

batalha = Batalha()
batalha.setLutadores(lutadorA, lutadorB)

while(batalha.getVencedor() == None):
  batalha.realizarTurno()

  lutadorA.print()
  lutadorB.print()

print("Vencedor")
batalha.getVencedor().print()