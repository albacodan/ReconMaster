import os
import zipfile
import shutil

# Crear estructura de carpetas completa para ReconMaster
base_dir = 'ReconMaster'

# Limpiar directorio si existe
if os.path.exists(base_dir):
    shutil.rmtree(base_dir)

# Crear estructura de directorios
subdirs = [
    'core',
    'config', 
    'output',
    'screenshots',
    'docs',
    'tests'
]

os.makedirs(base_dir, exist_ok=True)
for sub in subdirs:
    os.makedirs(os.path.join(base_dir, sub), exist_ok=True)

# Contenido principal del archivo main.py
main_py_content = '''#!/usr/bin/env python3
"""
ReconMaster v1.0
Automated Reconnaissance Tool for Penetration Testing
Author: Daniel Albarrán Acosta
LinkedIn: linkedin.com/in/dalbaco/

DISCLAIMER: Esta herramienta es solo para uso en entornos autorizados
"""

import argparse
import sys
import os
from datetime import datetime
from colorama import init, Fore, Style

# Inicializar colorama para colores cross-platform
init()

def print_banner():
    banner = f"""
{Fore.CYAN}
╦═╗╔═╗╔═╗╔═╗╔╗╔╔╦╗╔═╗╔═╗╔╦╗╔═╗╦═╗
╠╦╝║╣ ║  ║ ║║║║║║║╠═╣╚═╗ ║ ║╣ ╠╦╝
╩╚═╚═╝╚═╝╚═╝╝╚╝╩ ╩╩ ╩╚═╝ ╩ ╚═╝╩╚═{Style.RESET_ALL}
{Fore.GREEN}    Automated Reconnaissance Tool v1.0{Style.RESET_ALL}
{Fore.YELLOW}    Por: Daniel Albarrán Acosta{Style.RESET_ALL}
{Fore.MAGENTA}    LinkedIn: linkedin.com/in/dalbaco/{Style.RESET_ALL}

{Fore.RED}⚠️  SOLO PARA USO AUTORIZADO - FINES EDUCATIVOS{Style.RESET_ALL}
    """
    print(banner)

def main():
    print_banner()
    
    parser = argparse.ArgumentParser(
        description="ReconMaster - Automated Reconnaissance Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python main.py example.com                    # Reconocimiento completo
  python main.py -s example.com                 # Solo subdominios
  python main.py example.com -o /tmp/results    # Output personalizado
        """
    )
    
    parser.add_argument('target', help='Target domain o IP address')
    parser.add_argument('-o', '--output', default='output', 
                       help='Directorio de output (default: output)')
    parser.add_argument('-s', '--subdomains-only', action='store_true',
                       help='Solo ejecutar enumeración de subdominios')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Modo verbose')
    
    args = parser.parse_args()
    
    print(f"{Fore.GREEN}[+] Target: {args.target}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[+] Output directory: {args.output}{Style.RESET_ALL}")
    
    if args.verbose:
        print(f"{Fore.BLUE}[+] Modo verbose activado{Style.RESET_ALL}")
    
    print(f"{Fore.YELLOW}[!] ReconMaster está en desarrollo - Semana 1 completada{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[+] Próximamente: Enumeración de subdominios funcional{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
'''

# Contenido del archivo utils.py
utils_py_content = '''"""
Utilidades compartidas para ReconMaster
"""

import re
import socket
import ipaddress
from colorama import Fore, Style
from datetime import datetime

def validate_target(target):
    """Validar si el target es un dominio o IP válida"""
    # Validar IP
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        pass
    
    # Validar dominio
    domain_pattern = re.compile(
        r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)*[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$'
    )
    return bool(domain_pattern.match(target))

def is_ip(target):
    """Verificar si el target es una IP"""
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        return False

def resolve_domain(domain):
    """Resolver dominio a IP"""
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return None

def get_timestamp():
    """Obtener timestamp actual"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def print_status(message, status="info"):
    """Print con colores según status"""
    colors = {
        "info": Fore.BLUE,
        "success": Fore.GREEN,
        "warning": Fore.YELLOW,
        "error": Fore.RED
    }
    
    symbols = {
        "info": "[+]",
        "success": "[✓]", 
        "warning": "[!]",
        "error": "[✗]"
    }
    
    color = colors.get(status, Fore.WHITE)
    symbol = symbols.get(status, "[+]")
    
    print(f"{color}{symbol} {message}{Style.RESET_ALL}")
'''

