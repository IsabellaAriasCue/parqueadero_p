from parkinguv.tarifas import calcular_tarifa


def test_primeros_30_minutos_gratis():
    assert calcular_tarifa(30) == 0