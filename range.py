name = "Augusto"
VOGAIS = "AEIOU"
for letras in name:
  if letras.upper() in VOGAIS:
   print(letras, end=".")
print("")

#range cria sozinho uma sequência de números inteiros
print(range(5))

print(list(range(5)))

print(list(range(0,30,3)))

for num in range(0,30,3):
 print(num, end="-")
print("")

while True:
  num = int(input ("Digite um número: "))
  if num == 7:
    print("Voce acertou!")
    break 

