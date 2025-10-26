"""
Funciones de ayuda para el procesamiento de datos.

Autor: Assiz Alcaraz Baxter
Fecha: 2025-10-26
"""

import math
from typing import Tuple


def normalize_vector(x: float, y: float, z: float) -> Tuple[float, float, float]:
    """
    Normalizar un vector 3D.
    
    Args:
        x, y, z: Componentes del vector
        
    Returns:
        Tupla con el vector normalizado
    """
    magnitude = calculate_magnitude(x, y, z)
    if magnitude == 0:
        return (0.0, 0.0, 0.0)
    return (x / magnitude, y / magnitude, z / magnitude)


def calculate_magnitude(x: float, y: float, z: float) -> float:
    """
    Calcular la magnitud de un vector 3D.
    
    Args:
        x, y, z: Componentes del vector
        
    Returns:
        Magnitud del vector
    """
    return math.sqrt(x*x + y*y + z*z)


def map_value(value: float, from_min: float, from_max: float, 
              to_min: float, to_max: float) -> float:
    """
    Mapear un valor de un rango a otro.
    
    Args:
        value: Valor a mapear
        from_min, from_max: Rango de origen
        to_min, to_max: Rango de destino
        
    Returns:
        Valor mapeado
    """
    return (value - from_min) / (from_max - from_min) * (to_max - to_min) + to_min
