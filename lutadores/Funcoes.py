def paraBinario(decimal, tamanho = 4):
  val = str(bin(decimal)).replace("0b", '')
  i = tamanho - len(val)
  while(i > 0):
      val = "0" + val
      i -= 1
  return val
    
def paraDecimal(binario):
  return int(binario, 2)