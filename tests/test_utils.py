"""
Tests para el módulo utils/helpers.py.

Este módulo contiene tests para las funciones de utilidad.
"""

import pytest
import sys
import math
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from utils.helpers import normalize_vector, calculate_magnitude, map_value


class TestCalculateMagnitude:
    """Tests para calculate_magnitude."""
    
    def test_magnitude_zero_vector(self):
        """
        Test con vector cero.
        
        Casos cubiertos:
        - Éxito: Magnitud de vector cero es 0
        """
        # Act
        result = calculate_magnitude(0, 0, 0)
        
        # Assert
        assert result == 0.0
    
    def test_magnitude_unit_vector(self):
        """
        Test con vector unitario.
        
        Casos cubiertos:
        - Éxito: Magnitud de vector unitario es 1
        """
        # Act
        result = calculate_magnitude(1, 0, 0)
        
        # Assert
        assert result == pytest.approx(1.0)
    
    def test_magnitude_standard_vector(self):
        """
        Test con vector estándar.
        
        Casos cubiertos:
        - Éxito: Magnitud se calcula correctamente (3-4-5 triangle)
        """
        # Act
        result = calculate_magnitude(3, 4, 0)
        
        # Assert
        assert result == pytest.approx(5.0)
    
    def test_magnitude_3d_vector(self):
        """
        Test con vector 3D.
        
        Casos cubiertos:
        - Éxito: Magnitud de vector 3D se calcula correctamente
        """
        # Act
        result = calculate_magnitude(3, 4, 12)
        
        # Assert
        assert result == pytest.approx(13.0)


class TestNormalizeVector:
    """Tests para normalize_vector."""
    
    def test_normalize_unit_vector(self):
        """
        Test de normalización de vector unitario.
        
        Casos cubiertos:
        - Éxito: Vector unitario se mantiene igual
        """
        # Act
        result = normalize_vector(1, 0, 0)
        
        # Assert
        assert result == (1.0, 0.0, 0.0)
    
    def test_normalize_zero_vector(self):
        """
        Test de normalización de vector cero.
        
        Casos cubiertos:
        - Éxito: Retorna vector cero (0, 0, 0)
        """
        # Act
        result = normalize_vector(0, 0, 0)
        
        # Assert
        assert result == (0.0, 0.0, 0.0)
    
    def test_normalize_standard_vector(self):
        """
        Test de normalización de vector estándar.
        
        Casos cubiertos:
        - Éxito: Vector se normaliza a magnitud 1
        """
        # Act
        result = normalize_vector(3, 4, 0)
        
        # Assert
        magnitude = calculate_magnitude(result[0], result[1], result[2])
        assert magnitude == pytest.approx(1.0)
    
    def test_normalize_3d_vector(self):
        """
        Test de normalización de vector 3D.
        
        Casos cubiertos:
        - Éxito: Magnitud del resultado es 1
        """
        # Act
        result = normalize_vector(1, 1, 1)
        
        # Assert
        magnitude = calculate_magnitude(result[0], result[1], result[2])
        assert magnitude == pytest.approx(1.0)
        # Verificar que es vector normalizado correctamente
        expected = (1/math.sqrt(3), 1/math.sqrt(3), 1/math.sqrt(3))
        assert result[0] == pytest.approx(expected[0])
        assert result[1] == pytest.approx(expected[1])
        assert result[2] == pytest.approx(expected[2])


class TestMapValue:
    """Tests para map_value."""
    
    def test_map_minimum(self):
        """
        Test de mapeo al mínimo.
        
        Casos cubiertos:
        - Éxito: Valor mínimo se mapea correctamente
        """
        # Act
        result = map_value(0, 0, 1, 10, 20)
        
        # Assert
        assert result == pytest.approx(10.0)
    
    def test_map_maximum(self):
        """
        Test de mapeo al máximo.
        
        Casos cubiertos:
        - Éxito: Valor máximo se mapea correctamente
        """
        # Act
        result = map_value(1, 0, 1, 10, 20)
        
        # Assert
        assert result == pytest.approx(20.0)
    
    def test_map_middle(self):
        """
        Test de mapeo al centro.
        
        Casos cubiertos:
        - Éxito: Valor medio se mapea al centro del rango destino
        """
        # Act
        result = map_value(0.5, 0, 1, 0, 100)
        
        # Assert
        assert result == pytest.approx(50.0)
    
    def test_map_negative_range(self):
        """
        Test de mapeo con rango negativo.
        
        Casos cubiertos:
        - Éxito: Funciona con rangos negativos
        """
        # Act
        result = map_value(0.5, 0, 1, -100, 100)
        
        # Assert
        assert result == pytest.approx(0.0)
    
    def test_map_out_of_range_value(self):
        """
        Test de mapeo fuera de rango.
        
        Casos cubiertos:
        - Éxito: Valores fuera de rango se mapean según la fórmula
        """
        # Act - Valor mayor al rango de origen
        result_high = map_value(2.0, 0, 1, 0, 100)
        
        # Act - Valor menor al rango de origen
        result_low = map_value(-1.0, 0, 1, 0, 100)
        
        # Assert - Valores fuera de rango se mapean linealmente
        assert result_high == 200.0
        assert result_low == -100.0
    
    def test_map_sensor_to_midi_range(self):
        """
        Test de mapeo simulando conversión sensor a MIDI.
        
        Casos cubiertos:
        - Éxito: Mapeo de rango 0-1 a rango MIDI 0-127
        """
        # Act
        result_min = map_value(0.0, 0, 1, 0, 127)
        result_max = map_value(1.0, 0, 1, 0, 127)
        result_mid = map_value(0.5, 0, 1, 0, 127)
        
        # Assert
        assert result_min == pytest.approx(0.0)
        assert result_max == pytest.approx(127.0)
        assert result_mid == pytest.approx(63.5)
