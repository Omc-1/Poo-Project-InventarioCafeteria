import pytest
from cafe import Cafe
from cacao import Cacao
from lacteos import Lacteos

def test_creacion_cafe():
    """Prueba que un objeto Cafe se cree con los atributos correctos."""
    mi_cafe = Cafe("Starbucks", "Pike Place", "Grano", 5, 1.0)
    assert mi_cafe.brand == "Starbucks"
    assert mi_cafe.kilos_per_bag == 1.0
    assert mi_cafe.bags == 5

def test_creacion_cacao():
    """Prueba que un objeto Cacao se cree correctamente."""
    mi_cacao = Cacao("Hersheys", "Cocoa Pure", "Polvo", 10, 0.5)
    assert mi_cacao.brand == "Hersheys"
    assert mi_cacao.kilos_per_bag == 0.5

def test_creacion_lacteos():
    """Prueba que un objeto Lacteos use litros en lugar de kilos."""
    mi_leche = Lacteos("Alpura", "Entera", "Liquido", 12, 1.0)
    assert mi_leche.brand == "Alpura"
    assert mi_leche.liters_per_bag == 1.0

def test_herencia_insumos():
    """Prueba que todos hereden de la lógica de Insumos (polimorfismo)."""
    productos = [
        Cafe("A", "B", "C", 1, 1.0),
        Cacao("D", "E", "F", 2, 0.5),
        Lacteos("G", "H", "I", 3, 1.0)
    ]
    # Todos deben tener el atributo 'brand' por herencia
    for p in productos:
        assert hasattr(p, 'brand')
