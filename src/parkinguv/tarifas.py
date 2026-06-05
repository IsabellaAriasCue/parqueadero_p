import math

MINUTOS_GRATIS = 30
TARIFA_HORA = 500
TOPE_DIARIO = 12000
DESCUENTO_VIP = 0.20


def calcular_tarifa(minutos, vip=False):

    if minutos <= MINUTOS_GRATIS:
        return 0

    horas = math.ceil(
        (minutos - MINUTOS_GRATIS) / 60
    )

    total = horas * TARIFA_HORA

    if vip:
        total *= (1 - DESCUENTO_VIP)

    return min(total, TOPE_DIARIO)