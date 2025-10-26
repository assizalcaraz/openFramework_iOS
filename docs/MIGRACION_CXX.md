# Migración a C++ / openFrameworks

## 📍 Estado: Fase 6 - EN PROGRESO

**Fecha de Inicio**: 2025-10-26  
**Directorio**: `/Users/joseassizalcarazbaxter/Developer/iphone/build`

---

## 🎯 Objetivo

Migrar el prototipo de investigación en Python a una aplicación nativa en C++ usando openFrameworks 0.12 para iPhone 15.

---

## ✅ Progreso Actual

### Estructura del Proyecto

```
build/
├── src/
│   ├── main.cpp                          # Entrada principal openFrameworks
│   ├── ofApp.h                           # Clase principal (modificada)
│   ├── ofApp.cpp                         # Implementación (modificada)
│   └── modules/                          # Módulos migrados de Python
│       ├── Utils.hpp                     # Funciones matemáticas
│       ├── SensorManager.h              # Gestor de sensores
│       ├── SensorManager.cpp             # Implementación sensores
│       ├── CommunicationManager.h       # Gestor MIDI/OSC
│       └── CommunicationManager.cpp     # Implementación comunicación
├── addons.make                           # Addons configurados
└── Makefile                             # Configuración de compilación
```

### Addons de openFrameworks Instalados

- ✅ **ofxOsc**: Comunicación OSC
- ✅ **ofxMidi**: Comunicación MIDI  
- ✅ **ofxGui**: Interfaz gráfica

---

## 🔄 Migración Realizada

### 1. Utils.hpp (Migrado de `src/utils/helpers.py`)

**Funciones migradas**:
```cpp
float calculateMagnitude(float x, float y, float z);
void normalizeVector(float x, float y, float z, float& outX, float& outY, float& outZ);
float mapValue(float value, float fromMin, float fromMax, float toMin, float toMax);
int mapSensorToMidi(float sensorValue);
```

### 2. SensorManager (Migrado de `src/sensors.py`)

**Características**:
- Sistema de callbacks usando `std::function<void(const SensorData&)>`
- Registro histórico (últimos 100 registros por tipo)
- Soporte para: Accelerometer, Gyroscope, Magnetometer, Gravity, UserAcceleration
- Gestión de estado (start/stop)

**API**:
```cpp
void registerCallback(SensorType sensorType, Callback callback);
void recordData(SensorType sensorType, const SensorData& data);
std::vector<SensorData> getData(SensorType sensorType, int count = -1);
void start();
void stop();
```

### 3. CommunicationManager (Migrado de `src/communication.py`)

**Características**:
- Comunicación OSC usando `ofxOsc`
- Comunicación MIDI usando `ofxMidi`
- Historial de mensajes
- Mapeo de valores a OSC/MIDI

**API**:
```cpp
void sendOSC(const OSCMessage& message, const std::string& target);
void sendMIDI(const MIDIEvent& event);
float mapSensorToOSC(float sensorValue, float oscMin, float oscMax);
int mapSensorToMIDI(float sensorValue);
```

### 4. Integración en ofApp

**Modificaciones en `ofApp.h`**:
- Incluidos módulos `SensorManager` y `CommunicationManager`
- Añadido callback `onSensorData()` para procesar datos

**Modificaciones en `ofApp.cpp`**:
- `setup()`: Inicializa sensores y comunicación
- `update()`: Simula datos de sensores (temporal)
- `draw()`: Muestra estado y últimos mensajes OSC
- `onSensorData()`: Convierte datos de sensores a OSC/MIDI

---

## 🔄 Flujo de Datos Implementado

```
┌─────────────────┐
│  Sensor iOS     │ (Pendiente: CoreMotion)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ SensorManager   │ (Callbacks + Historial)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  onSensorData() │ (Normalización + Mapeo)
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌────────┐ ┌────────┐
│  OSC   │ │  MIDI  │
└────────┘ └────────┘
```

---

## ⏳ Pendiente

### Alta Prioridad
- [ ] Integrar sensores nativos de iOS usando CoreMotion
- [ ] Compilar proyecto para iOS
- [ ] Testing en dispositivo real iPhone 15
- [ ] Corregir errores de compilación

### Media Prioridad
- [ ] Optimizar rendimiento para 60fps
- [ ] Implementar sistema de dibujo interactivo
- [ ] Añadir configuración de puertos MIDI/OSC
- [ ] Manejo de errores y logging

### Baja Prioridad
- [ ] Tests unitarios en C++
- [ ] Documentación de API en C++
- [ ] Optimización de memoria
- [ ] UI/UX mejorada

---

## 📝 Notas de Desarrollo

### Dependencias
- **openFrameworks**: 0.12 (o posterior)
- **Xcode**: 14.0+
- **iOS**: 15.0+ (Deployment Target)

### Estructura de Build
- El proyecto se puede abrir con Xcode: `build.xcodeproj`
- Compilación: `make` o desde Xcode
- Directorio de salida: `bin/`

### Diferencias con Python
1. **Sensores**: En Python son simulados; en C++ usar CoreMotion nativo
2. **Callbacks**: Python usa funciones; C++ usa `std::function`
3. **Historial**: Mismo límite (100), pero implementación diferente
4. **Comunicación**: Python usa python-osc/python-rtmidi; C++ usa ofxOsc/ofxMidi

---

## 🚀 Comandos Útiles

```bash
# Compilar proyecto
cd build
make

# Abrir en Xcode
open build.xcodeproj

# Limpiar build
make clean

# Run (en simulador/device)
# Desde Xcode: Cmd+R
```

---

**Última Actualización**: 2025-10-26  
**Estado**: Migración inicial completada, pendiente sensores nativos iOS

