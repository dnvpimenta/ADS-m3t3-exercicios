import sqlite3 as conector
from modelo import Pessoa
# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

# Definição dos comandos
comando = '''SELECT * FROM Pessoa WHERE oculos=:usa_oculos;'''
cursor.execute(comando, {"usa_oculos": True})

# Recuperação dos registros
registros = cursor.fetchall()
for registro in registros:
    pessoa = Pessoa(*registro)
    print("cpf:", type(pessoa.cpf), pessoa.cpf)
    print("nome:", type(pessoa.nome), pessoa.nome)
    print("nascimento:", type(pessoa.data_nascimento), pessoa.data_nascimento)
    print("oculos:", type(pessoa.usa_oculos), pessoa.usa_oculos)

# Fechamento das conexões
cursor.close()
conexao.close()
