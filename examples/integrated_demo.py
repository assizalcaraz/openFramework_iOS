"""
Ejemplo de uso integrado: Sensores → OSC/MIDI

Este ejemplo demuestra cómo usar el módulo de comunicación
para enviar datos de sensores como mensajes OSC o eventos MIDI.

Autor: Assiz Alcaraz Baxter
Fecha: 2025-10-26
"""

import sys
import time
import logging
from pathlib import Path

# Agregar src al path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from sensors import SensorManager, SensorType, SensorData
from communication import CommunicationManager, OSCMessage, MIDIEvent
from utils.helpers import normalize_vector, map_value

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def sensor_to_osc_callback(data: SensorData):
    """
    Callback que envía datos de sensores como mensaje OSC.
    
    Args:
        data: Datos del sensor
    """
    # Normalizar el vector (x, y, z)
    nx, ny, nz = normalize_vector(data.x, data.y, data.z)
    
    # Crear mensaje OSC con datos normalizados
    msg = OSCMessage(
        address=f"/sensor/{data.type.value}",
        args=[nx, ny, nz]
    )
    
    # Enviar a un receptor OSC (por ejemplo, Pure Data, Max, etc.)
    comm_manager.send_osc(msg, target="localhost:8000")
    logger.info(f"OSC enviado: {msg}")


def sensor_to_midi_callback(data: SensorData):
    """
    Callback que envía datos de sensores como evento MIDI.
    
    Args:
        data: Datos del sensor
    """
    # Calcular magnitud del vector aceleración
    magnitude = (data.x**2 + data.y**2 + data.z**2)**0.5
    
    # Mapear magnitud a nota MIDI (0-127)
    note = comm_manager.map_sensor_to_midi(magnitude / 20.0)  # Normalizar
    
    # Crear evento MIDI
    event = MIDIEvent(
        note=note,
        velocity=comm_manager.map_sensor_to_midi(abs(data.y) / 10.0),
        channel=0
    )
    
    # Enviar evento MIDI
    comm_manager.send_midi(event)
    logger.info(f"MIDI enviado: {event}")


def simulate_sensor_data():
    """
    Simula datos de sensores para testing.
    
    En una app real, estos datos vendrían del dispositivo iOS.
    """
    import random
    
    # Simular acelerómetro
    for i in range(10):
        data = SensorData(
            type=SensorType.ACCELEROMETER,
            x=random.uniform(-2, 2),
            y=random.uniform(-2, 2),
            z=random.uniform(-2, 2),
            timestamp=time.time()
        )
        
        sensor_manager.record_data(SensorType.ACCELEROMETER, data)
        time.sleep(0.1)  # Simular intervalo de muestreo


def main():
    """
    Función principal que ejecuta la demostración.
    """
    global sensor_manager, comm_manager
    
    logger.info("=== DEMO: Sensores → OSC/MIDI ===")
    
    # Inicializar gestores
    sensor_manager = SensorManager()
    comm_manager = CommunicationManager()
    
    # Registrar callbacks
    sensor_manager.register_callback(
        SensorType.ACCELEROMETER, 
        sensor_to_osc_callback
    )
    sensor_manager.register_callback(
        SensorType.ACCELEROMETER,
        sensor_to_midi_callback
    )
    
    # Iniciar captura
    sensor_manager.start()
    comm_manager.start()
    
    logger.info("Iniciando captura de sensores...")
    logger.info("Simulando datos de acelerómetro...")
    
    # Simular datos
    simulate_sensor_data()
    
    # Mostrar historial
    logger.info("\n=== Historial de Mensajes ===")
    history = comm_manager.get_history()
    for i, msg in enumerate(history[-5:], 1):
        logger.info(f"{i}. {msg}")
    
    # Detener
    sensor_manager.stop()
    comm_manager.stop()
    
    logger.info("\n=== DEMO Finalizada ===")


if __name__ == "__main__":
    main()

