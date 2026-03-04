import os
import shutil

try:
    os.remove('arquivo.txt')
except FileNotFoundError:
    print("Arquivo não encontrado.")
except PermissionError:
    print("Permissão negada.")
except IsADirectoryError:
    print("Não é possível remover, é um diretório.")
except Exception as e:
    print(f"Erro inesperado: {e}")