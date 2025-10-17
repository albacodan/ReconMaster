"""
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
