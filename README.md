# app

Trabajo preliminar de investigación. Objetivo build a openFramework 0.12 app on iphone 15. db, curl, sensorres. Referencias: Controladores MIDI/OSC, instalaciones artísticas donde usuario interviene la obra gestionando su dispositivo como si fuera un instrumento de dibujo.

## 🚀 Inicio Rápido

### Requisitos
- Python 3.10+
- macOS (para acceso a sensores de iOS vía PyObjC)
- Git

### Instalación
```bash
# Clonar el repositorio
git clone https://github.com/assizalcaraz/app.git
cd app

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar tests
pytest
```

### Uso Básico

```python
from src.app import App
from src.sensors import SensorManager, SensorType
from src.communication import CommunicationManager, OSCMessage

# Ejemplo básico
app = App()

# Ejemplo con sensores
sensor_manager = SensorManager()
comm_manager = CommunicationManager()

# Ejemplo de uso en instalación artística
def process_sensor_data(data):
    """Procesar datos del sensor y enviar OSC."""
    osc_msg = OSCMessage("/instrument/position", [data.x, data.y, data.z])
    comm_manager.send_osc(osc_msg, "192.168.1.100:8000")

# Registrar callback
sensor_manager.register_callback(SensorType.ACCELEROMETER, process_sensor_data)
```

## 📁 Estructura del Proyecto

```
app/
├── README.md                    # Este archivo
├── CONTEXTO.md                  # Contexto del proyecto
├── METODOLOGIA_DESARROLLO.md   # Metodología de desarrollo
├── requirements.txt            # Dependencias
├── src/                        # Código fuente
│   ├── app.py                  # Módulo principal
│   ├── sensors.py              # Gestor de sensores del iPhone
│   ├── communication.py        # Comunicación MIDI/OSC
│   └── utils/                  # Utilidades
│       ├── __init__.py
│       └── helpers.py          # Funciones matemáticas
├── tests/                      # Pruebas
│   ├── README.md              # Instrucciones de testing
│   └── test_app.py
├── docs/                       # Documentación
│   ├── BITACORA.md            # Log de desarrollo
│   ├── CURSOR_GUIDE.md        # Guía para IA
│   ├── roadmap_v1.md          # Plan de desarrollo
│   └── TUTORIAL.md            # Tutorial de uso
└── examples/                   # Ejemplos
```

## 🧪 Testing

Seguir las instrucciones en `tests/README.md` para ejecutar las pruebas.

## 📚 Documentación

- [Tutorial de Inicio](docs/TUTORIAL.md)
- [API Reference](docs/API.md)
- [Contributing](CONTRIBUTING.md)

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'WIP: Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 👨‍💻 Autor

**Assiz Alcaraz Baxter**
- GitHub: [@](https://github.com/assizalcaraz)


---

**Fecha de Creación**: 2025-10-26  
**Última Actualización**: 2025-10-26
