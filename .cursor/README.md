# .cursor/ - Integración Cursor Supervisor

Este directorio contiene archivos de configuración y logs generados automáticamente por el sistema de supervisión de Pre-Cursor.

## ⚠️ NO modificar manualmente

Los archivos en esta carpeta son generados automáticamente y modificarlos manualmente puede romper la integración.

## 📁 Estructura

```
.cursor/
├── config/
│   └── cursor_supervisor.yaml    # Configuración del supervisor
├── prompts/                      # Prompts generados automáticamente
├── logs/                         # Logs de ejecución
└── README.md                     # Este archivo
```

## 🔧 Uso del Supervisor

El supervisor de Pre-Cursor monitorea:
- ✅ Estructura del proyecto
- ✅ Calidad de tests
- ✅ Archivos fuera de lugar
- ✅ Funciones duplicadas
- ✅ Documentación BITACORA.md

## 📊 Estado Actual

- **Proyecto**: Investigación preliminar para app iOS
- **Estado**: 47 tests, 89% cobertura
- **Fase**: Prototipo en Python
- **Meta**: Migración futura a C++/openFrameworks

