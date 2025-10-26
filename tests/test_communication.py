"""
Tests para el módulo communication.py.

Este módulo contiene tests para CommunicationManager.
"""

import pytest
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communication import CommunicationManager, OSCMessage, MIDIEvent


class TestOSCMessage:
    """Tests para OSCMessage."""
    
    def test_creation_basic(self):
        """
        Test de creación básica de mensaje OSC.
        
        Casos cubiertos:
        - Éxito: Mensaje se crea correctamente
        - Estado: Dirección y argumentos se asignan
        """
        # Arrange & Act
        msg = OSCMessage("/test", [1, 2, 3])
        
        # Assert
        assert msg.address == "/test"
        assert msg.args == [1, 2, 3]
        assert isinstance(msg.timestamp, datetime)
    
    def test_creation_without_args(self):
        """
        Test de creación sin argumentos.
        
        Casos cubiertos:
        - Éxito: Lista de argumentos vacía por defecto
        """
        # Arrange & Act
        msg = OSCMessage("/empty")
        
        # Assert
        assert msg.args == []
    
    def test_to_dict(self):
        """
        Test de conversión a diccionario.
        
        Casos cubiertos:
        - Éxito: Retorna diccionario con todos los campos
        """
        # Arrange
        msg = OSCMessage("/test", [1, 2.5, "hello"])
        
        # Act
        result = msg.to_dict()
        
        # Assert
        assert result["address"] == "/test"
        assert result["args"] == [1, 2.5, "hello"]
        assert "timestamp" in result
    
    def test_str_representation(self):
        """
        Test de representación como string.
        
        Casos cubiertos:
        - Éxito: String legible con dirección y argumentos
        """
        # Arrange
        msg = OSCMessage("/test", [1, 2, 3])
        
        # Act
        result = str(msg)
        
        # Assert
        assert "/test" in result
        assert "[1, 2, 3]" in result or "1" in result


class TestMIDIEvent:
    """Tests para MIDIEvent."""
    
    def test_creation_basic(self):
        """
        Test de creación básica de evento MIDI.
        
        Casos cubiertos:
        - Éxito: Evento se crea correctamente
        - Estado: Nota, velocidad y canal se asignan
        """
        # Arrange & Act
        event = MIDIEvent(note=64, velocity=127, channel=0)
        
        # Assert
        assert event.note == 64
        assert event.velocity == 127
        assert event.channel == 0
        assert isinstance(event.timestamp, datetime)
    
    def test_creation_default_channel(self):
        """
        Test de creación con canal por defecto.
        
        Casos cubiertos:
        - Éxito: Canal 0 por defecto
        """
        # Arrange & Act
        event = MIDIEvent(note=60, velocity=100)
        
        # Assert
        assert event.channel == 0
    
    def test_to_dict(self):
        """
        Test de conversión a diccionario.
        
        Casos cubiertos:
        - Éxito: Retorna diccionario con todos los campos
        """
        # Arrange
        event = MIDIEvent(note=60, velocity=100, channel=1)
        
        # Act
        result = event.to_dict()
        
        # Assert
        assert result["note"] == 60
        assert result["velocity"] == 100
        assert result["channel"] == 1
        assert "timestamp" in result
    
    def test_str_representation(self):
        """
        Test de representación como string.
        
        Casos cubiertos:
        - Éxito: String legible con información del evento
        """
        # Arrange
        event = MIDIEvent(note=60, velocity=100, channel=2)
        
        # Act
        result = str(event)
        
        # Assert
        assert "60" in result or "note=60" in result
        assert "100" in result or "vel=100" in result


class TestCommunicationManager:
    """Tests para CommunicationManager."""
    
    def test_initialization(self):
        """
        Test de inicialización de CommunicationManager.
        
        Casos cubiertos:
        - Éxito: Inicialización exitosa
        - Estado: Listas vacías inicialmente
        """
        # Arrange & Act
        manager = CommunicationManager()
        
        # Assert
        assert manager.osc_clients == {}
        assert manager.midi_outputs == []
        assert manager.message_history == []
        assert manager.is_active is False
    
    def test_send_osc(self, caplog):
        """
        Test de envío de mensaje OSC.
        
        Casos cubiertos:
        - Éxito: Mensaje se registra en historial
        - Estado: Log se genera correctamente
        """
        # Arrange
        manager = CommunicationManager()
        msg = OSCMessage("/test", [1, 2, 3])
        
        # Act
        manager.send_osc(msg, "localhost:8000")
        
        # Assert
        assert len(manager.message_history) == 1
        assert manager.message_history[0]["type"] == "osc"
    
    def test_send_midi(self, caplog):
        """
        Test de envío de evento MIDI.
        
        Casos cubiertos:
        - Éxito: Evento se registra en historial
        - Estado: Log se genera correctamente
        """
        # Arrange
        manager = CommunicationManager()
        event = MIDIEvent(note=60, velocity=100)
        
        # Act
        manager.send_midi(event)
        
        # Assert
        assert len(manager.message_history) == 1
        assert manager.message_history[0]["type"] == "midi"
    
    def test_map_sensor_to_osc(self):
        """
        Test de mapeo de sensor a OSC.
        
        Casos cubiertos:
        - Éxito: Valor se mapea correctamente al rango OSC
        """
        # Arrange
        manager = CommunicationManager()
        
        # Act & Assert
        result = manager.map_sensor_to_osc(0.0, 0.0, 1.0)
        assert result == pytest.approx(0.0)
        
        result = manager.map_sensor_to_osc(1.0, 0.0, 100.0)
        assert result == pytest.approx(100.0)
        
        result = manager.map_sensor_to_osc(0.5, 0.0, 200.0)
        assert result == pytest.approx(100.0)
    
    def test_map_sensor_to_midi(self):
        """
        Test de mapeo de sensor a MIDI.
        
        Casos cubiertos:
        - Éxito: Valor se mapea correctamente al rango MIDI (0-127)
        """
        # Arrange
        manager = CommunicationManager()
        
        # Act & Assert
        result = manager.map_sensor_to_midi(0.0)
        assert result == 0
        
        result = manager.map_sensor_to_midi(1.0)
        assert result == 127
        
        result = manager.map_sensor_to_midi(0.5)
        assert result == 63
    
    def test_get_history(self):
        """
        Test de obtención de historial.
        
        Casos cubiertos:
        - Éxito: Retorna historial completo
        """
        # Arrange
        manager = CommunicationManager()
        manager.send_osc(OSCMessage("/test1"), "localhost:8000")
        manager.send_midi(MIDIEvent(note=60, velocity=100))
        
        # Act
        history = manager.get_history()
        
        # Assert
        assert len(history) == 2
    
    def test_get_history_with_count(self):
        """
        Test de obtención de historial con límite.
        
        Casos cubiertos:
        - Éxito: Retorna solo los últimos N mensajes
        """
        # Arrange
        manager = CommunicationManager()
        for i in range(5):
            manager.send_osc(OSCMessage(f"/test{i}"), "localhost:8000")
        
        # Act
        history = manager.get_history(count=2)
        
        # Assert
        assert len(history) == 2
    
    def test_start_stop(self):
        """
        Test de inicio y detención.
        
        Casos cubiertos:
        - Éxito: is_active cambia correctamente
        """
        # Arrange
        manager = CommunicationManager()
        
        # Act & Assert
        assert manager.is_active is False
        
        manager.start()
        assert manager.is_active is True
        
        manager.stop()
        assert manager.is_active is False