# Contenido del README.md
readme_content = '''# 🔍 ReconMaster

<div align="center">
  <img src="https://img.shields.io/badge/python-v3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/contributions-welcome-orange.svg" alt="Contributions">
  <img src="https://img.shields.io/badge/status-development-yellow.svg" alt="Status">
</div>

## 🎯 Descripción

**ReconMaster** es una herramienta de reconocimiento automatizado desarrollada para pentesting y preparación de la certificación eJPTv2. Automatiza las fases de reconocimiento más tediosas, permitiendo a los pentesters enfocarse en la explotación.

**Desarrollada por:** Daniel Albarrán Acosta  
**LinkedIn:** [linkedin.com/in/dalbaco/](https://linkedin.com/in/dalbaco/)  
**Objetivo:** Certificación eJPTv2 y primera posición en ciberseguridad  

## 🚀 Estado Actual (Semana 1 - En Desarrollo)

- ✅ **Estructura base del proyecto** completada
- ✅ **CLI con colores** y argumentos básicos
- ✅ **Utilidades de validación** implementadas
- ✅ **Sistema modular** para escalabilidad
- 🚧 **Enumeración de subdominios** (próximamente)
- 📅 **Port scanning** (Semana 2)
- 📅 **Reportes HTML** (Semana 3)

## 🛠️ Instalación

### Método Rápido (Sin entorno virtual)
```bash
git clone https://github.com/tuusuario/ReconMaster.git
cd ReconMaster
pip3 install --user -r requirements.txt
```

### Con entorno virtual (Opcional)
```bash
git clone https://github.com/tuusuario/ReconMaster.git
cd ReconMaster
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

## 💻 Uso

### Ayuda
```bash
python3 main.py -h
```

### Ejemplo básico (En desarrollo)
```bash
python3 main.py example.com -v
```

## 📊 Ejemplo de Salida

```bash
$ python3 main.py google.com -v

╦═╗╔═╗╔═╗╔═╗╔╗╔╔╦╗╔═╗╔═╗╔╦╗╔═╗╦═╗
╠╦╝║╣ ║  ║ ║║║║║║║╠═╣╚═╗ ║ ║╣ ╠╦╝
╩╚═╚═╝╚═╝╚═╝╝╚╝╩ ╩╩ ╩╚═╝ ╩ ╚═╝╩╚═
    Automated Reconnaissance Tool v1.0
    Por: Daniel Albarrán Acosta
    LinkedIn: linkedin.com/in/dalbaco/

⚠️  SOLO PARA USO AUTORIZADO - FINES EDUCATIVOS

[+] Target: google.com
[+] Output directory: output
[+] Modo verbose activado
[!] ReconMaster está en desarrollo - Semana 1 completada
[+] Próximamente: Enumeración de subdominios funcional
```

## 🗺️ Roadmap de Desarrollo

### ✅ Semana 1 (Completada)
- [x] Arquitectura base y CLI
- [x] Sistema de utilidades
- [x] Validación de targets
- [x] Colores y formatting

### 🚧 Semana 2 (En desarrollo)
- [ ] Enumeración de subdominios completa
- [ ] Port scanning con Nmap
- [ ] Verificación de servicios activos
- [ ] Reportes básicos

### 📅 Semana 3 (Planificada)
- [ ] OSINT integration (Shodan, VirusTotal)
- [ ] Reportes HTML profesionales
- [ ] Web enumeration básica
- [ ] Documentación completa

## 🛡️ Consideraciones Éticas

⚠️ **IMPORTANTE**: Esta herramienta está diseñada únicamente para:
- Pentesting autorizado en entornos propios
- Laboratorios de práctica y aprendizaje  
- Fines educativos y certificaciones
- Testing con permisos explícitos del propietario

**NO utilizar en sistemas sin autorización explícita.**

## 🤝 Contribuciones

Las contribuciones son bienvenidas! Este es un proyecto de aprendizaje y preparación para eJPTv2.

## 📝 Licencia

Este proyecto está bajo la licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 📧 Contacto

**Daniel Albarrán Acosta**
- LinkedIn: [linkedin.com/in/dalbaco/](https://linkedin.com/in/dalbaco/)
- Email: danielalbarranacosta610@gmail.com

---

<div align="center">
  <i>Desarrollado con ❤️ para la comunidad de ciberseguridad</i><br>
  <i>Preparación eJPTv2 | Portfolio Project 2025</i>
</div>
'''

