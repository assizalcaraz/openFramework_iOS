"""
Configuración común para pytest.

Este archivo contiene fixtures y configuración compartida
para todos los tests del proyecto.
"""

import pytest
import sys
from pathlib import Path

# Añadir src al path para imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))


@pytest.fixture
def sample_config():
    """Fixture con configuración de ejemplo."""
    return {
        "version": "0.1.0",
        "debug": True,
        "sensor_update_rate": 60
    }


@pytest.fixture
def sample_sensor_data():
    """Fixture con datos de sensor de ejemplo."""
    return {
        "x": 0.5,
        "y": 0.5,
        "z": 0.5,
        "timestamp": 1234567890.0
    }
