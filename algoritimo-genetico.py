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
    populacao[0] = formatarDecimal(populacao[0])
    populacao[1] = formatarDecimal(populacao[1])
    populacao[2] = formatarDecimal(populacao[2])
    populacao[3] = formatarDecimal(populacao[3])
    populacao.sort(reverse=True)
    populacao[0] = formatarBinario(populacao[0])
    populacao[1] = formatarBinario(populacao[1])
    populacao[2] = formatarBinario(populacao[2])
    populacao[3] = formatarBinario(populacao[3])
    return populacao
    
def selecionarMelhoresPais(populacao):
    val = populacao
    val = rankearPopulacao(populacao)
    return [val[0], val[1]]
    
def gerarPopulacao(paiA, paiB):
    filhoA = gerarFilho(paiA, paiB)
    filhoB = gerarFilho(paiB, paiA)
    filhoC = gerarMutacao(filhoA)
    filhoD = gerarMutacao(filhoB)
    return [filhoA, filhoB, filhoC, filhoD]
    
def resultadoGeracao(pais, filhos):
    print("--Pais--")
    print(pais)
    print("--Filhos--")
    print(filhos)
    print("--Ranking--")
    print(rankearPopulacao(filhos))
    print("--Melhores Pais--")
    print(selecionarMelhoresPais(filhos))
    
paiA = gerarAleatorio(60)
paiB = gerarAleatorio(60)
    
populacao = gerarPopulacao(paiA, paiB)

resultadoGeracao([paiA, paiB], populacao)
