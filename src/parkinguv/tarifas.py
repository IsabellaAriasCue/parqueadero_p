import math

TOPE_DIARIO = 12000


def calcular_tarifa(minutos, vip=False):

    if minutos <= 30:
        return 0

    horas = math.ceil((minutos - 30) / 60)

    total = horas * 500

    if vip:
        total *= 0.8

    return min(total, TOPE_DIARIO)