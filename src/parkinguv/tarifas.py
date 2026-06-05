import math

TOPE_DIARIO = 12000


def calcular_tarifa(minutos):

    if minutos <= 30:
        return 0

    horas = math.ceil((minutos - 30) / 60)

    total = horas * 500

    return min(total, TOPE_DIARIO)