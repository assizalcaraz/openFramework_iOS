# 🤖 Guía para Cursor AI - app

**IMPORTANTE**: Este es un proyecto generado con Pre-Cursor. Este archivo contiene instrucciones específicas para agentes de IA en Cursor.

---

## 📋 Contexto del Proyecto

### Objetivo Principal
**Trabajo preliminar de investigación. Objetivo build a openFramework 0.12 app on iphone 15. db, curl, sensorres. Referencias: Controladores MIDI/OSC, instalaciones artísticas donde usuario interviene la obra gestionando su dispositivo como si fuera un instrumento de dibujo.**

### Tipo de Proyecto
**Python Library** - Aplicación iOS con openFrameworks 0.12 para iPhone 15, integrando sensores, comunicación MIDI/OSC, y transformación del dispositivo en un instrumento de dibujo interactivo para instalaciones artísticas

### Metodología
Este proyecto sigue la metodología establecida de Pre-Cursor, optimizada para desarrollo con agentes de IA.

---

## 🎯 Instrucciones para Cursor AI

### 1. **Usar este template como GUÍA, no como código final**
- ✅ **SÍ**: Adaptar el código a los objetivos específicos del proyecto
- ✅ **SÍ**: Modificar funciones según las necesidades reales
- ✅ **SÍ**: Añadir funcionalidades que cumplan la descripción del proyecto
- ❌ **NO**: Copiar literalmente sin adaptar al contexto
- ❌ **NO**: Dejar placeholders sin procesar

### 2. **Alinear TODO al objetivo del proyecto**
- Revisar `Trabajo preliminar de investigación. Objetivo build a openFramework 0.12 app on iphone 15. db, curl, sensorres. Referencias: Controladores MIDI/OSC, instalaciones artísticas donde usuario interviene la obra gestionando su dispositivo como si fuera un instrumento de dibujo.` antes de cada cambio
- Cada función debe contribuir al objetivo principal
- Priorizar funcionalidades que cumplan la descripción

### 3. **Estructura base a seguir**
```
app/
├── README.md                    # Documentación principal
├── CONTEXTO.md                  # Contexto del proyecto
├── requirements.txt             # Dependencias
├── src/                         # Código fuente
│   ├── app.py
│   └── utils/
├── tests/                       # Pruebas
├── docs/                        # Documentación técnica
│   ├── TUTORIAL.md              # Guía de uso
│   ├── BITACORA.md              # Log de desarrollo
│   ├── CURSOR_GUIDE.md          # Este archivo (para IA)
│   ├── roadmap_v1.md            # Plan de desarrollo
│   └── METODOLOGIA_DESARROLLO.md # Metodología establecida
├── .cursor/                     # Integración Cursor CLI
│   ├── prompts/                 # Prompts generados
│   │   ├── 2024-10-14/          # Organizados por fecha
│   │   │   ├── move_test_files_080529.md
│   │   │   └── reorganize_structure_080506.md
│   │   └── latest.md            # Enlace al último prompt
│   ├── logs/                    # Logs de ejecución
│   │   ├── instructions.json    # Instrucciones generadas
│   │   ├── executions.json      # Log de ejecuciones
│   │   ├── feedback.json        # Log de feedback
│   │   └── metrics.json         # Métricas de integración
│   └── config/                  # Configuración específica
│       └── cursor_supervisor.yaml
└── examples/                    # Ejemplos de uso
```

