"""
Módulo de manejo de sensores del iPhone.

Este módulo proporciona funcionalidades para interactuar con los sensores
del iPhone 15 (acelerómetro, giroscopio, brújula, etc.) para usar el
dispositivo como instrumento de dibujo en instalaciones artísticas.

Autor: Assiz Alcaraz Baxter
Fecha: 2025-10-26
"""

import logging
from typing import Dict, Optional, Callable
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)


class SensorType(Enum):
    """Tipos de sensores disponibles."""
    ACCELEROMETER = "accelerometer"
    GYROSCOPE = "gyroscope"
    MAGNETOMETER = "magnetometer"  # Brújula
    GRAVITY = "gravity"
    USER_ACCELERATION = "user_acceleration"


@dataclass
class SensorData:
    """Datos de un sensor."""
    type: SensorType
    x: float
    y: float
    z: float
    timestamp: float
    
    def to_dict(self) -> Dict:
        """Convertir a diccionario."""
        return {
            "type": self.type.value,
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "timestamp": self.timestamp
        }


class SensorManager:
    """
    Gestor de sensores del iPhone.
    
    Maneja la lectura y procesamiento de datos de sensores
    para su uso en aplicaciones artísticas interactivas.
    """
    
    def __init__(self):
        """Inicializar el gestor de sensores."""
        self.callbacks: Dict[SensorType, list[Callable]] = {}
        self.data_history: Dict[SensorType, list[SensorData]] = {}
        self.is_active = False
        logger.info("SensorManager inicializado")
    
    def register_callback(self, sensor_type: SensorType, callback: Callable) -> None:
        """
        Registrar un callback para un tipo de sensor.
        
        Args:
            sensor_type: Tipo de sensor a monitorear
            callback: Función a llamar cuando lleguen datos
        """
        if sensor_type not in self.callbacks:
            self.callbacks[sensor_type] = []
        self.callbacks[sensor_type].append(callback)
        logger.info(f"Callback registrado para {sensor_type.value}")
    
    def _emit_data(self, sensor_type: SensorType, data: SensorData) -> None:
        """
        Emitir datos a los callbacks registrados.
        
        Args:
            sensor_type: Tipo de sensor
            data: Datos del sensor
        """
        if sensor_type in self.callbacks:
            for callback in self.callbacks[sensor_type]:
                try:
                    callback(data)
                except Exception as e:
                    logger.error(f"Error en callback para {sensor_type.value}: {e}")
    
    def record_data(self, sensor_type: SensorType, data: SensorData) -> None:
        """
        Registrar datos de sensor.
        
        Args:
            sensor_type: Tipo de sensor
            data: Datos del sensor
        """
        if sensor_type not in self.data_history:
            self.data_history[sensor_type] = []
        
        # Mantener solo los últimos 100 registros
        if len(self.data_history[sensor_type]) >= 100:
            self.data_history[sensor_type].pop(0)
        
        self.data_history[sensor_type].append(data)
        self._emit_data(sensor_type, data)
    
    def get_data(self, sensor_type: SensorType, count: Optional[int] = None) -> list[SensorData]:
        """
        Obtener datos históricos de un sensor.
        
        Args:
            sensor_type: Tipo de sensor
            count: Número de muestras a obtener (None para todas)
            
        Returns:
            Lista de datos del sensor
        """
        if sensor_type not in self.data_history:
            return []
        
        data = self.data_history[sensor_type]
        if count is None:
            return data
        return data[-count:]
    
    def start(self) -> None:
        """Iniciar la captura de sensores."""
        self.is_active = True
        logger.info("Captura de sensores iniciada")
    
    def stop(self) -> None:
        """Detener la captura de sensores."""
        self.is_active = False
        logger.info("Captura de sensores detenida")
