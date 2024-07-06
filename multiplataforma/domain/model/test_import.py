import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
current_dir = os.path.dirname(__file__)
root_dir = os.path.abspath(os.path.join(current_dir, '../../../'))
sys.path.insert(0, root_dir)

try:
    from multiplataforma.config.database import Base, engine
    print("Importação bem-sucedida!")
except ImportError as e:
    print(f"Erro ao importar: {e}")