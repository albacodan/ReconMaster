#!/usr/bin/env python3
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
