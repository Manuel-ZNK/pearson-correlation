"""
Módulo para validación y limpieza de datos.
Elimina filas con valores inválidos y organiza los datos por columna.
"""


def es_numero(valor):
    """
    Verifica si un valor puede convertirse a float.

    Args:
        valor (str): Valor a validar.

    Returns:
        bool: True si es número, False en caso contrario.
    """
    if not valor or valor.isspace():
        return False

    try:
        float(valor)
        return True
    except ValueError:
        return False


def limpiar_datos(encabezados, datos):
    """
    Limpia los datos eliminando filas inválidas.

    Args:
        encabezados (list): Nombres de variables.
        datos (list): Lista de filas con datos crudos.

    Returns:
        dict: Diccionario con claves:
            - 'encabezados': lista de nombres de columnas.
            - 'datos': lista de filas numéricas válidas.
            - 'filas_eliminadas': cantidad de filas descartadas.
            - 'filas_originales': cantidad de filas antes de limpiar.
            - 'filas_validas': cantidad de filas conservadas.
            - 'datos_por_columna': dict de listas de floats por columna.
    """
    filas_originales = len(datos)
    datos_limpios = []
    filas_eliminadas = 0

    for fila in datos:
        # Verificar que la fila tenga el mismo número de columnas
        if len(fila) != len(encabezados):
            filas_eliminadas += 1
            continue

        # Verificar que todos los valores sean numéricos
        fila_valida = all(es_numero(valor) for valor in fila)

        if fila_valida:
            fila_numerica = [float(valor) for valor in fila]
            datos_limpios.append(fila_numerica)
        else:
            filas_eliminadas += 1

    # Organizar datos por columna
    datos_por_columna = {}
    if datos_limpios:
        for i, encabezado in enumerate(encabezados):
            datos_por_columna[encabezado] = [fila[i] for fila in datos_limpios]

    return {
        'encabezados': encabezados,
        'datos': datos_limpios,
        'filas_eliminadas': filas_eliminadas,
        'datos_por_columna': datos_por_columna,
        'filas_originales': filas_originales,
        'filas_validas': len(datos_limpios),
    }


def validar_variables(encabezados, var1, var2):
    """
    Valida que las variables seleccionadas existan y sean distintas.

    Args:
        encabezados (list): Lista de nombres de variables disponibles.
        var1 (str): Primera variable (nombre o índice numérico como string).
        var2 (str): Segunda variable (nombre o índice numérico como string).

    Returns:
        tuple: (nombre_var1, nombre_var2) validados.

    Raises:
        ValueError: Si alguna variable no existe o ambas son iguales.
    """

    def resolver_variable(var):
        """Devuelve el nombre de la columna dado un nombre o índice."""
        # Intentar interpretar como índice numérico entero
        try:
            idx = int(var)
        except ValueError:
            # No es un entero; buscar por nombre
            if var in encabezados:
                return var
            raise ValueError(f"Variable '{var}' no encontrada")

        # Es un entero: validar rango
        if idx < 0 or idx >= len(encabezados):
            raise ValueError(f"Índice {idx} fuera de rango (0-{len(encabezados) - 1})")
        return encabezados[idx]

    nombre_var1 = resolver_variable(var1)
    nombre_var2 = resolver_variable(var2)

    if nombre_var1 == nombre_var2:
        raise ValueError("No puedes seleccionar la misma variable dos veces")

    return nombre_var1, nombre_var2
