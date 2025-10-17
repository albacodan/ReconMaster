# 🔍 ReconMaster

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
