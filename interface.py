cores = {
  'lim': '\033[m',    # Limpa
  'verd': '\033[32m', # Verde
  'verm': '\033[31m', # Vermelho
  'ama': '\033[33m',  # Amarelo
  'azul': '\033[34m'  # Azul
}

def ler_int(msg):
  while True:
    try:
      return int(input(msg))
    except ValueError:
      print(f'{cores["verm"]}Erro! Digite um valor válido.{cores["lim"]}')
    except KeyboardInterrupt:
      print(f'{cores["verm"]}Erro! Digite um valor válido.{cores["lim"]}')   

def cabecalho(msg):
  print('-' * 40)
  print(f'{msg:^40}')
  print('-' * 40)

def opcoes(* msgs):
  for indice, elemento in enumerate(msgs):
    print(f'{cores["ama"]}{indice + 1}{cores["lim"]} - {cores["azul"]}{elemento}{cores["lim"]}')


def principal():
  cabecalho('Biblioteca')
  opcoes('Cadastrar livro', 'Listar livros', 'Buscar livro pelo nome', 'Remover livro', 'Editar nome de um livro', 'Sair')
  print('-' * 40)
  while True:
    opcao = ler_int(f'{cores["ama"]}Sua opção: {cores["lim"]}')
    if 1 <= opcao <= 6:
      return opcao
    print(f'{cores["verm"]}Opção inválida!{cores["lim"]}')
  

   