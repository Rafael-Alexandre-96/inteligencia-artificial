import random

#Função para gerar um individuo aleatorio.
#
#Parametro <maxValue>: Valor máximo do decimal à ser gerado aleatoriamente.
#Retorno <string>: Binário de 6 posições.
def gerarAleatorio(maxValue):
    val = random.randint(1, maxValue)
    return formatarBinario(val)

#Função converter Decimal para Binario.
#
#Parametro <valor>: Decimal a ser convertido.
#Retorno <string>: Binario de 6 posições.
def formatarBinario(valor):
    val = str(bin(valor)).replace("0b", '')
    i = 6 - len(val)
    while(i > 0):
        val = "0" + val
        i -= 1
    return val

#Função converter Binario para Decimal.
#
#Parametro <valor>: Binario de 6 posições a ser convertido.
#Retorno <int>: Decimal.  
def formatarDecimal(valor):
    return int(valor, 2)

#Função para gerar um filho atraves de Crossover simples.
#
#Parametro <paiA>: Binario de 6 posições.
#Parametro <paiB>: Binario de 6 posições.
#Retorno <string>: Binario de 6 posições. 
def gerarFilho(paiA, paiB):
    filho = str(paiA[0])+str(paiA[1])+str(paiA[2])
    filho = filho + str(paiB[3])+str(paiB[4])+str(paiB[5])   
    return filho

#Função para criar uma mutação em um filho atraves do Operador Genetico.
#
#Parametro <filho>: Binario de 6 posições.
#Retorno <string>: Binario de 6 posições.    
def gerarMutacao(filho):
    val = list(filho)
    index = random.randint(0, 5)
    val[index] = '1' if (val[index] == '0') else '0'   
    return ''.join(val)

#Função para Rank dos individuos, sendo os maiores valores decimal posicionados em primeiro.
#
#Parametro <populacao>: Lista com uma população de binário de 6 posições.
#Retorno <string>: Lista com uma população de binários de 6 posições rankeada.     
def rankearPopulacao(populacao):
    populacao = list(map(formatarDecimal, populacao))
    populacao.sort(reverse=True)
    populacao = list(map(formatarBinario, populacao))
    return populacao

#Função para selecionar os melhores pais de uma população.
#
#Parametro <populacao>: Lista com uma população de binário de 6 posições.
#Retorno <lista>: Lista de 2 pais binários de 6 posições rankeada.      
def selecionarMelhoresPais(populacao):
    val = populacao
    val = rankearPopulacao(populacao)
    return [val[0], val[1]]

#Função para gerar uma população de 4 filhos através de 2 pais.
#
#Parametro <paiA>: Binario de 6 posições.
#Parametro <paiB>: Binario de 6 posições.
#Retorno <lista>: Lista de 4 filhos Binarios de 6 posições. 
def gerarPopulacao(paiA, paiB):
    filhoA = gerarFilho(paiA, paiB)
    filhoB = gerarFilho(paiB, paiA)
    filhoC = gerarMutacao(filhoA)
    filhoD = gerarMutacao(filhoB)
    return [filhoA, filhoB, filhoC, filhoD]

#Função mostrar o valor Binário e Decimal juntos.
#
#Parametro <valBin>: Binario de 6 posições.
#Retorno <string>: String formatada Bin - Dec.   
def mostrarBinDec(valBin):
    return valBin + " - " + str(formatarDecimal("0b" + valBin))

#Função imprimir o resultado de uma geração, contendo os pais, os filhos, o Rank e os 2 melhores pais.
#
#Parametro <pais>: Lista de 2 pais binários de 6 posições.
#Parametro <filhos>: Lista de 4 filhos Binarios de 6 posições. 
#Retorno: Impresso os valores em tela   
def resultadoGeracao(pais, filhos):
    print("--PAIS--")
    print(list(map(mostrarBinDec, pais)))
    print("--FILHOS--")
    print(list(map(mostrarBinDec, filhos)))
    print("--RANKING--")
    print(list(map(mostrarBinDec, rankearPopulacao(filhos))))
    print("--MELHORES PAIS--")
    print(list(map(mostrarBinDec, selecionarMelhoresPais(filhos))))

#Função criar 'n' gerações através dos pais ["000001 - 1", "000000 - 0"]
#no final das gerações devem ser escolhidos os individuos com maiores valores decimais.
#
#Parametro <quantidade>: Quantidade de gerações a serem realizadas.
#Retorno: Impresso os valores em tela  
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