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
    populacao = list(map(formatarDecimal, populacao))
    populacao.sort(reverse=True)
    populacao = list(map(formatarBinario, populacao))
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
    
def mostrarBinDec(valBin):
    return valBin + " - " + str(formatarDecimal("0b" + valBin))
    
def resultadoGeracao(pais, filhos):
    print("--PAIS--")
    print(list(map(mostrarBinDec, pais)))
    print("--FILHOS--")
    print(list(map(mostrarBinDec, filhos)))
    print("--RANKING--")
    print(list(map(mostrarBinDec, rankearPopulacao(filhos))))
    print("--MELHORES PAIS--")
    print(list(map(mostrarBinDec, selecionarMelhoresPais(filhos))))
    
def criarGeracoes(quantidade):
    paiA = "000001"
    paiB = "000000"
   
    inicial = quantidade
    
    while(quantidade > 0):
        print("\n======GERACAO " + str(inicial - quantidade + 1) + "======")
        populacao = gerarPopulacao(paiA, paiB)
        resultadoGeracao([paiA, paiB], populacao)
        paiA = selecionarMelhoresPais(populacao)[0]
        paiB = selecionarMelhoresPais(populacao)[1]
        quantidade -= 1
    
    print("\nRESULTADO:")
    print("ESTES FORAM OS PAIS DA 1A GERACAO")
    print(["000001 - 1", "000000 - 0"])
    print("EM " + str(inicial) + " GERACOES ESTES FORAM OS MELHORES RESULTADOS")
    print(list(map(mostrarBinDec, [paiA, paiB])))
        
print('ATRAVES DO ALGORITIMO GENETICO, \nDEVEMOS OBTER O MAIOR VALOR DECIMAL GERADO \nATRAVES DOS PAIS: ["000001 - 1", "000000 - 0"]')
print('\nDIGITE criarGeracoes(x) SENDO x A QUANTIDADE DE GERACOES PARA SEREM EVOLUIDAS.')