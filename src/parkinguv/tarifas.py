import math

MINUTOS_GRATIS = 30
TARIFA_HORA = 500
TOPE_DIARIO = 12000
DESCUENTO_VIP = 0.20


def calcular_tarifa(minutos, vip=False):

    if minutos <= MINUTOS_GRATIS:
        return 0

    horas = math.ceil((minutos - MINUTOS_GRATIS) / 60)
    total = horas * TARIFA_HORA

    # 1. tope primero (IMPORTANTE para Behave)
    total = min(total, TOPE_DIARIO)

    # 2. VIP después
    if vip:
        total *= (1 - DESCUENTO_VIP)

    return int(total)