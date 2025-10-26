# Notas sobre openFrameworks

**Fecha**: 2025-10-26  
**Fuente**: [openframeworks.cc](https://openframeworks.cc/)

---

## 📚 Información sobre openFrameworks

### ¿Qué es openFrameworks?

**openFrameworks** es un toolkit open source de C++ diseñado para creative coding. Proporciona herramientas simples y intuitivas para programación creativa, lo que lo hace ideal para:

- Instalaciones artísticas interactivas
- Visualización de datos
- Arte generativo
- Proyectos multimedia

### Versión Actual

- **Versión**: 0.12.1 (la más reciente)
- **Lenguaje**: C++
- **Estado**: Activo y en desarrollo

### Características Principales

1. **Cross-platform**: Funciona en Windows, macOS, Linux, iOS, Android
2. **Addons**: Sistema extensible de complementos
3. **Comunidad**: Foro activo, GitHub, Slack
4. **Documentación**: Bien documentado con tutoriales

---

## 🎯 Relación con este Proyecto

### Objetivo Final

El objetivo de este proyecto es construir una aplicación usando **openFrameworks 0.12** para iPhone 15 que:

1. **Utilice sensores del dispositivo** (acelerómetro, giroscopio, brújula)
2. **Se comunique vía MIDI/OSC** para controlar instalaciones artísticas
3. **Transforme el iPhone en un instrumento de dibujo** interactivo

### Enfoque del Proyecto Actual (Python)

Este repositorio Python es una **fase de investigación preliminar** que:

- ✅ **Prototipa la lógica** de sensores y comunicación
- ✅ **Experimenta con MIDI/OSC** antes de implementarlo en C++
- ✅ **Desarrolla algoritmos** de procesamiento de datos
- ✅ **Documenta el flujo** de trabajo y casos de uso
- 🔄 **Prepara el camino** para la implementación en C++

### Arquitectura Futura

```
Fase 1 (Actual): Python Prototype
├── src/sensors.py          → Investigación de sensores
├── src/communication.py    → Experimentación MIDI/OSC
└── src/utils/              → Algoritmos de procesamiento

Fase 2 (Futuro): iOS App con openFrameworks
├── main.cpp                → Aplicación openFrameworks
├── sensor_handler.h        → Gestor de sensores iOS
├── midi_osc_handler.h      → Comunicación MIDI/OSC
└── drawing_engine.h        → Motor de dibujo interactivo
```

---

## 🔗 Recursos de openFrameworks

### Enlaces Oficiales

- **Web**: https://openframeworks.cc/
- **Documentación**: https://openframeworks.cc/documentation/
- **Foro**: https://forum.openframeworks.cc/
- **GitHub**: https://github.com/openframeworks/openframeworks
- **Addons**: https://ofxaddons.com/
- **Slack**: Comunidad en Slack para soporte en tiempo real

### Recursos de Aprendizaje

1. **Documentation**: Referencia completa de clases y funciones
2. **Tutorials**: Guías paso a paso
3. **Examples**: Ejemplos de código en la web
4. **Forum**: Comunidad para preguntas y compartir trabajo

### Para iOS

- **openFrameworks iOS**: La versión para iOS incluye soporte para:
  - Sensores del dispositivo
  - Comunicación de red
  - OpenGL ES
  - Cámara y micrófono
  - Integración con frameworks nativos de iOS

---

## 📋 Próximos Pasos

### Investigación Continua

1. Estudiar estructura de proyecto openFrameworks para iOS
2. Revisar addons disponibles para MIDI/OSC
3. Investigar acceso a sensores en openFrameworks iOS
4. Documentar patrones de comunicación OSC

### Migración de Python a C++

El código Python actual servirá como **blueprint** para la implementación en C++:

```python
# Python (prototipo)
sensor_manager.record_data(sensor_type, data)
comm_manager.send_osc(message, target)
```

```cpp
// C++ (implementación futura en openFrameworks)
void ofApp::recordSensorData(SensorType type, SensorData data) {
    // Implementación en C++
}

void ofApp::sendOSC(ofxOscMessage& msg, string target) {
    // Envío OSC en C++
}
```

---

## 🎨 Casos de Uso Objetivo

### Instalación Artística Interactiva

1. **Usuario mueve el iPhone** → Sensores detectan movimiento
2. **Datos se procesan** → Se generan valores para comunicación
3. **Se envía OSC/MIDI** → A instalación externa (TouchDesigner, Max/MSP, etc.)
4. **Instalación reacciona** → Visualización/sonido responden al movimiento

### Referencias

- Controladores MIDI/OSC existentes
- Instalaciones artísticas donde usuarios interactúan con dispositivos como instrumentos
- Sistemas de tracking y mapeo de datos en tiempo real

---

**Última Actualización**: 2025-10-26  
**Referencia**: [openframeworks.cc](https://openframeworks.cc/)
