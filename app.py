import os
import random
import shutil


def copiar_imagens(origem='imagens', destino='imagens2'):
    # Garante que a pasta de destino existe
    os.makedirs(destino, exist_ok=True)
    
    # Lista e filtra os arquivos .jpeg
    arquivos = [arquivo for arquivo in os.listdir(origem) if arquivo.lower().endswith('.jpeg')]
    
    # Embaralha os arquivos
    random.shuffle(arquivos)
    
    # Copia e renomeia os arquivos
    for i, arquivo in enumerate(arquivos, start=1):
        origem_arquivo = os.path.join(origem, arquivo)
        destino_arquivo = os.path.join(destino, f'{i}.jpeg')
        shutil.copy2(origem_arquivo, destino_arquivo)  # Copia mantendo metadados
        print(f'Copiado e renomeado: {arquivo} -> {i}.jpeg')

if __name__ == "__main__":
    copiar_imagens()
