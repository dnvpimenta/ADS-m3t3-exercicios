from modelo import Veiculo, Marca


def recuperar_veiculos(conexao, cpf):
    # Aquisição de cursor
    cursor = conexao.cursor()

    # Definição dos comandos
    comando = '''SELECT * FROM Veiculo
                 JOIN Marca ON Marca.id = Veiculo.marca
                 WHERE Veiculo.proprietario = ?;'''
    cursor.execute(comando, (cpf,))

    # Recuperação dos registros
    veiculos = []
    registros = cursor.fetchall()
    for registro in registros:
        marca = Marca(*registro[6:])
        veiculo = Veiculo(*registro[:5], marca)
        veiculos.append(veiculo)

    # Fechamento do cursor
    cursor.close()
    return veiculos
