def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
  contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": False}
  contatos.append(contato) # cada contato adicionado vai para o fim da lista
  print(f"\nContato {nome_contato} foi adicionado com sucesso!!")
  return

def ver_contatos(contatos):
  print("\nLista de contatos:")
  for indice, contato in enumerate(contatos, start=1):
    status = "★" if contato["favorito"] else " "
    nome_contato = contato["nome"]
    telefone_contato = contato["telefone"]
    email_contato = contato["email"]
    print(f"\nContato {indice}: \nNome: {nome_contato} \nTelefone: {telefone_contato} \nE-mail: {email_contato}\nFavoritos: [{status}]")
  return

def editar_contato(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["nome"] = novo_nome_contato
    contatos[indice_contato_ajustado]["telefone"] = novo_telefone_contato
    contatos[indice_contato_ajustado]["email"] = novo_email_contato
  
    print(f"\nContato {indice_contato} atualizado para\nNome: {novo_nome_contato};\nTelefone: {novo_telefone_contato};\nE-mail: {novo_email_contato}")
  else:
    print("\nIndice de contato inválido!!")
  return

def adicionar_contato_favorito(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  contatos[indice_contato_ajustado]["favorito"] = True
  print(f"\nContato {indice_contato} marcada como favorito!")

  return

def deletar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    del contatos[indice_contato_ajustado]
    print(f"\nContato {indice_contato} deletado com sucesso!")
  else:
    print("\nIndice de contato inválido!!")
  return

def ver_contato_favorito(contatos):
  print("\nLista de contatos favoritos:")
  for indice, contato in enumerate(contatos, start=1):
    if contato["favorito"]:
      nome_contato = contato["nome"]
      telefone_contato = contato["telefone"]
      email_contato = contato["email"]
      print(f"\nContato {indice} \nNome: {nome_contato} \nTelefone: {telefone_contato} \nE-mail: {email_contato}")
  return

def retirar_contato_favorito(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  contatos[indice_contato_ajustado]["favorito"] = False
  print(f"\nContato {indice_contato} desmarcada como favorito!")

  return

contatos = []

while True:
  print("\nAgenda de contatos:")
  print("1. Adicionar contato:")
  print("2. Ver contatos:")
  print("3. Editar dados do contato:")
  print("4. Marcar contato como favorito:")
  print("5. Deletar um contato:")
  print("6. Fechar agenda de contatos:")
  print("7. Ver contatos favoritados ")
  print("8. Retirar contato dos favoritos:")

  escolha = input("\nDigite sua escolha: ")

  if escolha == "1":
    nome_contato = input("Adicionar o nome: ")
    telefone_contato = input("Adicionar telefone: ")
    email_contato = input("Adicionar o email: ")
    adicionar_contato(contatos,nome_contato, telefone_contato, email_contato)
  elif escolha == "2":
    ver_contatos(contatos)
  elif escolha =="3":
    ver_contatos(contatos)
    inidice_contato = input("\nDigite o numero do contato que deseja atualizar: ")
    novo_nome_contato = input("\nDigite o novo nome do contato: ")
    novo_telefone_contato = input("\nDigite o novo telefone do contato: ")
    novo_email_contato = input("\nDigite o novo email do contato: ")
    editar_contato(contatos, inidice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato)

  elif escolha == "4":
    ver_contatos(contatos)
    inidice_contato = input("\nDigite o indice do contato que deseja favoritar: ")
    adicionar_contato_favorito(contatos, inidice_contato)

  elif escolha == "5":
    ver_contatos(contatos)
    indice_contato = input("\nDigite o indice do contato que deseja deletar: ")
    deletar_contato(contatos, indice_contato)
    ver_contatos(contatos)

  elif escolha == "6":
    break
  elif escolha == "7":
    ver_contato_favorito(contatos)

  elif escolha == "8":
    ver_contatos(contatos) ##mostra somente contatos favoritos
    inidice_contato = input("\nDigite o indice do contato que deseja desfavoritar: ")
    retirar_contato_favorito(contatos, inidice_contato)