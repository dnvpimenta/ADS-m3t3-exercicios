import os

arquivo = open('dados.txt', 'w', encoding='utf-8')

print("Nome do arquivo:", arquivo.name)
print("Modo de abertura:", arquivo.mode)
print("Arquivo está fechado?", arquivo.closed)


arquivo.write("Olá mundo!")
arquivo.close()

print("Arquivo está fechado agora?", arquivo.closed)

relpath = os.path.relpath('dados.txt')
abspath = os.path.abspath('dados.txt')

print("Caminho relativo:", relpath)
print("Caminho absoluto:", abspath)
