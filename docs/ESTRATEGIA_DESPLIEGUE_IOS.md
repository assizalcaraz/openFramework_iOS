# Estrategia de Despliegue iOS - app

## 📊 Evaluación de Estrategia Actual

### Estado Actual
- ✅ Estructura de módulos C++ creada
- ✅ Addons openFrameworks configurados (ofxOsc, ofxMidi, ofxGui)
- ✅ Comunicación implementada (emisor)
- ❌ Receptor no implementado
- ❌ Sensores iOS nativos pendientes
- ❌ Testing de comunicación pendiente

---

## 🎯 Objetivo: Arquitectura Emisor/Receptor

```
┌─────────────────────────────────────┐
│         iPhone (app openFrameworks) │
│                                      │
│  ┌────────────┐                        │
│  │ Sensores  │──┐                     │
│  │  iOS      │  │                     │
│  └──────────┘  │                     │
│                ▼                     │
│  ┌─────────────────┐                │
│  │ SensorManager   │                │
│  └────────┬────────┘                │
│           │                         │
│           ▼                         │
│  ┌──────────────────┐              │
│  │ CommunicationMgr │  ───► OSC/MIDI│
│  └──────────────────┘              │
└─────────────────────────────────────┘
         │              │
         ▼              ▼
    ┌────────┐    ┌──────────┐
    │  OSC    │    │   MIDI   │ (LAN/Bluetooth)
    │ Server  │    │   Device │
    └─────────┘    └──────────┘
         │              │
         ▼              ▼
    ┌─────────────────────┐
    │ Instalación Artística│
    │   (Receptor/Target) │
    └─────────────────────┘
```

---

## 🔌 Conexiones: MIDI/OSC en openFrameworks

### Comunicación OSC

**Cómo funciona**:
```cpp
// ofxOsc usa UDP sobre IP
ofxOscSender sender;
sender.setup("192.168.1.100", 8000);  // host:port

// Enviar mensaje
ofxOscMessage msg;
msg.setAddress("/sensor/accelerometer");
msg.addFloatArg(x);
msg.addFloatArg(y);
msg.addFloatArg(z);
sender.sendMessage(msg, false);
```

**Opciones de conexión**:
1. **LAN/WiFi**: `sender.setup("192.168.1.100", 8000)` - Más común
2. **Localhost**: `sender.setup("127.0.0.1", 8000)` - Testing
3. **Bluetooth**: Requiere configuración adicional (menos común para OSC)

### Comunicación MIDI

**Cómo funciona**:
```cpp
// ofxMidi conecta a puertos MIDI del sistema
ofxMidiOut midiOut;
midiOut.listPorts();  // Ver puertos disponibles
midiOut.openPort(0);   // Abrir primer puerto
midiOut.sendNoteOn(0, 64, 127);  // channel, note, velocity
```

**Opciones de conexión**:
1. **MIDI virtual**: Loopback (IAC Driver en macOS)
2. **Network MIDI**: Bluetooth o WiFi
3. **MIDI hardware**: USB/Bluetooth MIDI interfaces

---

## 🧪 Estrategia de Testing y Validación

### Fase 1: Testing Local (localhost) ✅ PRIORIDAD

**Objetivo**: Validar comunicación antes de despliegue iOS

#### 1.1 OSC Local Testing

**Emisor** (app openFrameworks):
```cpp
// En ofApp.cpp
void ofApp::setup() {
    commManager.sendOSC(msg, "localhost:8000");
}
```

**Receptor de Prueba** (implementar uno):
```cpp
// Crear: src/modules/OSCReceiver.h
class OSCReceiver {
public:
    ofxOscReceiver receiver;
    
    void setup(int port) {
        receiver.setup(port);
    }
    
    void update() {
        while (receiver.hasWaitingMessages()) {
            ofxOscMessage msg;
            receiver.getNextMessage(msg);
            ofLog() << "Received: " << msg.getAddress();
            // Constatar recepción
        }
    }
};
```

#### 1.2 MIDI Local Testing

**Simular MIDI local**:
- macOS: Activar "IAC Driver" en Audio MIDI Setup
- Usar PuTTY o aplicaciones MIDI Monitors para ver mensajes

---

### Fase 2: Testing en Red Local (LAN) 📡

**Configuración**:
```cpp
// Detectar IP del target
std::string targetIP = "192.168.1.100";
commManager.sendOSC(msg, targetIP + ":8000");
```

**Receptor en otra app/dispositivo**:
- Max MSP, Pure Data, TouchDesigner
- O crear otra app openFrameworks como receptor

---

### Fase 3: Despliegue Mínimo iOS 🚀

**Recomendación**: Sí, conviene hacer despliegue mínimo primero

#### Estrategia Incremental:

**3.1 Despliegue Básico** (UI desconectada)
- [ ] Crear interfaz mínima con visualización
- [ ] Mostrar datos de sensores simulados
- [ ] Comprobar que compila para iOS
- [ ] Validar en simulador iOS
- [ ] **NO preocuparse aún por OSC/MIDI real**

