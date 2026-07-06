from interface import cabecalho, cores

def livro_existe(msg):
  msg = msg.strip().casefold()
  with open('livros.txt', 'r') as arquivo: 
    for linha in arquivo:
      linha2 = linha.strip().casefold()
      if msg == linha2:
        return True
  return False

def cadastrar():
  cabecalho('Cadastrar livro')
  titulo = input('Título: ').strip().title()
  if livro_existe(titulo):
    print(f'{cores["verm"]}Livro já existente no arquivo.{cores["lim"]}')
  else:
    print(f'{cores["verd"]}Livro cadastrado com sucesso!{cores["lim"]}')
    with open('livros.txt', 'a') as arquivo:
      arquivo.write(f'\n{titulo}')
    
def listar():
  cabecalho('Listar livros')
  with open('livros.txt', 'r') as arquivo:
    livros = arquivo.readlines()
  livros.sort()
  for indice, livro in enumerate(livros):
    print(f'{indice + 1}. {livro.strip()}')
  print(f'\nTotal de livros: {len(livros)}')

def buscar():
  cabecalho('Buscar livro')
  procura = input('Livro desejado: ').strip()
  encontrou = False
  with open('livros.txt', 'r') as arquivo:
    for linha in arquivo:
      linha2 = linha.strip().casefold()
      if procura.casefold() == linha2:
        print(f'{cores["verd"]}Livro "{linha.strip()}" encontrado com sucesso!{cores["lim"]}')
        encontrou = True
        break
  if not encontrou:
    print(f'{cores["verm"]}Livro não está na biblioteca.{cores["lim"]}')

def remover():
  cabecalho('Remover livro')
  titulo = input('Remover livro: ').strip()
  removido = False
  with open('livros.txt', 'r') as arquivo:
    livros = arquivo.readlines()
    for livro in livros:
      if titulo.casefold() == livro.strip().casefold():
        livros.remove(livro)
        print(f'{cores["verd"]}Livro "{livro.strip()}" removido com sucesso!{cores["lim"]}')
        removido = True
        break
  if removido:
    with open('livros.txt', 'w') as arquivo:
      arquivo.writelines(livros)
  else:
    print(f'{cores["verm"]}Livro não está na biblioteca.{cores["lim"]}')

def editar():
  cabecalho('Editar nome')
  titulo = input('Digite o nome do livro para editar: ').strip()
  existe = False
  with open('livros.txt', 'r') as arquivo:
    livros = arquivo.readlines()
    for indice, livro in enumerate(livros):
      if titulo.casefold() == livro.strip().casefold():
        existe = True
        break  
  if not existe:
    print('Livro não está na bibliotaca.')
  else:
    print(f'Livro {livro.strip()} encontrado! ')
    titulo2 = input('Digite o novo nome: ').strip().title()
    if livro_existe(titulo2):
      print(f'{cores["verm"]}Livro já existente na biblioteca. Nenhuma alteração feita.{cores["lim"]}')
    else:
      livros[indice] = f'{titulo2}\n'
      with open('livros.txt', 'w') as arquivo:
        arquivo.writelines(livros)
      print(f'{cores["verd"]}Livro "{livro.strip()}" modificado para "{titulo2}" com sucesso!{cores["lim"]}')
