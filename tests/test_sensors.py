"""
Tests para el módulo sensors.py.

Este módulo contiene tests para SensorManager.
"""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from sensors import SensorManager, SensorType, SensorData


class TestSensorManager:
    """Tests para SensorManager."""
    
    def test_initialization(self):
        """
        Test de inicialización de SensorManager.
        
        Casos cubiertos:
        - Éxito: Inicialización exitosa
        - Estado: Callbacks y data_history vacíos
        - Estado: is_active = False inicialmente
        """
        # Arrange & Act
        manager = SensorManager()
        
        # Assert
        assert manager.callbacks == {}
        assert manager.data_history == {}
        assert manager.is_active is False
    
    def test_register_callback(self):
        """
        Test de registro de callback.
        
        Casos cubiertos:
        - Éxito: Callback se registra correctamente
        - Estado: Callback se añade a la lista
        """
        # Arrange
        manager = SensorManager()
        callback = lambda x: x
        
        # Act
        manager.register_callback(SensorType.ACCELEROMETER, callback)
        
        # Assert
        assert SensorType.ACCELEROMETER in manager.callbacks
        assert len(manager.callbacks[SensorType.ACCELEROMETER]) == 1
    
    def test_register_multiple_callbacks(self):
        """
        Test de registro múltiple de callbacks.
        
        Casos cubiertos:
        - Éxito: Múltiples callbacks se registran
        - Estado: Todos los callbacks se almacenan
        """
        # Arrange
        manager = SensorManager()
        callback1 = lambda x: x
        callback2 = lambda x: x * 2
        
        # Act
        manager.register_callback(SensorType.ACCELEROMETER, callback1)
        manager.register_callback(SensorType.ACCELEROMETER, callback2)
        
        # Assert
        assert len(manager.callbacks[SensorType.ACCELEROMETER]) == 2
    
    def test_record_data(self):
        """
        Test de registro de datos.
        
        Casos cubiertos:
        - Éxito: Datos se registran correctamente
        - Estado: Datos se añaden al historial
        """
        # Arrange
        manager = SensorManager()
        data = SensorData(SensorType.ACCELEROMETER, 1.0, 2.0, 3.0, 1234567890.0)
        
        # Act
        manager.record_data(SensorType.ACCELEROMETER, data)
        
        # Assert
        assert SensorType.ACCELEROMETER in manager.data_history
        assert len(manager.data_history[SensorType.ACCELEROMETER]) == 1
        assert manager.data_history[SensorType.ACCELEROMETER][0] == data
    
    def test_get_data_empty(self):
        """
        Test de obtención de datos vacía.
        
        Casos cubiertos:
        - Éxito: Retorna lista vacía si no hay datos
        """
        # Arrange
        manager = SensorManager()
        
        # Act
        result = manager.get_data(SensorType.GYROSCOPE)
        
        # Assert
        assert result == []
    
    def test_get_data_with_count(self):
        """
        Test de obtención de datos con límite.
        
        Casos cubiertos:
        - Éxito: Retorna solo los últimos N registros
        """
        # Arrange
        manager = SensorManager()
        sensor_type = SensorType.MAGNETOMETER
        
        # Act
        for i in range(5):
            data = SensorData(sensor_type, i, i, i, float(i))
            manager.record_data(sensor_type, data)
        
        result = manager.get_data(sensor_type, count=3)
        
        # Assert
        assert len(result) == 3
        assert result[-1].timestamp == 4.0
    
    def test_history_limit(self):
        """
        Test de límite de historial.
        
        Casos cubiertos:
        - Éxito: Solo se mantienen los últimos 100 registros
        """
        # Arrange
        manager = SensorManager()
        sensor_type = SensorType.ACCELEROMETER
        
        # Act
        for i in range(150):
            data = SensorData(sensor_type, i, i, i, float(i))
            manager.record_data(sensor_type, data)
        
        # Assert
        assert len(manager.data_history[sensor_type]) == 100
    
    def test_start_stop(self):
        """
        Test de inicio y detención.
        
        Casos cubiertos:
        - Éxito: is_active cambia correctamente
        """
        # Arrange
        manager = SensorManager()
        
        # Act & Assert
        assert manager.is_active is False
        
        manager.start()
        assert manager.is_active is True
        
        manager.stop()
        assert manager.is_active is False


class TestSensorData:
    """Tests para SensorData."""
    
    def test_sensor_data_creation(self):
        """
        Test de creación de SensorData.
        
        Casos cubiertos:
        - Éxito: Todos los campos se asignan correctamente
        """
        # Arrange & Act
        data = SensorData(SensorType.ACCELEROMETER, 1.0, 2.0, 3.0, 1234567890.0)
        
        # Assert
        assert data.type == SensorType.ACCELEROMETER
        assert data.x == 1.0
        assert data.y == 2.0
        assert data.z == 3.0
        assert data.timestamp == 1234567890.0
    
    def test_to_dict(self):
        """
        Test de conversión a diccionario.
        
        Casos cubiertos:
        - Éxito: Retorna diccionario con todos los campos
        """
        # Arrange
        data = SensorData(SensorType.GYROSCOPE, 0.1, 0.2, 0.3, 1234567890.0)
        
        # Act
        result = data.to_dict()
        
        # Assert
        assert result["type"] == "gyroscope"
        assert result["x"] == 0.1
        assert result["y"] == 0.2
        assert result["z"] == 0.3
        assert result["timestamp"] == 1234567890.0
