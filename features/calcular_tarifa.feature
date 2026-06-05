Feature: Cálculo de tarifa de parqueadero

  Como gerente de ParkingUV
  Quiero calcular correctamente la tarifa de parqueo
  Para cobrar a los clientes de acuerdo con las reglas del negocio

  Scenario: Los primeros 30 minutos son gratuitos
    Given un vehículo permanece 30 minutos
    When se calcula la tarifa
    Then el valor a pagar debe ser 0 pesos

  Scenario: Cobro de la primera hora o fracción
    Given un vehículo permanece 31 minutos
    When se calcula la tarifa
    Then el valor a pagar debe ser 500 pesos

  Scenario: Cobro de dos horas
    Given un vehículo permanece 91 minutos
    When se calcula la tarifa
    Then el valor a pagar debe ser 1000 pesos

  Scenario: Aplicación del tope diario
    Given un vehículo permanece 2000 minutos
    When se calcula la tarifa
    Then el valor a pagar debe ser 12000 pesos

  Scenario: Aplicación del descuento VIP
    Given un cliente VIP permanece 91 minutos
    When se calcula la tarifa VIP
    Then el valor a pagar debe ser 800 pesos

  Scenario: Descuento VIP antes del tope diario
    Given un cliente VIP permanece 2000 minutos
    When se calcula la tarifa VIP
    Then el valor a pagar debe ser 9600 pesos