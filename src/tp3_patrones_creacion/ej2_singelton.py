# ------------------------------------------------------------------------------------------------------------------
# Trabajo Practico N° 3 - Patrones de Creacion.
# Josue Linarez Hein
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# Punto 2:
# Elabore una clase para el cálculo del valor de impuestos a ser utilizado por 
# todas las clases que necesiten realizarlo. El cálculo de impuestos simplificado 
# deberá recibir un valor de importe base imponible y deberá retornar la suma 
# del cálculo de IVA (21%), IIBB (5%) y Contribuciones municipales (1,2%) sobre 
# esa base imponible
# ------------------------------------------------------------------------------------------------------------------

class CalculadoraImpuestos:
    _instance = None

    def __new__(cls):
        """
        Método especial que se llama para crear una nueva instancia de la clase.
        Utilizamos este método para asegurarnos de que solo haya una instancia de la clase.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def calcular_impuestos(self, base_imponible):
        """
        Calcula el valor total de impuestos sobre una base imponible dada.

        Args:
            base_imponible (float): El valor base sobre el cual se calculan los impuestos.

        Returns:
            float: El valor total de impuestos calculado.
        """
        iva = base_imponible * 0.21  # Calcula el IVA (21%)
        iibb = base_imponible * 0.05  # Calcula el impuesto sobre los ingresos brutos (5%)
        contrib_municipales = base_imponible * 0.012  # Calcula las contribuciones municipales (1.2%)

        total_impuestos = iva + iibb + contrib_municipales  # Suma de los impuestos

        return total_impuestos


calculadora_singleton = CalculadoraImpuestos()
impuestos = calculadora_singleton.calcular_impuestos(1000.0)
print("Total de impuestos a pagar:", impuestos)
