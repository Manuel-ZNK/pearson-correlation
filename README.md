# 📊 Análisis de Correlación de Pearson

Programa en Python para calcular la **correlación de Pearson** entre dos variables a partir de un archivo CSV o TXT, **sin usar ninguna librería externa** (sólo Python estándar).

---

## Descripción general

El programa lee un archivo de datos, limpia los registros inválidos, permite seleccionar dos variables y calcula manualmente el coeficiente de correlación de Pearson mostrando el resultado con una interpretación cualitativa y una barra visual.

---

## Requisitos

- Python 3.7 o superior
- Sin dependencias externas (no se usan pandas, numpy, scipy ni ninguna otra librería de terceros)

---

## Instalación

```bash
# Clona el repositorio
git clone https://github.com/Manuel-ZNK/pearson-correlation.git
cd pearson-correlation
```

No es necesario instalar nada más.

---

## Uso del programa

```bash
python main.py
```

### Flujo interactivo

1. Selecciona la opción **1** en el menú.
2. Ingresa la ruta del archivo `.csv` o `.txt` (p. ej. `datos_ejemplo.csv`).
3. El programa mostrará el resumen de limpieza y la tabla de datos.
4. Selecciona dos variables por **nombre** o por **índice** (número entre corchetes).
5. El programa calcula y muestra el coeficiente de Pearson con su interpretación.
6. Puedes repetir el análisis con otro par de variables o cargar otro archivo.

---

## Estructura de archivos

```
pearson-correlation/
├── main.py            # Orquesta el flujo principal del programa
├── lector.py          # Lectura de archivos CSV/TXT
├── limpiador.py       # Validación y limpieza de datos
├── analisis.py        # Cálculo manual de la correlación de Pearson
├── salida.py          # Presentación formateada de resultados
├── datos_ejemplo.csv  # Archivo CSV de ejemplo para pruebas
└── README.md          # Documentación del proyecto
```

---

## Ejemplo de datos (`datos_ejemplo.csv`)

```
edad,peso,altura,ingresos
25,70,1.75,2500
30,75,1.80,3000
28,72,1.78,2800
...
```

La **primera fila** debe contener los nombres de las variables (encabezados).  
Las filas con valores vacíos, no numéricos o con número incorrecto de columnas son descartadas automáticamente.

---

## Fórmula de Pearson

$$r = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2 \cdot \sum_{i=1}^{n}(y_i - \bar{y})^2}}$$

Implementación paso a paso en `analisis.py`:

1. Calcular promedios **x̄** e **ȳ**.
2. Calcular diferencias `(xi - x̄)` y `(yi - ȳ)`.
3. Sumar los productos de las diferencias (numerador).
4. Sumar los cuadrados de cada diferencia.
5. Calcular la raíz cuadrada del producto de las sumas de cuadrados (denominador).
6. Dividir numerador entre denominador.

---

## Interpretación de resultados

| Rango de \|r\| | Interpretación              |
|---------------|-----------------------------|
| 0.8 – 1.0     | Correlación fuerte          |
| 0.5 – 0.8     | Correlación moderada        |
| 0.3 – 0.5     | Correlación débil           |
| 0.0 – 0.3     | Sin correlación significativa |

El signo indica la **dirección**:  
- **Positivo** → cuando X sube, Y también sube.  
- **Negativo** → cuando X sube, Y baja.
