import os
import subprocess
import sys

def create_virtualenv(env_name='venv'):
    """Cria um ambiente virtual."""
    # Verifique se o ambiente virtual já existe
    if os.path.exists(env_name):
        print(f"Ambiente virtual '{env_name}' já existe.")
    else:
        print(f"Criando ambiente virtual '{env_name}'...")
        try:
            subprocess.check_call([sys.executable, '-m', 'virtualenv', env_name])
            print(f"Ambiente virtual '{env_name}' criado com sucesso.")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao criar o ambiente virtual: {e}")
            sys.exit(1)

def get_pip_executable(env_name='venv'):
    """Retorna o caminho do pip no ambiente virtual."""
    if os.name == 'nt':  # Windows
        return os.path.join(env_name, 'Scripts', 'pip')
    else:  # Linux/macOS
        return os.path.join(env_name, 'bin', 'pip')

def install_requirements(env_name='venv'):
    """Instala as dependências do arquivo requirements.txt dentro do ambiente virtual."""
    project_root = os.path.dirname(os.path.abspath(__file__))
    requirements_path = os.path.join(project_root, 'requirements.txt')

    # Verifica se o arquivo requirements.txt existe
    if not os.path.exists(requirements_path):
        print(f"Arquivo 'requirements.txt' não encontrado no caminho: {requirements_path}")
        sys.exit(1)

    # Obtém o caminho do pip dentro do ambiente virtual
    pip_executable = get_pip_executable(env_name)

    # Instala as dependências usando o pip do ambiente virtual
    try:
        print(f"Instalando dependências no ambiente virtual usando {pip_executable}...")
        subprocess.check_call([pip_executable, 'install', '-r', requirements_path])
        print("Todas as dependências foram instaladas com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao instalar as dependências: {e}")
        sys.exit(1)

def main():
    """Função principal para configurar o projeto."""
    env_name = 'venv'  # Nome do ambiente virtual (pode ser personalizado)
    
    create_virtualenv(env_name)
    install_requirements(env_name)

if __name__ == '__main__':
    main()
