from cafe import Cafe


def test_total_kilos_cafe():
    # Prueba que el cálculo de kilos sea correcto
    mi_cafe = Cafe("TestBrand", "TestModel", 10, 2.5)
    assert mi_cafe.total_kilos() == 25.0