# Contenido del requirements.txt
requirements_content = '''requests==2.31.0
colorama==0.4.6
python-nmap==0.7.1
dnspython==2.4.2
beautifulsoup4==4.12.2
jinja2==3.1.2
tqdm==4.66.1
'''

# Contenido del .gitignore
gitignore_content = '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.env

# IDEs
.vscode/
.idea/
*.swp
*.swo

# Project specific
output/
*.log
config/api_keys.json
screenshots/
.DS_Store
Thumbs.db

# Testing
.coverage
.pytest_cache/
htmlcov/
'''

# Contenido del LICENSE
license_content = '''MIT License

Copyright (c) 2025 Daniel Albarrán Acosta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

# Contenido del test básico
test_content = '''#!/usr/bin/env python3
"""
Tests básicos para ReconMaster
"""

import sys
import os

# Añadir el directorio padre al path para poder importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.utils import validate_target, is_ip, resolve_domain

def test_target_validation():
    """Test de validación de targets"""
    print("🧪 Testing target validation...")
    
    # Tests básicos
    assert validate_target("google.com") == True
    assert validate_target("192.168.1.1") == True
    assert validate_target("invalid..domain") == False
    assert validate_target("") == False
    
    print("✅ Target validation test passed")

def test_ip_detection():
    """Test de detección de IPs"""
    print("🧪 Testing IP detection...")
    
    assert is_ip("192.168.1.1") == True
    assert is_ip("8.8.8.8") == True
    assert is_ip("google.com") == False
    assert is_ip("invalid") == False
    
    print("✅ IP detection test passed")

def test_domain_resolution():
    """Test de resolución de dominios"""
    print("🧪 Testing domain resolution...")
    
    # Test con un dominio conocido
    ip = resolve_domain("google.com")
    assert ip is not None
    assert is_ip(ip) == True
    
    # Test con dominio inválido
    invalid_ip = resolve_domain("this-domain-does-not-exist-12345.com")
    assert invalid_ip is None
    
    print("✅ Domain resolution test passed")

if __name__ == "__main__":
    print("🔍 ReconMaster - Running basic tests...")
    print("=" * 50)
    
    test_target_validation()
    test_ip_detection()
    test_domain_resolution()
    
    print("=" * 50)
    print("🎉 All tests passed! ReconMaster basic functionality working.")
'''

# Crear archivos con contenido completo
archivos = {
    'main.py': main_py_content,
    'README.md': readme_content,
    'requirements.txt': requirements_content,
    '.gitignore': gitignore_content,
    'LICENSE': license_content,
    os.path.join('core', '__init__.py'): '',
    os.path.join('core', 'utils.py'): utils_py_content,
    os.path.join('tests', 'test_basic.py'): test_content,
    os.path.join('config', '.gitkeep'): '# Este archivo mantiene la carpeta config en Git',
    os.path.join('docs', '.gitkeep'): '# Este archivo mantiene la carpeta docs en Git',
    os.path.join('screenshots', '.gitkeep'): '# Este archivo mantiene la carpeta screenshots en Git'
}

# Escribir todos los archivos
for file_path, content in archivos.items():
    full_path = os.path.join(base_dir, file_path)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Crear ZIP con la estructura completa
zip_filename = 'ReconMaster-Complete-v1.0.zip'
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            file_path = os.path.join(root, file)
            # Mantener la estructura relativa dentro del zip
            arcname = os.path.relpath(file_path, '.')
            zipf.write(file_path, arcname)

print(f"✅ Proyecto ReconMaster creado exitosamente!")
print(f"📦 Archivo ZIP: {zip_filename}")
print(f"📁 Carpetas incluidas: {len(subdirs)} + archivos principales")
print(f"🔧 Archivos Python: main.py, core/utils.py, tests/test_basic.py")
print(f"📝 Documentación: README.md completo con ejemplos")
print(f"⚙️ Configuración: requirements.txt, .gitignore, LICENSE")

zip_filename