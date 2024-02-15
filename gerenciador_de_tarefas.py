def adicionar_tarefa(tarefas, nome_tarefa):
  #tarefa: nome da tarefa
  #completada: indica se essa tarefa ja foi completada ou nao
  tarefa = {"tarefa": nome_tarefa, "completada": False} #biblioteca
  tarefas.append(tarefa) #adiciona ao fim da lista
  print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!!")
  return

def ver_tarefas(tarefas):
  print("\n Lista de tarefas:")
  for indice, tarefa in enumerate(tarefas, start=1):
    status = "✓" if tarefa["completada"] else " "
    nome_tarefa = tarefa["tarefa"]
    print(f"{indice}. [{status}] {nome_tarefa}")
  return 

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
  indice_tarefa_ajustado = int(indice_tarefa) - 1
  if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
    tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
    print(f"\nTarefa {indice_tarefa} atualizada para novo {novo_nome_tarefa}")
  else:
    print("\nIndice de tarefas inválido!")
  return

def completar_tarefas(tarrefas, indice_tarefa):
  indice_tarefa_ajustado = int(indice_tarefa) - 1
  tarefas[indice_tarefa_ajustado]["completada"] = True
  print(f"\nTarefa {indice_tarefa} marcada como completa!")
  return

def deletar_tarefa_completada(tarefas):
  
  for tarefa in tarefas:
    if tarefa["completada"] == True:
      tarefas.remove(tarefa)
  print("\nTarefas completadas foram deletadas!!")      
  return

tarefas = []

while True:
  print("\n Menu do gerenciador de lista de tarefas:")
  print("1. Adicionar tarefas:")
  print("2. Ver tarefas:")
  print("3. Atualizar tarefas:")
  print("4. Completar tarefas:")
  print("5. Deletar tarefas completadas:")
  print("6. Sair:")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
    adicionar_tarefa(tarefas, nome_tarefa)
  elif escolha == "2":
    ver_tarefas(tarefas)
  elif escolha == "3":
    ver_tarefas(tarefas)
    indice_tarefa = input("\nDigite o numero da tarefa que deseja atualiza? ")
    novo_nome = input("\nDigite o novo nome da tarefa: ")
    atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
  elif escolha == "4":
    ver_tarefas(tarefas)
    indice_tarefa = input("\nDigite o numero da tarefa que deseja completar: ")
    completar_tarefas(tarefas, indice_tarefa)
  elif escolha == "5":
    deletar_tarefa_completada(tarefas)
    ver_tarefas(tarefas)

  elif escolha == "6":
    break
  

print("Programa finalizado")
