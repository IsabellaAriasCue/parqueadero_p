import math


def calcular_tarifa(minutos):

    if minutos <= 30:
        return 0

    horas = math.ceil((minutos - 30) / 60)

    return horas * 500