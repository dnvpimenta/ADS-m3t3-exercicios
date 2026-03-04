import sqlite3 as conector
from modelo import Pessoa

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

# Criação de um objeto do tipo Pessoa
pessoa = Pessoa(30000000099, 'Silva', '1990-03-30', True)

# Definição de um comando com named parameter
comando = '''INSERT INTO Pessoa VALUES (:cpf,:nome,:data_nascimento,:usa_oculos);'''
cursor.execute(comando, vars(pessoa))
print(vars(pessoa))

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()
