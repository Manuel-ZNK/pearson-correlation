"""
Módulo para cálculo manual de la correlación de Pearson.
No utiliza librerías externas; sólo Python estándar (math).
"""

import math


def calcular_promedio(valores):
    """
    Calcula el promedio de una lista de valores numéricos.

    Args:
        valores (list): Lista de números (int o float).

    Returns:
        float: Promedio de los valores, o 0 si la lista está vacía.
    """
    if not valores:
        return 0.0
    return sum(valores) / len(valores)


def calcular_pearson(valores_x, valores_y):
    """
    Calcula el coeficiente de correlación de Pearson entre dos variables.

    Fórmula implementada paso a paso:
        r = Σ((xi - x̄)(yi - ȳ)) / sqrt(Σ(xi - x̄)² · Σ(yi - ȳ)²)

    Args:
        valores_x (list): Datos de la primera variable.
        valores_y (list): Datos de la segunda variable.

    Returns:
        dict: Diccionario con claves:
            - 'correlacion' (float): Coeficiente r.
            - 'promedio_x' (float): Promedio de X.
            - 'promedio_y' (float): Promedio de Y.
            - 'interpretacion' (str): Descripción cualitativa del resultado.
            - 'detalles' (dict): Valores intermedios del cálculo.

    Raises:
        ValueError: Si los datos son insuficientes o tienen longitudes distintas.
    """
    if not valores_x or not valores_y:
        raise ValueError("Las variables no tienen datos válidos")

    if len(valores_x) != len(valores_y):
        raise ValueError("Las variables deben tener la misma cantidad de datos")

    n = len(valores_x)

    # Paso 1: Calcular promedios
    promedio_x = calcular_promedio(valores_x)
    promedio_y = calcular_promedio(valores_y)

    # Paso 2: Calcular diferencias respecto al promedio y sus productos
    numerador = 0.0
    suma_cuadrados_x = 0.0
    suma_cuadrados_y = 0.0

    for i in range(n):
        diferencia_x = valores_x[i] - promedio_x
        diferencia_y = valores_y[i] - promedio_y

        numerador += diferencia_x * diferencia_y
        suma_cuadrados_x += diferencia_x ** 2
        suma_cuadrados_y += diferencia_y ** 2

    # Paso 3: Calcular denominador
    denominador = math.sqrt(suma_cuadrados_x * suma_cuadrados_y)

    # Paso 4: Manejar división entre cero (variable constante)
    if denominador == 0:
        correlacion = 0.0
        interpretacion = "No hay variación en una o ambas variables (correlación indefinida)"
    else:
        correlacion = numerador / denominador
        interpretacion = _interpretar_correlacion(correlacion)

    return {
        'correlacion': correlacion,
        'promedio_x': promedio_x,
        'promedio_y': promedio_y,
        'interpretacion': interpretacion,
        'detalles': {
            'n': n,
            'numerador': numerador,
            'suma_cuadrados_x': suma_cuadrados_x,
            'suma_cuadrados_y': suma_cuadrados_y,
            'denominador': denominador,
        },
    }


def _interpretar_correlacion(r):
    """
    Devuelve una descripción cualitativa del coeficiente de Pearson.

    Args:
        r (float): Coeficiente de correlación entre -1 y 1.

    Returns:
        str: Interpretación del coeficiente.
    """
    abs_r = abs(r)

    if abs_r >= 0.8:
        intensidad = "fuerte"
    elif abs_r >= 0.5:
        intensidad = "moderada"
    elif abs_r >= 0.3:
        intensidad = "débil"
    else:
        return "Sin correlación (relación muy débil o inexistente)"

    direccion = "positiva" if r > 0 else "negativa"
    return f"Correlación {direccion} {intensidad}"
