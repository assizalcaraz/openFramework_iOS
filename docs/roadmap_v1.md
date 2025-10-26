# Roadmap v1 - app

**Fecha**: 2025-10-26  
**Objetivo**: Trabajo preliminar de investigación para construir app openFrameworks 0.12 en iPhone 15  
**Estado**: Fase 1-2 Completada (Investigación en Python)

---

## 🎯 Objetivo Principal

Construir una aplicación iOS con **openFrameworks 0.12** para iPhone 15 que:
- Utilice sensores del dispositivo (acelerómetro, giroscopio, brújula)
- Se comunique vía **MIDI/OSC** para controlar instalaciones artísticas
- Transforme el iPhone en **instrumento de dibujo interactivo**

### Contexto del Proyecto

Este repositorio Python es la **fase de investigación preliminar** antes de construir la app nativa en C++. La app final será en C++ usando [openFrameworks](https://openframeworks.cc/).

---

## 📋 Fases de Desarrollo

### Fase 1: Configuración Inicial ✅ COMPLETADA
- [x] Estructura de directorios
- [x] Archivos de configuración
- [x] Sistema de documentación
- [x] Control de versiones (Git)
- [x] Pre-Cursor supervisor configurado
- [x] .cursor/ estructura creada

### Fase 2: Módulos Core (Python) ✅ COMPLETADA
- [x] **app.py**: Clase principal de la aplicación
- [x] **sensors.py**: Gestor de sensores del iPhone (SensorManager)
- [x] **communication.py**: Gestor MIDI/OSC (CommunicationManager)
- [x] **utils/helpers.py**: Funciones de procesamiento matemático
- [x] Sistema de logging configurado
- [x] Callbacks para sensores implementados
- [x] Mapeo valores sensor → MIDI/OSC

### Fase 3: Testing y Validación ✅ COMPLETADA
- [x] Suite de tests completa (47 tests)
- [x] Fixtures compartidas (conftest.py)
- [x] Tests para app.py (7 tests)
- [x] Tests para sensors.py (10 tests)
- [x] Tests para communication.py (15 tests)
- [x] Tests para utils/helpers.py (15 tests)
- [x] Cobertura: 89% ✅
- [x] Todos los tests pasando ✅

### Fase 4: Integración con Bibliotecas 🔄 EN PROGRESO
- [ ] Instalar y configurar `python-osc`
- [ ] Instalar y configurar `python-rtmidi`
- [ ] Instalar y configurar `PyObjC` (acceso sensores iOS)
- [ ] Implementar envío OSC real
- [ ] Implementar envío MIDI real
- [ ] Acceso real a sensores del iPhone

### Fase 5: Ejemplos y Demos ⏳ PENDIENTE
- [ ] Ejemplo básico de uso sensores
- [ ] Ejemplo sensor → OSC
- [ ] Ejemplo sensor → MIDI
- [ ] Flujo completo instalación artística
- [ ] Documentación de casos de uso

### Fase 6: Migración a C++ / openFrameworks ⏳ PENDIENTE
- [ ] Investigar estructura proyecto openFrameworks iOS
- [ ] Crear proyecto iOS con openFrameworks
- [ ] Migrar lógica Python a C++
- [ ] Implementar sensores nativos iOS
- [ ] Implementar comunicación MIDI/OSC nativa
- [ ] Testing en dispositivo real iPhone 15

---

## 🚀 Funcionalidades Implementadas

### ✅ Python (Investigación Preliminar)
1. **Sistema de Sensores**:
   - SensorManager con callbacks
   - Registro histórico (últimos 100)
   - Tipos: Accelerometer, Gyroscope, Magnetometer

2. **Comunicación MIDI/OSC**:
   - OSCMessage y MIDIEvent
   - CommunicationManager
   - Historial de mensajes
   - Mapeo de valores

3. **Utilidades Matemáticas**:
   - Normalización de vectores
   - Cálculo de magnitud
   - Mapeo de rangos

### 🔄 Pendientes para Migración a C++
1. **openFrameworks iOS App**:
   - Main.cpp con ciclo openFrameworks
   - Sensor handlers nativos
   - MIDI/OSC handlers nativos
   - Drawing engine interactivo

---

## 📊 Métricas de Éxito

### ✅ Fase Python (Completada)
- [x] **Funcionalidad**: Módulos core implementados
- [x] **Testing**: Cobertura 89% (objetivo >80% ✅)
- [x] **Documentación**: Completa y actualizada
- [x] **Estructura**: Organizada y modular
- [x] **Git**: Control de versiones configurado

### 🎯 Fase C++ (Pendiente)
- [ ] **App nativa**: Compilando para iOS
- [ ] **Sensores**: Acceso real a dispositivos
- [ ] **Comunicación**: MIDI/OSC funcionando en dispositivo
- [ ] **Performance**: Tiempo de respuesta <16ms (60fps)
- [ ] **Testing**: Tests en dispositivo real

---

## 📝 Notas de Desarrollo

- **Metodología**: Seguir METODOLOGIA_DESARROLLO.md
- **Commits**: Usar convenciones WIP/FIX/FEAT/POINT
- **Testing**: Evaluar tests existentes antes de crear nuevos
- **Documentación**: Mantener BITACORA.md actualizada
- **Supervisión**: Usar Pre-Cursor supervisor para monitoreo automático

## 🔧 Uso de Cursor CLI Supervisor

### Iniciar Supervisión

```bash
# Supervisión única
cd /Users/joseassizalcarazbaxter/Developer/pre_cursor/src
python -m pre_cursor.cli supervisor start /Users/joseassizalcarazbaxter/Developer/iphone/app

# Supervisión continua (daemon)
python -m pre_cursor.cli supervisor start /Users/joseassizalcarazbaxter/Developer/iphone/app --daemon --interval 600
```

### Qué Supervisa

- ✅ Estructura del proyecto
- ✅ Archivos fuera de lugar
- ✅ Funciones duplicadas
- ✅ Calidad de tests
- ✅ Actualización automática de BITACORA.md

### Configuración

Ver: `.cursor/config/cursor_supervisor.yaml`

---

**Última Actualización**: 2025-10-26  
**Estado**: Fase 1-3 completadas (47 tests, 89% cobertura)
