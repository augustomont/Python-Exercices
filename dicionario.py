pessoa = {
    'nome': 'Pedro',
    'idade': 25,
    'sexo': 'M',
    'peso': 70.5
}
print(pessoa)
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['sexo'])
print(pessoa['peso'])
print(pessoa.keys())#mostra as chaves
print(pessoa.values())#mostra os valores
print(pessoa.items())#mostra os itens completos (chave e valor)

contatos = {
  "Augusto": {"email": "ejeyd@example.com", "telefone": "(41) 99999-9999"},
  "João": {"email": "ztejd@example.com", "telefone": "(41) 88888888"},
  "Maria": {"email": "ejeyd@example.com", "telefone": "(41) 77777777"}
}

for nome, contato in contatos.items():#metodos para mostrar cada item (chave e valor)
  print(nome)
  print(contato["email"])
  print(contato["telefone"])
  print()

for nome, contato in contatos.items():#metodos para mostrar cada item (chave e valor)
  print(f"{nome}: {contato['email']} - {contato['telefone']}")
  print()

pelasChaves = dict.fromkeys(["chave1", "chave2", "chave3"], "valor_padrao")#cria um dicionário a partir das chaves, com um valor padrão para todas as chaves
print(pelasChaves)

print(pelasChaves["chave1"])#mostra o valor da chave caso ela exista
print(pelasChaves.get("chave99"))#mostra o valor da chave caso ela exista, ou não.
print(pelasChaves.get("chave99", "valor_caso_vazio"))#mostra o valor da chave caso ela exista, ou o valor padrão caso ela não exista

print(pelasChaves.keys())#mostra as chaves
print(pelasChaves.values())#mostra os valores
print(pelasChaves.items())#mostra os itens completos (chave e valor)

pelasChaves.setdefault("chave87", "valor_adcionado")#adiciona um valor padrão caso a chave não exista
print(pelasChaves.get("chave87"))#mostra o valor da chave caso ela exista.

print(pelasChaves.pop("chave87"))#remove o valor da chave e retorna o valor
print(pelasChaves.pop("chave87", "valor_caso_vazio"))#remove o valor da chave e retorna o valor, ou o valor padrão caso a chave não exista

pelasChaves.update({"chave88": "valor_novo"})#adiciona um valor padrão caso a chave não exista
print(pelasChaves.get("chave88"))#mostra o valor da chave caso ela exista.

teste = "chave1" in pelasChaves#verifica se a chave existe
print(teste)

print(pelasChaves.clear())#remove todos os itens do dicionário
print(pelasChaves)

teste = "chave1" in pelasChaves#verifica se a chave existe
print(teste)


del contatos["João"]#remove um item do dicionário
print(contatos)

del contatos#remove o dicionário inteiro
#print(contatos) - gera um erro, pois o dicionário foi deletado

