# app - openFrameworks iOS Prototype

Proyecto de investigación preliminar en Python para el desarrollo de una aplicación iOS nativa con **openFrameworks 0.12** para iPhone 15.

## 🎯 Objetivo

Crear una aplicación interactiva que:
- **Utiliza sensores del iPhone 15** (acelerómetro, giroscopio, brújula)
- **Se comunica vía MIDI/OSC** para controlar instalaciones artísticas
- **Transforma el iPhone en un instrumento de dibujo interactivo**

Este repositorio Python sirve como **prototipo de investigación** antes de construir la aplicación nativa en C++ con openFrameworks.

## 🚀 Inicio Rápido

### Estado del Proyecto
- ✅ **Fase 1-4 Completadas** (Configuración, Módulos Core, Testing, Integración OSC/MIDI)
- ✅ **47 tests pasando** con 89% de cobertura
- ✅ **Envío real de OSC y MIDI** funcionando
- 🔄 **Próximo**: Ejemplos y migración a openFrameworks/C++

### Requisitos
- Python 3.10+
- macOS (para acceso a sensores de iOS vía PyObjC)
- Git

### Instalación
```bash
# Clonar el repositorio
git clone https://github.com/assizalcaraz/openFramework_iOS.git
cd openFramework_iOS

# Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate  # En macOS/Linux
# venv\Scripts\activate  # En Windows

# Instalar dependencias
pip install pytest pytest-asyncio pytest-cov numpy python-osc python-rtmidi

# Ejecutar tests
pytest

# Ejecutar demo
python examples/integrated_demo.py
```

### Uso Básico

**Ejemplo 1: Enviar mensaje OSC**
```python
from src.communication import CommunicationManager, OSCMessage

# Inicializar gestor de comunicación
comm_manager = CommunicationManager()
comm_manager.start()

# Crear y enviar mensaje OSC
msg = OSCMessage("/instrument/x", [0.5, 0.7, 0.9])
comm_manager.send_osc(msg, "localhost:8000")

comm_manager.stop()
```

**Ejemplo 2: Enviar evento MIDI**
```python
from src.communication import CommunicationManager, MIDIEvent

comm_manager = CommunicationManager()
comm_manager.start()

# Crear y enviar evento MIDI
event = MIDIEvent(note=64, velocity=127, channel=0)
comm_manager.send_midi(event)

comm_manager.stop()
```

**Ejemplo 3: Callbacks con sensores simulados**
```python
from src.sensors import SensorManager, SensorType, SensorData
from src.communication import CommunicationManager, OSCMessage

# Inicializar gestores
sensor_manager = SensorManager()
comm_manager = CommunicationManager()

# Callback que procesa datos del sensor
def process_sensor_data(data: SensorData):
    """Procesar datos del sensor y enviar OSC."""
    msg = OSCMessage(f"/sensor/{data.type.value}", [data.x, data.y, data.z])
    comm_manager.send_osc(msg, "localhost:8000")

# Registrar callback y procesar
sensor_manager.register_callback(SensorType.ACCELEROMETER, process_sensor_data)
sensor_manager.start()
comm_manager.start()

# Simular dato de sensor
sensor_data = SensorData(
    type=SensorType.ACCELEROMETER,
    x=0.1, y=0.2, z=0.3,
    timestamp=0.0
)
sensor_manager.record_data(SensorType.ACCELEROMETER, sensor_data)

sensor_manager.stop()
comm_manager.stop()
```

**Para un ejemplo completo y funcional**, ejecuta:
```bash
python examples/integrated_demo.py
```

## 📁 Estructura del Proyecto

```
app/
├── README.md                          # Este archivo
├── CONTEXTO.md                        # Contexto del proyecto
├── METODOLOGIA_DESARROLLO.md          # Metodología de desarrollo
├── requirements.txt                   # Dependencias
├── venv/                              # Entorno virtual (ignorado)
├── src/                               # Código fuente
│   ├── app.py                        # Módulo principal
│   ├── sensors.py                    # Gestor de sensores del iPhone
│   ├── communication.py              # Comunicación MIDI/OSC
│   └── utils/                        # Utilidades
│       ├── __init__.py
│       └── helpers.py                # Funciones matemáticas
├── tests/                             # Pruebas
│   ├── README.md                     # Instrucciones de testing
│   ├── conftest.py                   # Configuración pytest
│   ├── test_app.py                   # Tests del módulo app
│   ├── test_sensors.py               # Tests del módulo sensors
│   ├── test_communication.py         # Tests del módulo communication
│   └── test_utils.py                 # Tests del módulo utils
├── docs/                              # Documentación
│   ├── BITACORA.md                   # Log de desarrollo
│   ├── CURSOR_GUIDE.md               # Guía para IA
│   ├── roadmap_v1.md                  # Plan de desarrollo
│   └── TUTORIAL.md                   # Tutorial de uso
└── examples/                          # Ejemplos
    └── integrated_demo.py            # Demo integrada sensores → OSC/MIDI
```

## 🧪 Testing

```bash
# Ejecutar todos los tests
pytest

# Con cobertura
pytest --cov=src --cov-report=html

# Tests específicos
pytest tests/test_communication.py -v
```

## 🎬 Ejemplos

### Ejemplo Integrado: Sensores → OSC/MIDI

```bash
# Ejecutar ejemplo completo
python examples/integrated_demo.py
```

Este ejemplo demuestra:
- Captura de datos de sensores simulados
- Conversión a mensajes OSC con normalización
- Conversión a eventos MIDI
- Envío real de mensajes
- Historial de comunicación

## 📚 Documentación

- **BITACORA**: Registro completo de desarrollo en `docs/BITACORA.md`
- **Roadmap**: Plan de desarrollo y estado actual en `docs/roadmap_v1.md`
- **Metodología**: Guía de desarrollo en `METODOLOGIA_DESARROLLO.md`
- **Contexto**: Información del proyecto en `CONTEXTO.md`

**Para más detalles sobre el roadmap**:
- Fase 1-4: ✅ Completadas (Configuración, Core, Tests, Integración)
- Fase 5: 🔄 En progreso (Ejemplos y Demos)
- Fase 6: ⏳ Pendiente (Migración a C++/openFrameworks)

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'WIP: Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles (si aplica).

## 👨‍💻 Autor

**Assiz Alcaraz Baxter**
- GitHub: [@assizalcaraz](https://github.com/assizalcaraz)

---

## 📊 Estado Actual del Proyecto

**Última Actualización**: 2025-10-26

**Estado**: Fase 4 completada - Integración OSC/MIDI funcional

- ✅ Entorno virtual configurado
- ✅ Bibliotecas python-osc y python-rtmidi integradas
- ✅ Envío real de mensajes OSC y MIDI funcionando
- ✅ 47 tests pasando (89% cobertura)
- ✅ Ejemplo integrado disponible (`examples/integrated_demo.py`)
- 🔄 Próximo: Documentación de casos de uso y preparación para migración a C++/openFrameworks

**Repositorio**: [openFramework_iOS](https://github.com/assizalcaraz/openFramework_iOS.git)
