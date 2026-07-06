from interface import principal
from livros import cadastrar, listar, buscar, remover, editar
from time import sleep


while True:
  escolha = principal()

  if escolha == 1:
    cadastrar()

  elif escolha == 2:
    listar()
  
  elif escolha == 3:
    buscar()

  elif escolha == 4:
    remover()

  elif escolha == 5:
    editar()

  elif escolha == 6:
    break

  sleep(1)

  