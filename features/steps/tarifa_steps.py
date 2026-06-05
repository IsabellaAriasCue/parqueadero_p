from behave import given, when, then
from parkinguv.tarifas import calcular_tarifa


@given('un vehículo permanece {minutos:d} minutos')
def step_given(context, minutos):
    context.minutos = minutos
    context.vip = False


@given('un cliente VIP permanece {minutos:d} minutos')
def step_given_vip(context, minutos):
    context.minutos = minutos
    context.vip = True


@when('se calcula la tarifa')
def step_when(context):
    context.resultado = calcular_tarifa(context.minutos, context.vip)


@when('se calcula la tarifa VIP')
def step_when_vip(context):
    context.resultado = calcular_tarifa(context.minutos, True)


@then('el valor a pagar debe ser {valor:d} pesos')
def step_then(context, valor):
    assert context.resultado == valor