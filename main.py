"""
Programa principal: Análisis de Correlación de Pearson
Flujo: Lectura → Limpieza → Selección de variables → Cálculo → Resultados
"""

from lector import leer_archivo, obtener_ruta_archivo
from limpiador import limpiar_datos, validar_variables
from analisis import calcular_pearson
from salida import (
    mostrar_encabezado,
    mostrar_menu_inicial,
    mostrar_variables,
    mostrar_tabla_datos,
    mostrar_resumen_limpieza,
    mostrar_resultados_correlacion,
    mostrar_error,
    mostrar_exito,
)


def seleccionar_variables(encabezados):
    """
    Interfaz para que el usuario elija dos variables a correlacionar.

    Args:
        encabezados (list): Nombres de variables disponibles.

    Returns:
        tuple: (nombre_var1, nombre_var2) validados.
    """
    mostrar_variables(encabezados)

    while True:
        print("Selecciona dos variables por nombre o índice:")
        var1 = input("  Primera variable  : ").strip()
        var2 = input("  Segunda variable  : ").strip()

        try:
            nombre_var1, nombre_var2 = validar_variables(encabezados, var1, var2)
            return nombre_var1, nombre_var2
        except ValueError as e:
            mostrar_error(str(e))


def realizar_analisis(ruta_archivo):
    """
    Ejecuta el flujo completo de análisis para un archivo dado.

    Args:
        ruta_archivo (str): Ruta del archivo CSV o TXT a analizar.
    """
    try:
        # 1. Leer archivo
        print("\n⏳ Leyendo archivo...")
        encabezados, datos_crudos = leer_archivo(ruta_archivo)
        mostrar_exito(
            f"Archivo leído: {len(encabezados)} variable(s), {len(datos_crudos)} registro(s)"
        )

        # 2. Limpiar datos
        print("⏳ Limpiando datos...")
        resultado_limpieza = limpiar_datos(encabezados, datos_crudos)
        mostrar_exito("Datos limpiados")

        # Validar que queden datos suficientes
        if resultado_limpieza['filas_validas'] == 0:
            mostrar_error("No hay datos válidos después de la limpieza")
            return

        if resultado_limpieza['filas_validas'] < 2:
            mostrar_error("Se necesitan al menos 2 filas válidas para calcular la correlación")
            return

        # 3. Mostrar resumen y tabla
        mostrar_resumen_limpieza(resultado_limpieza)
        mostrar_tabla_datos(resultado_limpieza['datos'], resultado_limpieza['encabezados'])

        # 4. Seleccionar variables
        var1, var2 = seleccionar_variables(resultado_limpieza['encabezados'])

        # 5. Obtener datos de las variables seleccionadas
        datos_x = resultado_limpieza['datos_por_columna'][var1]
        datos_y = resultado_limpieza['datos_por_columna'][var2]

        # 6. Calcular correlación de Pearson
        print("\n⏳ Calculando correlación de Pearson...")
        resultado_pearson = calcular_pearson(datos_x, datos_y)
        mostrar_exito("Cálculo completado")

        # 7. Mostrar resultados
        mostrar_resultados_correlacion(var1, var2, resultado_pearson)

    except FileNotFoundError as e:
        mostrar_error(str(e))
    except ValueError as e:
        mostrar_error(str(e))
    except Exception as e:
        mostrar_error(f"Error inesperado: {str(e)}")


def main():
    """Función principal: muestra el menú y orquesta el flujo del programa."""
    mostrar_encabezado()

    while True:
        mostrar_menu_inicial()

        try:
            opcion = input("Selecciona una opción (1-2): ").strip()
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrumpido. ¡Hasta luego!\n")
            break

        if opcion == "1":
            try:
                ruta = obtener_ruta_archivo()
                realizar_analisis(ruta)

                continuar = input(
                    "\n¿Deseas realizar otro análisis? (s/n): "
                ).strip().lower()
                if continuar not in ('s', 'si', 'sí'):
                    print("\n👋 ¡Hasta luego!\n")
                    break

            except KeyboardInterrupt:
                print("\n\n👋 Programa interrumpido. ¡Hasta luego!\n")
                break

        elif opcion == "2":
            print("\n👋 ¡Hasta luego!\n")
            break

        else:
            mostrar_error("Opción no válida. Por favor ingresa 1 o 2.")


if __name__ == "__main__":
    main()
