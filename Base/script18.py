import sqlite3 as conector
from modelo import Pessoa
# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./meu_banco.db", detect_types=conector.PARSE_DECLTYPES)
cursor = conexao.cursor()

# Funções conversoras
def conv_bool(dado):
    return True if dado == 1 else False

# Registro de conversores
conector.register_converter("BOOLEAN", conv_bool)

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
