letras = []
nome = list("Augusto")
print (nome)

nome2 = nome.copy()
nome2[0] = "P"
nome2.append("!!!!!")

print (nome2)

nome2.clear()

print(nome2)

nome3 = []
nome2.extend(["!!!", "$$$"])
nome3.extend([f"{nome} {nome2}"])
print(nome3)

print(nome.index("u"))

print(nome.pop())#retira o último elemento
print(nome)
print(nome.pop(3))#retira o elemento selecionado por indice
print(nome)
nome.remove("g")#retira o elemento especificado 
print(nome)
nome.reverse()#inverte a ordem 
print(nome)
nome.sort()#ordena a lista
print(nome)
nome.sort(reverse=True)#ordena a lista em ordem decrescente
print(nome)
nome.insert(1, "!!!")#insere o elemento selecionado por indice
print(nome)
nome.append("!!!")#insere o elemento no final da lista
print(nome)
nome.remove("!!!")#remove o elemento especificado
print(nome)

print(nome.count("!!!"))#conta quantas vezes o elemento aparece na lista

nome4 = "paralelepípedo"
print(nome4)
nome_u = set(nome4)
#nome_u.sort() nao funciona para set(), precisa transformar em uma list()
nome_u = list(nome_u)
nome_u.sort()
print(nome_u)

