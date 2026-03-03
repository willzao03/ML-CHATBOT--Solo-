import sys

def check_environment():
    print("=" * 50)
    print("VERIFICAÇÃO DO AMBIENTE")
    print("=" * 50)
    
    # Verifica versão do Python
    python_version = sys.version_info
    print(f"\n✓ Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 10):
        print("❌ ERRO: Python 3.10 ou superior é necessário!")
        return False
    
    # Verifica bibliotecas
    libraries = ['pandas', 'matplotlib', 'sklearn']
    missing = []
    
    for lib in libraries:
        try:
            __import__(lib)
            print(f"✓ {lib} instalado")
        except ImportError:
            print(f"❌ {lib} NÃO instalado")
            missing.append(lib)
    
    print("\n" + "=" * 50)
    if not missing:
        print("RESULTADO: PRONTO PARA AULA!")
    else:
        print(f"RESULTADO: Instale: {', '.join(missing)}")
    print("=" * 50)
    
    return len(missing) == 0

if __name__ == "__main__":
    check_environment()
