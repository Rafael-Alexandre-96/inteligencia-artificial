from Lutador import Lutador
import random

def gerarFilho(lutadorA, lutadorB):
  filho = Lutador()

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
    print("Fez mutação")
  return novoDna

def __criarMutacao(dna):
  i = random.randint(0, len(dna) - 1)
  val = list(dna)
  val[i] = '1' if (val[i] == '0') else '0'
  return ''.join(val)