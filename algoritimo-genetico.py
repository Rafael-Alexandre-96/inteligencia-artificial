import random

def gerarAleatorio(maxValue):
    val = random.randint(1, maxValue)
    return formatarBinario(val)

def formatarBinario(valor):
    val = str(bin(valor)).replace("0b", '')
    i = 6 - len(val)
    while(i > 0):
        val = "0" + val
        i -= 1
    return val
    
def formatarDecimal(valor):
    return int(valor, 2)
    
def gerarFilho(paiA, paiB):
    filho = str(paiA[0])+str(paiA[1])+str(paiA[2])
    filho = filho + str(paiB[3])+str(paiB[4])+str(paiB[5])   
    return filho
    
def gerarMutacao(filho):
    val = list(filho)
    index = random.randint(0, 5)
    val[index] = '1' if (val[index] == '0') else '0'   
    return ''.join(val)
    
def rankearPopulacao(populacao):
    populacao.sort(reverse=True)
    return populacao
    
def selecionarMelhoresPais(populacao):
    return [populacao[0], populacao[1]]

a = gerarAleatorio(60)
b = gerarAleatorio(60)

f1 = gerarFilho(a, b)
f2 = gerarFilho(b, a)
f3 = gerarMutacao(f1)
f4 = gerarMutacao(f2)

print(formatarDecimal(a))
print(a)

print(formatarDecimal(b))
print(b)

print(formatarDecimal(f1))
print(f1)

print(formatarDecimal(f2))
print(f2)

print(formatarDecimal(f3))
print(f3)

print(formatarDecimal(f4))
print(f4)

pop = [formatarDecimal(f1), formatarDecimal(f2), formatarDecimal(f3), formatarDecimal(f4)]
print(rankearPopulacao(pop))
print(selecionarMelhoresPais(pop))
