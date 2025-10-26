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

# Intentar importar bibliotecas OSC y MIDI
try:
    from pythonosc import udp_client
    from pythonosc.osc_message_builder import OscMessageBuilder
    OSC_AVAILABLE = True
except ImportError:
    OSC_AVAILABLE = False
    logger.warning("python-osc no disponible, solo envío simulado")

try:
    import rtmidi
    MIDI_AVAILABLE = True
except ImportError:
    MIDI_AVAILABLE = False
    logger.warning("python-rtmidi no disponible, solo envío simulado")


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
        self.osc_clients: Dict[str, any] = {}  # Guardará clientes OSC
        self.midi_output = None  # Guardará salida MIDI
        self.message_history: List[Dict] = []
        self.is_active = False
        
        # Inicializar MIDI si está disponible
        if MIDI_AVAILABLE:
            try:
                self.midi_output = rtmidi.MidiOut()
                available_ports = self.midi_output.get_ports()
                if available_ports:
                    self.midi_output.open_port(0)
                    logger.info(f"MIDI inicializado - Puerto: {available_ports[0]}")
                else:
                    logger.warning("No hay puertos MIDI disponibles")
            except Exception as e:
                logger.error(f"Error inicializando MIDI: {e}")
        
        logger.info("CommunicationManager inicializado")
    
    def _get_or_create_osc_client(self, target: str):
        """
        Obtener o crear un cliente OSC para el destino especificado.
        
        Args:
            target: Destino en formato "host:port"
            
        Returns:
            Cliente OSC o None si hubo error
        """
        if target in self.osc_clients:
            return self.osc_clients[target]
        
        if not OSC_AVAILABLE:
            logger.warning("python-osc no disponible, no se puede enviar OSC real")
            return None
        
        try:
            host, port_str = target.split(":")
            port = int(port_str)
            client = udp_client.UDPClient(host, port)
            self.osc_clients[target] = client
            logger.info(f"Cliente OSC creado para {target}")
            return client
        except Exception as e:
            logger.error(f"Error creando cliente OSC para {target}: {e}")
            return None
    
    def send_osc(self, message: OSCMessage, target: str = "localhost:8000") -> None:
        """
        Enviar mensaje OSC.
        
        Args:
            message: Mensaje OSC a enviar
            target: Destino en formato "host:port"
        """
        try:
            logger.info(f"Enviando OSC: {message}")
            
            # Intentar envío real si está disponible
            client = self._get_or_create_osc_client(target)
            if client is not None and OSC_AVAILABLE:
                builder = OscMessageBuilder(message.address)
                for arg in message.args:
                    builder.add_arg(arg)
                osc_msg = builder.build()
                client.send(osc_msg)
                logger.debug(f"OSC enviado realmente a {target}")
            else:
                logger.debug(f"OSC simulado (sin cliente real)")
            
            # Registrar en historial
            self.message_history.append({
                "type": "osc",
                "message": message.to_dict(),
                "target": target,
                "sent": client is not None
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
            
            # Intentar envío real si está disponible
            sent = False
            if self.midi_output is not None and MIDI_AVAILABLE:
                try:
                    # Construir mensaje MIDI: [status byte, note, velocity]
                    # Status: 0x90 + channel (Note On), 0x80 + channel (Note Off)
                    status = 0x90 | (event.channel & 0x0F)
                    midi_msg = [status, event.note & 0x7F, event.velocity & 0x7F]
                    self.midi_output.send_message(midi_msg)
                    logger.debug("MIDI enviado realmente")
                    sent = True
                except Exception as e:
                    logger.error(f"Error enviando MIDI real: {e}")
            else:
                logger.debug("MIDI simulado (sin salida real)")
            
            # Registrar en historial
            self.message_history.append({
                "type": "midi",
                "message": event.to_dict(),
                "sent": sent
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
        
        # Cerrar salida MIDI
        if self.midi_output is not None:
            try:
                self.midi_output.close_port()
                logger.info("Salida MIDI cerrada")
            except Exception as e:
                logger.error(f"Error cerrando MIDI: {e}")
        
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
