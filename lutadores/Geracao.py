from Lutador import Lutador
import random

def gerarLutador(nome = ''):
  lutador = Lutador()
  lutador.setNome(nome)
  lutador.setAtaque(random.randint(1, 3), True)
  lutador.setDefesa(random.randint(0, 3), True)
  lutador.setVida(random.randint(0, 80), True)
  return lutador

def gerarFilho(lutadorA, lutadorB):
  filho = Lutador()
  filho.setNome(__gerarNome(lutadorA.getNome(), lutadorB.getNome()))
  filho.setAtaque(__gerarDna(lutadorA.getAtaque(), lutadorB.getAtaque()))
  filho.setDefesa(__gerarDna(lutadorA.getDefesa(), lutadorB.getDefesa()))
  filho.setVida(__gerarDna(lutadorA.getVida(), lutadorB.getVida()))
  return filho

def gerarFilhos(pais):
  filhos = []
  for paiA in pais:
    for paiB in pais:
      filhos.append(gerarFilho(paiA, paiB))
  return filhos

def __gerarNome(nomeA, nomeB):
  return nomeA.split('-')[0] + '-' + nomeB.split('-')[1]

def __gerarDna(dnaA, dnaB):
  tamanho = len(dnaA) / 2
  novoDna = ''
  i = 0
  while(i < tamanho):
    novoDna += dnaA[i]
    i += 1
  tamanho += tamanho
  while(i < tamanho):
    novoDna += dnaB[i]
    i += 1
  if(random.randint(0, 1) == 1):
    novoDna = __criarMutacao(novoDna)
  return novoDna

def __criarMutacao(dna):
  i = random.randint(0, len(dna) - 1)
  val = list(dna)
  val[i] = '1' if (val[i] == '0') else '0'
  return ''.join(val)