"""
Tests para el módulo app.py.

Este módulo contiene tests para la clase App principal.
"""

import pytest
from unittest.mock import Mock, patch
import sys
from pathlib import Path

# Importar módulos del proyecto
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from app import App


class TestApp:
    """Tests para la clase App."""
    
    def test_initialization_basic(self):
        """
        Test de inicialización básica.
        
        Casos cubiertos:
        - Éxito: Inicialización sin configuración
        - Estado: Configuración vacía por defecto
        - Estado: Lista de datos vacía inicialmente
        """
        # Arrange & Act
        app = App()
        
        # Assert
        assert app.config == {}
        assert app.datos == []
    
    def test_initialization_with_config(self, sample_config):
        """
        Test de inicialización con configuración.
        
        Casos cubiertos:
        - Éxito: Inicialización con configuración personalizada
        - Estado: Configuración se almacena correctamente
        """
        # Arrange & Act
        app = App(config=sample_config)
        
        # Assert
        assert app.config == sample_config
        assert app.datos == []
    
    def test_procesar_without_data(self):
        """
        Test de procesamiento sin datos.
        
        Casos cubiertos:
        - Éxito: Retorna lista vacía
        - Estado: No lanza excepción
        """
        # Arrange
        app = App()
        
        # Act
        result = app.procesar()
        
        # Assert
        assert result == []
    
    def test_procesar_with_data(self):
        """
        Test de procesamiento con datos.
        
        Casos cubiertos:
        - Éxito: Almacena datos en la lista
        - Estado: Datos se retornan correctamente
        """
        # Arrange
        app = App()
        test_data = {"test": "value"}
        
        # Act
        result = app.procesar(test_data)
        
        # Assert
        assert len(result) == 1
        assert result[0] == test_data
    
    def test_procesar_multiple_times(self):
        """
        Test de procesamiento múltiple.
        
        Casos cubiertos:
        - Éxito: Múltiples datos se acumulan
        - Estado: Lista crece correctamente
        """
        # Arrange
        app = App()
        
        # Act
        app.procesar({"first": 1})
        app.procesar({"second": 2})
        app.procesar({"third": 3})
        
        # Assert
        assert len(app.datos) == 3
    
    def test_validar_truthy_value(self):
        """
        Test de validación con valores truthy.
        
        Casos cubiertos:
        - Éxito: Retorna True para valores truthy
        """
        # Arrange
        app = App()
        
        # Act & Assert
        assert app.validar(1) is True
        assert app.validar("test") is True
        assert app.validar([1, 2]) is True
        assert app.validar({"key": "value"}) is True
    
    def test_validar_falsy_value(self):
        """
        Test de validación con valores falsy.
        
        Casos cubiertos:
        - Éxito: Retorna False para valores falsy
        """
        # Arrange
        app = App()
        
        # Act & Assert
        assert app.validar(0) is False
        assert app.validar("") is False
        assert app.validar([]) is False
        assert app.validar({}) is False
        assert app.validar(None) is False
