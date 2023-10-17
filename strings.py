name = " aUgU StO "

print(name.upper())
print(name.lower())
print(name.title())

#retirar espaço 
print(name.strip())
print(name.lstrip())
print(name.rstrip())

print(name.center(20, "#"))
print(".".join(name))

PI = 3.14159

print(f"O número de PI é {PI: 10.4}")
print(f"O numero de PI é {PI: 0.10f}")

texto = "Um texto qualquer!"
print(texto[3:13])
print(texto [:13])
print(texto [13:])
print(texto [::2])
print(texto [::-1])

mensagem_formatada = f"""     um texto
        com espaços
  e multiplas linhas"""

print(mensagem_formatada)
