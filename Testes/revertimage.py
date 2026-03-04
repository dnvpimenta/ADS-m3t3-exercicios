import os
import sys
import subprocess

def verificar_dependencias():
    """Verifica e instala dependências automaticamente"""
    try:
        from PIL import Image
        import numpy as np
        print("✅ Bibliotecas já estão instaladas!")
        return Image, np
    except ImportError as e:
        print(f"❌ Erro: {e}")
        print("📦 Instalando dependências automaticamente...")
        
        try:
            # Instalar usando pip
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow", "numpy"])
            
            # Tentar importar novamente
            from PIL import Image
            import numpy as np
            print("✅ Dependências instaladas com sucesso!")
            return Image, np
        except Exception as install_error:
            print(f"❌ Falha na instalação: {install_error}")
            print("\n📝 Instruções manuais:")
            print("1. Abra o Prompt de Comando como administrador")
            print("2. Execute:")
            print(f'   "{sys.executable}" -m pip install pillow numpy')
            sys.exit(1)

def main():
    # Verificar dependências primeiro
    Image, np = verificar_dependencias()
    
    try:
        # Caminho da imagem
        caminho_imagem = r"C:\Users\hanny\OneDrive\Área de Trabalho\DIREITA.jpg"
        
        print(f"📁 Procurando imagem em: {caminho_imagem}")
        
        # Verificar se o arquivo existe
        if not os.path.exists(caminho_imagem):
            print("❌ Arquivo não encontrado!")
            print("\n📂 Arquivos na Área de Trabalho:")
            desktop = r"C:\Users\hanny\OneDrive\Área de Trabalho"
            if os.path.exists(desktop):
                for arquivo in os.listdir(desktop):
                    if arquivo.lower().endswith(('.jpg', '.jpeg', '.png')):
                        print(f"   📸 {arquivo}")
            return
        
        # Processar a imagem
        print(f"\n📷 Carregando imagem: {caminho_imagem}")
        img = Image.open(caminho_imagem)
        print(f"   Formato: {img.size} pixels")
        print(f"   Modo: {img.mode}")
        
        # Converter para array numpy
        img_data = np.array(img)
        print(f"   Shape do array: {img_data.shape}")
        print(f"   Tipo de dado: {img_data.dtype}")
        
        # Converter para bytes
        binary_data = img_data.tobytes()
        print(f"   Tamanho em bytes: {len(binary_data):,}")
        
        # Salvar binário original
        with open("original_img.bin", "wb") as f:
            f.write(binary_data)
        print("✅ original_img.bin salvo")
        
        # Criar cópia e inverter
        with open("copy_img.bin", "wb") as f:
            f.write(binary_data)
        
        # Inverter os bytes
        with open("copy_img.bin", "rb") as f:
            data = bytearray(f.read())
        
        data_invertido = data[::-1]
        
        with open("copy_img.bin", "wb") as f:
            f.write(data_invertido)
        print("✅ copy_img.bin salvo (bytes invertidos)")
        
        # Tentar recriar imagem invertida
        try:
            inverted_array = np.frombuffer(data_invertido, dtype=img_data.dtype)
            if inverted_array.size == img_data.size:
                inverted_array = inverted_array.reshape(img_data.shape)
                inverted_img = Image.fromarray(inverted_array)
                
                nome_saida = "imagem_invertida.jpg"
                inverted_img.save(nome_saida)
                print(f"✅ Imagem invertida salva como: {nome_saida}")
            else:
                print(f"⚠️  Tamanho incompatível")
        except Exception as e:
            print(f"⚠️  Não foi possível recriar imagem: {e}")
        
        print("\n📊 PROCESSO CONCLUÍDO!")
        
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()