### 4. **Organización de archivos**
- **📁 docs/**: Toda la documentación técnica va aquí
- **📁 src/**: Código fuente principal
- **📁 tests/**: Pruebas unitarias y de integración
- **📁 examples/**: Ejemplos de uso y demos
- **📁 .cursor/**: Integración Cursor CLI (NO modificar manualmente)
- **📄 README.md**: Documentación principal (en raíz)
- **📄 CONTEXTO.md**: Contexto del proyecto (en raíz)

### 5. **Integración Cursor CLI**
- **📁 .cursor/prompts/**: Prompts generados automáticamente por el supervisor
- **📁 .cursor/logs/**: Logs de ejecución y métricas de integración
- **📁 .cursor/config/**: Configuración específica del supervisor
- **📄 .cursor/prompts/latest.md**: Enlace al último prompt generado

---

## 🔧 Comandos Útiles para Cursor

### Verificar estado del proyecto
```bash
# Ver estructura actual
ls -la

# Verificar dependencias
pip list | grep app

# Ejecutar tests
pytest tests/
```

### Desarrollo iterativo
```bash
# Instalar en modo desarrollo
pip install -e .

# Ejecutar proyecto
python -m app

# Verificar sintaxis
python -m py_compile src/app.py
```

### Integración Cursor CLI
```bash
# Ver último prompt generado
cat .cursor/prompts/latest.md

# Ver logs de ejecución
cat .cursor/logs/executions.json

# Ver métricas de integración
cat .cursor/logs/metrics.json

# Listar prompts por fecha
ls -la .cursor/prompts/2024-10-14/

# Ver configuración del supervisor
cat .cursor/config/cursor_supervisor.yaml
```

---

## 📝 Checklist de Desarrollo

### ✅ Fase 1: Configuración
- [ ] Revisar `requirements.txt` y instalar dependencias
- [ ] Verificar que el código base compila sin errores
- [ ] Leer `README.md` para entender el objetivo
- [ ] Revisar `TUTORIAL.md` para ejemplos de uso

### ✅ Fase 2: Adaptación
- [ ] Identificar qué funcionalidades faltan según la descripción
- [ ] Modificar `app.py` para cumplir objetivos
- [ ] Actualizar documentación según cambios realizados
- [ ] Añadir tests para nuevas funcionalidades

### ✅ Fase 3: Validación
- [ ] Ejecutar todos los tests: `pytest`
- [ ] Verificar que el proyecto cumple su descripción
- [ ] Actualizar `BITACORA.md` con cambios realizados
- [ ] Revisar que no quedan placeholders sin procesar

---

## 🚨 Errores Comunes a Evitar

### ❌ NO hacer esto:
1. **Dejar placeholders**: `{{VARIABLE}}` o `$VARIABLE` sin reemplazar
2. **Copiar literalmente**: Sin adaptar al contexto del proyecto
3. **Ignorar la descripción**: No alinear funcionalidades al objetivo
4. **Saltarse tests**: No verificar que el código funciona

### ✅ SÍ hacer esto:
1. **Adaptar al contexto**: Modificar código según necesidades reales
2. **Cumplir objetivos**: Cada función debe servir al propósito del proyecto
3. **Documentar cambios**: Actualizar README y comentarios
4. **Probar funcionalidad**: Ejecutar tests y verificar funcionamiento

---

## 📚 Archivos de Referencia

### Documentación Principal
- `README.md` - Información general del proyecto
- `TUTORIAL.md` - Guía paso a paso de uso
- `BITACORA.md` - Historial de cambios y decisiones

### Código Fuente
- `src/app.py` - Módulo principal (ADAPTAR SEGÚN OBJETIVOS)
- `src/utils/` - Utilidades auxiliares
- `tests/` - Pruebas unitarias e integración

### Configuración
- `requirements.txt` - Dependencias Python
- `pyproject.toml` - Configuración del proyecto
- `.gitignore` - Archivos ignorados por Git

---

## 🎯 Objetivos Específicos de app

### Funcionalidad Principal
**Trabajo preliminar de investigación. Objetivo build a openFramework 0.12 app on iphone 15. db, curl, sensorres. Referencias: Controladores MIDI/OSC, instalaciones artísticas donde usuario interviene la obra gestionando su dispositivo como si fuera un instrumento de dibujo.**

### Características Esperadas
- Integración con sensores del iPhone 15 (acelerómetro, giroscopio, brújula)
- Comunicación MIDI/OSC para control externo de instalaciones artísticas
- Transformación del dispositivo en instrumento de dibujo interactivo
- Base de datos para almacenar patrones y configuraciones
- Sistema de comunicación curl para sincronización de datos

### Casos de Uso
1. Instalación artística interactiva donde el usuario dibuja con el iPhone como si fuera un instrumento
2. Controlador MIDI/OSC para efectos visuales y sonoros en tiempo real
3. Captura y procesamiento de datos de sensores para visualizaciones creativas

---

## 🔄 Flujo de Trabajo Recomendado

1. **Leer contexto**: Revisar descripción y objetivos
2. **Analizar template**: Entender estructura base
3. **Adaptar código**: Modificar según necesidades reales
4. **Implementar funcionalidades**: Añadir características específicas
5. **Probar y validar**: Ejecutar tests y verificar funcionamiento
6. **Documentar cambios**: Actualizar README y comentarios

---

## 📞 Información de Contacto

- **Autor**: Assiz Alcaraz Baxter
- **Email**: Por definir
- **GitHub**: [@assizalcaraz](https://github.com/assizalcaraz)
- **Proyecto**: [app](https://github.com/assizalcaraz/app)

---

**Fecha de Creación**: 2025-10-26  
**Última Actualización**: 2025-10-26  
**Versión**: 0.1.0-prealpha

---

> **💡 Tip para Cursor**: Este archivo es tu guía principal. Léelo completo antes de empezar a trabajar en el proyecto y consulta la descripción del proyecto para mantener el foco en los objetivos reales.
