"""
Módulo de comunicación MIDI/OSC.

Proporciona funcionalidades para enviar y recibir mensajes MIDI/OSC
desde el dispositivo iPhone para controlar instalaciones artísticas.

Autor: Assiz Alcaraz Baxter
Fecha: 2025-10-26
"""

import logging
from typing import Dict, Optional, List
from datetime import datetime

logger = logging.getLogger(__name__)


class OSCMessage:
    """Representa un mensaje OSC."""
    
    def __init__(self, address: str, args: List = None):
        """
        Inicializar mensaje OSC.
        
        Args:
            address: Dirección OSC (ej: "/instrument/x")
            args: Argumentos del mensaje
        """
        self.address = address
        self.args = args or []
        self.timestamp = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convertir a diccionario."""
        return {
            "address": self.address,
            "args": self.args,
            "timestamp": self.timestamp.isoformat()
        }
    
    def __str__(self) -> str:
        """Representación como string."""
        return f"{self.address} {self.args}"


class MIDIEvent:
    """Representa un evento MIDI."""
    
    def __init__(self, note: int, velocity: int, channel: int = 0):
        """
        Inicializar evento MIDI.
        
        Args:
            note: Nota MIDI (0-127)
            velocity: Velocidad (0-127)
            channel: Canal MIDI (0-15)
        """
        self.note = note
        self.velocity = velocity
        self.channel = channel
        self.timestamp = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convertir a diccionario."""
        return {
            "note": self.note,
            "velocity": self.velocity,
            "channel": self.channel,
            "timestamp": self.timestamp.isoformat()
        }
    
    def __str__(self) -> str:
        """Representación como string."""
        return f"MIDI[ch{self.channel}] note={self.note} vel={self.velocity}"


class CommunicationManager:
    """
    Gestor de comunicación MIDI/OSC.
    
    Maneja el envío y recepción de mensajes para controlar
    instalaciones artísticas externas.
    """
    
    def __init__(self):
        """Inicializar el gestor de comunicación."""
        self.osc_clients: Dict[str, any] = {}  # Guardará clientes OSC cuando se implemente
        self.midi_outputs: List[any] = []  # Guardará salidas MIDI cuando se implemente
        self.message_history: List[Dict] = []
        self.is_active = False
        logger.info("CommunicationManager inicializado")
    
    def send_osc(self, message: OSCMessage, target: str = "localhost:8000") -> None:
        """
        Enviar mensaje OSC.
        
        Args:
            message: Mensaje OSC a enviar
            target: Destino en formato "host:port"
        """
        try:
            logger.info(f"Enviando OSC: {message}")
            # TODO: Implementar envío real con python-osc
            self.message_history.append({
                "type": "osc",
                "message": message.to_dict(),
                "target": target
            })
        except Exception as e:
            logger.error(f"Error enviando OSC: {e}")
    
    def send_midi(self, event: MIDIEvent) -> None:
        """
        Enviar evento MIDI.
        
        Args:
            event: Evento MIDI a enviar
        """
        try:
            logger.info(f"Enviando MIDI: {event}")
            # TODO: Implementar envío real con python-rtmidi
            self.message_history.append({
                "type": "midi",
                "message": event.to_dict()
            })
        except Exception as e:
            logger.error(f"Error enviando MIDI: {e}")
    
    def map_sensor_to_osc(self, sensor_value: float, osc_min: float, osc_max: float) -> float:
        """
        Mapear valor de sensor a rango OSC.
        
        Args:
            sensor_value: Valor del sensor
            osc_min: Mínimo del rango OSC
            osc_max: Máximo del rango OSC
            
        Returns:
            Valor mapeado
        """
        # Normalizar a rango [0, 1] y mapear
        normalized = max(0, min(1, sensor_value))
        return osc_min + (osc_max - osc_min) * normalized
    
    def map_sensor_to_midi(self, sensor_value: float) -> int:
        """
        Mapear valor de sensor a nota MIDI.
        
        Args:
            sensor_value: Valor del sensor
            
        Returns:
            Nota MIDI (0-127)
        """
        import math
        normalized = max(0, min(1, sensor_value))
        return int(127 * normalized)
    
    def start(self) -> None:
        """Iniciar comunicación."""
        self.is_active = True
        logger.info("Comunicación iniciada")
    
    def stop(self) -> None:
        """Detener comunicación."""
        self.is_active = False
        logger.info("Comunicación detenida")
    
    def get_history(self, count: Optional[int] = None) -> List[Dict]:
        """
        Obtener historial de mensajes.
        
        Args:
            count: Número de mensajes a obtener (None para todos)
            
        Returns:
            Lista de mensajes
        """
        if count is None:
            return self.message_history
        return self.message_history[-count:]
