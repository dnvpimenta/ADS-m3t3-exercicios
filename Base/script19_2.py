import sqlite3 as conector
from modelo import Veiculo

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

# Definição dos comandos
comando = '''SELECT
                Veiculo.placa, Veiculo.ano, Veiculo.cor,
                Veiculo.motor, Veiculo.proprietario,
                Marca.nome FROM Veiculo JOIN Marca ON Marca.id = Veiculo.marca;'''
cursor.execute(comando)

# Recuperação dos registros
reg_veiculos = cursor.fetchall()
for reg_veiculo in reg_veiculos:
    veiculo = Veiculo(*reg_veiculo)
    print("Placa:", veiculo.placa, ", Marca:", veiculo.marca)

# Fechamento das conexões
cursor.close()
conexao.close()
