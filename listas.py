lestras = list("Augusto")

print(lestras)
print(lestras[3])
print(lestras[:4])
print(lestras[4:])
print(lestras[::2])

print (lestras[-2] )
print("-".join(lestras))
print(list(range (10)))

for lt in lestras:
    print(lt, end="#")
print("")
for indice, ltrs in enumerate(lestras):
  print(f"{indice}: {ltrs}")

numeros = list(range(20))
pares = []
for num in numeros:
  if num % 2 == 0:
    pares.append(num)
print(pares)

#or...

pares = [num for num in numeros if num % 2 == 0]
print(pares)

quadrado = [num ** 2 for num in pares]
print(quadrado)

