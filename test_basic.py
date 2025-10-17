#!/usr/bin/env python3
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
