# CONTEXTO - app

## Información del Proyecto

- **Nombre**: app
- **Descripción**: Trabajo preliminar de investigación. Objetivo: build a openFrameworks 0.12 app on iPhone 15. Incluye: db, curl, sensores. Referencias: Controladores MIDI/OSC, instalaciones artísticas donde usuario interviene la obra gestionando su dispositivo como si fuera un instrumento de dibujo.
- **Tipo**: Python Library (Investigación Preliminar)
  - **Meta**: App nativa en C++ con [openFrameworks](https://openframeworks.cc/) para iPhone 15
- **Autor**: Assiz Alcaraz Baxter
- **Fecha de Creación**: 2025-10-26

## Estructura Generada

```
app/
├── README.md                    # Documentación principal
├── BITACORA.md                 # Log de desarrollo
├── roadmap_v1.md               # Plan de desarrollo
├── requirements.txt            # Dependencias
├── METODOLOGIA_DESARROLLO.md   # Metodología establecida
├── CONTEXTO.md                 # Este archivo
├── src/                        # Código fuente
│   └── app.py
├── tests/                      # Pruebas
│   └── README.md
├── docs/                       # Documentación
│   └── TUTORIAL.md
├── examples/                   # Ejemplos
└── logs/                       # Logs
```

## Próximos Pasos

1. Revisar y ajustar archivos generados
2. Implementar funcionalidades core
3. Crear tests unitarios
4. Seguir metodología en METODOLOGIA_DESARROLLO.md

## Comandos Útiles

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar tests
pytest

# Actualizar bitácora
echo "### $(date +%Y-%m-%d)" >> BITACORA.md
```

---
**Generado automáticamente**: 2025-10-26
