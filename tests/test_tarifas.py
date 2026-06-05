from parkinguv.tarifas import calcular_tarifa


def test_primeros_30_minutos_gratis():
    assert calcular_tarifa(30) == 0


def test_minuto_31_cobra_500():
    assert calcular_tarifa(31) == 500


def test_90_minutos_cobra_500():
    assert calcular_tarifa(90) == 500


def test_91_minutos_cobra_1000():
    assert calcular_tarifa(91) == 1000

def test_tope_diario():
    assert calcular_tarifa(2000) == 12000