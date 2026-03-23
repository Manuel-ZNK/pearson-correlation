"""
Módulo para la presentación de resultados del análisis de Pearson.
Todas las funciones imprimen directamente en consola con formato visual.
"""


def mostrar_encabezado():
    """Muestra el encabezado principal del programa."""
    print("\n" + "=" * 70)
    print("   📊 ANÁLISIS DE CORRELACIÓN DE PEARSON (Sin librerías externas)")
    print("=" * 70 + "\n")


def mostrar_menu_inicial():
    """Muestra el menú inicial con las opciones disponibles."""
    print("\n¿Qué deseas hacer?")
    print("  1. Cargar archivo de datos")
    print("  2. Salir")
    print("-" * 50)


def mostrar_variables(encabezados):
    """
    Muestra la lista de variables disponibles con su índice.

    Args:
        encabezados (list): Lista de nombres de variables.
    """
    print("\n📋 VARIABLES DISPONIBLES:")
    print("-" * 50)
    for i, encabezado in enumerate(encabezados):
        print(f"  [{i}] {encabezado}")
    print()


def mostrar_tabla_datos(datos_limpios, encabezados):
    """
    Muestra una tabla formateada con los datos limpios.
    Si hay más de 20 filas sólo muestra las primeras 20.

    Args:
        datos_limpios (list): Lista de filas numéricas.
        encabezados (list): Nombres de las columnas.
    """
    print("\n📊 TABLA DE DATOS LIMPIA:")
    print("-" * 70)

    # Calcular ancho mínimo por columna (al menos 12 caracteres)
    anchos = [max(len(str(enc)), 12) for enc in encabezados]

    # Fila de encabezados
    encabezado_str = " | ".join(
        f"{enc:<{anchos[i]}}" for i, enc in enumerate(encabezados)
    )
    print(encabezado_str)
    print("-" * 70)

    # Filas de datos (máximo 20)
    filas_mostrar = min(20, len(datos_limpios))
    for fila in datos_limpios[:filas_mostrar]:
        fila_str = " | ".join(
            f"{valor:<{anchos[i]}.4f}" for i, valor in enumerate(fila)
        )
        print(fila_str)

    if len(datos_limpios) > 20:
        print(f"... ({len(datos_limpios) - 20} filas más no mostradas)")

    print("-" * 70)


def mostrar_resumen_limpieza(resultado_limpieza):
    """
    Muestra el resumen del proceso de limpieza de datos.

    Args:
        resultado_limpieza (dict): Resultado devuelto por limpiar_datos().
    """
    print("\n🔧 RESUMEN DE LIMPIEZA DE DATOS:")
    print("-" * 50)
    print(f"  ✓ Filas originales:  {resultado_limpieza['filas_originales']}")
    print(f"  ✓ Filas válidas:     {resultado_limpieza['filas_validas']}")
    print(f"  ✗ Filas eliminadas:  {resultado_limpieza['filas_eliminadas']}")
    print("-" * 50)


def mostrar_resultados_correlacion(var1, var2, resultado_pearson):
    """
    Muestra los resultados completos del cálculo de Pearson con barra visual.

    Args:
        var1 (str): Nombre de la primera variable.
        var2 (str): Nombre de la segunda variable.
        resultado_pearson (dict): Resultado devuelto por calcular_pearson().
    """
    print("\n" + "=" * 70)
    print("   📈 RESULTADOS DEL ANÁLISIS DE CORRELACIÓN")
    print("=" * 70)

    correlacion = resultado_pearson['correlacion']

    print(f"\n  Variables analizadas:")
    print(f"    X: {var1}")
    print(f"    Y: {var2}")

    print(f"\n  Estadísticas:")
    print(f"    Promedio X : {resultado_pearson['promedio_x']:.6f}")
    print(f"    Promedio Y : {resultado_pearson['promedio_y']:.6f}")
    print(f"    N (datos)  : {resultado_pearson['detalles']['n']}")

    print(f"\n  📊 COEFICIENTE DE CORRELACIÓN DE PEARSON:")
    print(f"    r = {correlacion:.6f}")

    # Barra visual de -1 a +1
    barra_width = 50
    centro = barra_width // 2
    posicion = int(((correlacion + 1) / 2) * barra_width)
    posicion = max(0, min(barra_width, posicion))

    barra = list("░" * barra_width)
    # Relleno desde el centro hasta la posición del valor
    if correlacion >= 0:
        for k in range(centro, posicion):
            barra[k] = "█"
    else:
        for k in range(posicion, centro):
            barra[k] = "█"
    barra_str = "".join(barra)
    print(f"    -1 [{barra_str}] +1")

    print(f"\n  🎯 INTERPRETACIÓN:")
    print(f"    {resultado_pearson['interpretacion']}")

    detalles = resultado_pearson['detalles']
    print("\n  📐 DETALLES DEL CÁLCULO:")
    print(f"    Σ(xi - x̄)(yi - ȳ) = {detalles['numerador']:.6f}")
    print(f"    Σ(xi - x̄)²        = {detalles['suma_cuadrados_x']:.6f}")
    print(f"    Σ(yi - ȳ)²        = {detalles['suma_cuadrados_y']:.6f}")
    print(f"    Denominador        = {detalles['denominador']:.6f}")

    print("\n" + "=" * 70 + "\n")


def mostrar_error(mensaje):
    """
    Muestra un mensaje de error formateado.

    Args:
        mensaje (str): Descripción del error.
    """
    print(f"\n❌ ERROR: {mensaje}\n")


def mostrar_exito(mensaje):
    """
    Muestra un mensaje de éxito formateado.

    Args:
        mensaje (str): Descripción de la acción completada.
    """
    print(f"  ✓ {mensaje}")
