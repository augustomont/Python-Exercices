# Exemplo de código usando set
nums = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 9, 1 , 2, 3, 4, 5, 11, 12, 13, 14, 15, 16, 15]
unique_nums = set(nums)
print(unique_nums)

nums001 = {1, 2, 3, 4, 5}
print(nums001.issubset(unique_nums))# verifica se o conjunto é subconjunto do outro
print(unique_nums.issuperset(nums001))# verifica se o conjunto é super

nums2 = {1, 3, 5, 7, 11, 13, 17, 19, 23, 29}
print(type(nums2))

print(nums001.isdisjoint(nums2))# verifica se o conjunto é disjunto do outro. ou seja, nao tem nenhum elemento em comum

nums12 = unique_nums.union(nums2)#junta osnfois conjuntos com elementos únicos 
print(nums12)

nums23 = unique_nums.intersection(nums2)# une apenas os elementos comuns aos dois
print (nums23)

nums34 = unique_nums.difference(nums2)# Elementos que estão no primeiro conjunto, mas nao estão no segundo conjunto.
print(nums34)

nums45 = unique_nums.symmetric_difference(nums2)# todos os elementos que não são semelhantes entre eles. elementos unicos de cada um.
print(nums45)

nums56 = unique_nums.difference_update(nums2)# diferença entre os conjuntos
print(nums56)

nums67 = unique_nums.intersection_update(nums2)# une apenas os elementos comuns aos dois
print (nums67)

nums78 = unique_nums.symmetric_difference_update(nums2)# diferença entre os conjuntos
print(nums78)

nums89 = unique_nums.add(9)# adiciona um elemento ao conjunto, caso nao exista ainda.
print(nums89)

nums90 = unique_nums.discard(9)# remove um elemento do conjunto, caso ele exista. se ele nao existir, nao tem problema. ele ignora.
print(nums90)

nums91 = unique_nums.pop()# remove o ultimo elemento do conjunto
print(nums91)

nums92 = unique_nums.remove(13)# remove o primeiro elemento do conjunto. Caso nao exista, ele da mensagem de erro!!!
print(nums92)

nums93 = unique_nums.clear()# limpa o conjunto
print(nums93)

nums94 = unique_nums.copy()# copia o conjunto
print(nums94)

nums95 = unique_nums.update(nums2)# adiciona os elementos do segundo conjunto ao primeiro conjunto.
print(nums95)

print(7 in unique_nums)# verifica se o elemento está no conjunto
print(7 not in unique_nums)# verifica se o elemento não está no conjunto
