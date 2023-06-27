entrada = int(input())

contador = 1
n = 65

while (entrada < 1 or entrada > 26):
  entrada = int(input())

while contador <= 26 and n <= 90: 
  print(f'{contador * chr(n)}')
  contador += 1
  n += 1
  if contador == (entrada + 1): 
    break
