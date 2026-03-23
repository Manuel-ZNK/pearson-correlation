"""
Módulo para lectura de archivos de datos.
Soporta formatos .txt y .csv
"""


def leer_archivo(ruta_archivo):
    """
    Lee un archivo CSV o TXT y retorna encabezados y datos.

    Args:
        ruta_archivo (str): Ruta del archivo a leer.

    Returns:
        tuple: (encabezados, datos) - Nombres de variables y filas de datos.

    Raises:
        FileNotFoundError: Si el archivo no existe.
        ValueError: Si el archivo está vacío o mal formateado.
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        if not lineas:
            raise ValueError("El archivo está vacío")

        # Limpiar saltos de línea
        lineas = [linea.strip() for linea in lineas]

        # Eliminar líneas vacías
        lineas = [linea for linea in lineas if linea]

        if len(lineas) < 2:
            raise ValueError(
                "El archivo debe contener al menos encabezados y una fila de datos"
            )

        # Extraer encabezados (primera fila)
        encabezados = [col.strip() for col in lineas[0].split(',')]

        # Extraer datos (resto de filas)
        datos = []
        for linea in lineas[1:]:
            fila = [valor.strip() for valor in linea.split(',')]
            datos.append(fila)

        return encabezados, datos

    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{ruta_archivo}' no existe")
    except ValueError:
        raise
    except Exception as e:
        raise ValueError(f"Error al leer el archivo: {str(e)}")


def obtener_ruta_archivo():
    """
    Solicita al usuario la ruta de un archivo y la valida.

    Returns:
        str: Ruta del archivo validada.
    """
    while True:
        ruta = input("\nIngresa la ruta del archivo (.txt o .csv): ").strip()

        if not ruta:
            print("❌ La ruta no puede estar vacía")
            continue

        if not (ruta.endswith('.txt') or ruta.endswith('.csv')):
            print("❌ El archivo debe ser .txt o .csv")
            continue

        try:
            leer_archivo(ruta)
            return ruta
        except FileNotFoundError:
            print(f"❌ Archivo no encontrado: {ruta}")
        except ValueError as e:
            print(f"❌ {str(e)}")
