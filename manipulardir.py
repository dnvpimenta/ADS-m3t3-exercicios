import os
import shutil

def criar_diretorios(diretorios):
    for diretorio in diretorios:
        if not os.path.exists(diretorio):
            try:
                os.makedirs(diretorio)
                print(f"Diretório {diretorio} criado.")
            except PermissionError:
                print(f"Sem permissão para criar o diretório {diretorio}.")
            except Exception as e:
                print(f"Erro inesperado ao criar {diretorio}: {e}")

def mover_arquivos(diretorio_origem):
    for arquivo in os.listdir(diretorio_origem):
        caminho_arquivo = os.path.join(diretorio_origem, arquivo)
        if os.path.isfile(caminho_arquivo):
            # Verificar se o arquivo tem extensão
            if '.' in arquivo:
                extensao = arquivo.split('.')[-1].lower()
                if extensao in ['md', 'txt', 'py']:
                    diretorio_destino = os.path.join(diretorio_origem, extensao)
                    try:
                        # Verificar se o arquivo já existe no destino
                        destino = os.path.join(diretorio_destino, arquivo)
                        if os.path.exists(destino):
                            # Se existir, renomeia com um número
                            nome_base, ext = os.path.splitext(arquivo)
                            contador = 1
                            while os.path.exists(os.path.join(diretorio_destino, f"{nome_base}_{contador}{ext}")):
                                contador += 1
                            novo_nome = f"{nome_base}_{contador}{ext}"
                            destino = os.path.join(diretorio_destino, novo_nome)
                            shutil.move(caminho_arquivo, destino)
                            print(f"{arquivo} renomeado para {novo_nome} e movido para {diretorio_destino}.")
                        else:
                            shutil.move(caminho_arquivo, diretorio_destino)
                            print(f"{arquivo} movido para {diretorio_destino}.")
                    except PermissionError:
                        print(f"Sem permissão para mover {arquivo}.")
                    except Exception as e:
                        print(f"Erro inesperado ao mover {arquivo}: {e}")
                else:
                    print(f"Extensão '{extensao}' de {arquivo} não é suportada.")
            else:
                print(f"Arquivo {arquivo} não tem extensão e será ignorado.")

def criar_arquivos_teste(diretorio_trabalho):
    """Função opcional para criar arquivos de teste"""
    import random
    
    # Criar alguns arquivos de exemplo
    extensoes = ['md', 'txt', 'py', 'pdf', 'jpg']
    
    for i in range(10):
        ext = random.choice(extensoes)
        nome_arquivo = f"arquivo_{i+1}.{ext}"
        caminho = os.path.join(diretorio_trabalho, nome_arquivo)
        
        try:
            with open(caminho, 'w') as f:
                f.write(f"Conteúdo do arquivo {nome_arquivo}")
            print(f"Arquivo de teste criado: {nome_arquivo}")
        except Exception as e:
            print(f"Erro ao criar {nome_arquivo}: {e}")

def main():
    diretorio_trabalho = "diretorio_trabalho"
    
    # Criar diretório de trabalho se não existir
    if not os.path.exists(diretorio_trabalho):
        try:
            os.makedirs(diretorio_trabalho)
            print(f"Diretório principal {diretorio_trabalho} criado.")
            
            # Opcional: criar arquivos de teste
            criar_arquivos = input("Deseja criar arquivos de teste? (s/n): ").lower()
            if criar_arquivos == 's':
                criar_arquivos_teste(diretorio_trabalho)
        except Exception as e:
            print(f"Erro ao criar diretório principal: {e}")
            return
    
    diretorios = [
        os.path.join(diretorio_trabalho, 'md'),
        os.path.join(diretorio_trabalho, 'txt'),
        os.path.join(diretorio_trabalho, 'py')
    ]
    
    # Criar diretórios se não existirem
    criar_diretorios(diretorios)
    
    # Mostrar arquivos antes da organização
    print("\n📁 Arquivos antes da organização:")
    for arquivo in os.listdir(diretorio_trabalho):
        caminho = os.path.join(diretorio_trabalho, arquivo)
        if os.path.isfile(caminho):
            print(f"   📄 {arquivo}")
    
    print("\n🔄 Organizando arquivos...\n")
    
    # Mover arquivos para os diretórios correspondentes
    mover_arquivos(diretorio_trabalho)
    
    print("\n✅ Organização concluída!")
    
    # Mostrar resultado final
    print("\n📁 Estrutura final:")
    for root, dirs, files in os.walk(diretorio_trabalho):
        nivel = root.replace(diretorio_trabalho, '').count(os.sep)
        indent = '   ' * nivel
        print(f"{indent}📂 {os.path.basename(root)}/")
        subindent = '   ' * (nivel + 1)
        for file in files:
            print(f"{subindent}📄 {file}")

if __name__ == "__main__":
    main()