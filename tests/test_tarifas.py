from parkinguv.tarifas import calcular_tarifa


def test_gratis_30_min():
    assert calcular_tarifa(30) == 0


def test_minuto_31():
    assert calcular_tarifa(31) == 500


def test_91_min():
    assert calcular_tarifa(91) == 1000


def test_tope_diario():
    assert calcular_tarifa(2000) == 12000


def test_vip():
    assert calcular_tarifa(91, True) == 800