**3.2 Despliegue con Visualización de Red**
- [ ] Mostrar estado de OSC (conectado/desconectado)
- [ ] Mostrar IP local y target IP
- [ ] Botones para activar/desactivar comunicación
- [ ] Indicadores visuales de mensajes enviados

**3.3 Despliegue con Comunicación Local**
- [ ] Activar OSC localhost
- [ ] Conectar a receptor de pruebas en Mac
- [ ] Validar flujo completo sensores → OSC

**3.4 Despliegue Final con Sensores Reales**
- [ ] Integrar CoreMotion para sensores iOS nativos
- [ ] Probar en dispositivo real iPhone
- [ ] Validar performance (objetivo: 60fps)

---

## 🛠 Implementación: Emisor/Receptor Diferenciado

### Opción A: Misma app (Modo Emisor/Receptor)

```cpp
// ofApp.h
class ofApp {
    bool isReceiver;  // true = receptor, false = emisor
    
    // Como emisor
    CommunicationManager commManager;
    
    // Como receptor
    OSCReceiver receiver;
    
public:
    void toggleMode();
};
```

### Opción B: Apps Separadas (RECOMENDADO)

**Estructura**:
```
build/
├── app_sender/        # App emisora (iPhone)
│   ├── src/
│   │   └── modules/
│   │       ├── SensorManager.*
│   │       └── CommunicationManager.*
│
└── app_receiver/     # App receptora (Mac/otros)
    ├── src/
    │   └── modules/
    │       └── OSCReceiver.*
```

**Ventajas**:
- Separación clara de responsabilidades
- Testing independiente
- Reutilización de código
- Puedes correr receptor en Mac para probar

---

## 📝 Plan de Implementación Inmediato

### PASO 1: Crear OSCReceiver Module ⚡ AHORA

**Archivos a crear**:
- `src/modules/OSCReceiver.h`
- `src/modules/OSCReceiver.cpp`

**Funcionalidad**:
```cpp
class OSCReceiver {
public:
    void setup(int port);
    void update();
    void draw();  // Visualización de mensajes
    bool isMessageReceived();
    std::vector<ofxOscMessage> getMessages();
};
```

### PASO 2: Modo Testing en ofApp

**Agregar toggle**:
```cpp
// ofApp.h
enum class AppMode { SENDER, RECEIVER, BOTH };

AppMode currentMode;
```

### PASO 3: Despliegue Mínimo iOS

**Objetivos**:
1. Compilar para iOS (sin sensores reales)
2. UI básica funcionando
3. Datos simulados visibles
4. Validar que no hay crashs

---

## 🎮 Estrategia de Constatar Comunicación

### Visual Indicators

```cpp
void ofApp::draw() {
    // Estado de conexión
    if (receiver.isMessageReceived()) {
        ofSetColor(0, 255, 0);  // Verde = funciona
    } else {
        ofSetColor(255, 0, 0);  // Rojo = no funciona
    }
    ofDrawCircle(50, 50, 20);
    
    // Contador de mensajes
    ofDrawBitmapString("Messages: " + to_string(msgCount), 20, 80);
}
```

### Logging

```cpp
void ofApp::onOSCMessage(const ofxOscMessage& msg) {
    ofLogNotice() << "OSC Received: " << msg.getAddress();
    
    // Guardar timestamp
    messageTimestamps.push_back(ofGetElapsedTimef());
}
```

### Historial Visual

- Timestamp de último mensaje
- Gráfica de frecuencia de mensajes
- Lista de últimos mensajes OSC

---

## 🚀 Comandos Útiles

### Testing OSC en Mac (antes de iOS)

```bash
# Usar OSCLogger (herramienta macOS)
# O crear receptor simple con:

# Receptor de prueba en Python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 8000))
while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received: {data} from {addr}")
```

### MIDI Testing

```bash
# macOS: Audio MIDI Setup
# Activar "IAC Driver" para loopback virtual
open "/Applications/Utilities/Audio MIDI Setup.app"

# Ver mensajes MIDI en consola
# o usar aplicaciones como MIDI Monitor
```

---

## 📊 Checklist de Despliegue

### Pre-despliegue
- [ ] Comunicación OSC funcionando en Mac
- [ ] Comunicación MIDI funcionando en Mac
- [ ] Receptor de pruebas implementado
- [ ] Logs y visualización funcionando

### Despliegue Mínimo iOS
- [ ] Compila para iOS (simulador)
- [ ] UI básica visibile
- [ ] Datos simulados se muestran
- [ ] No hay crashs

### Despliegue Completo
- [ ] Sensores iOS nativos funcionando
- [ ] OSC se envía desde iOS
- [ ] MIDI se envía desde iOS
- [ ] Receptor externo recibe mensajes
- [ ] Performance estable (60fps)
- [ ] Testing en dispositivo real iPhone

---

**Recomendación FINAL**: 
1. ✅ Implementar OSCReceiver AHORA
2. ✅ Hacer despliegue mínimo iOS (UI solo)
3. ✅ Conectar comunicación en fases incrementales
4. ✅ Validar cada fase antes de continuar

**Última Actualización**: 2025-10-26

