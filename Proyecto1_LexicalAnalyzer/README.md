## Project 1: Arithmetic Lexer Program

### Descripción

Este miniproyecto implementa un Autómata Finito Determinista (AFD) utilizando Python, diseñado para analizar y procesar expresiones aritméticas. El autómata clasifica secuencias de caracteres en distintos tokens como enteros, números flotantes, identificadores, operadores y símbolos, de acuerdo con un conjunto predefinido de reglas y transiciones. Este programa es una herramienta fundamental para entender cómo funcionan los autómatas finitos en el contexto de la lexicografía y la teoría de lenguajes formales.

### Estructura del Código

El proyecto se compone de los siguientes módulos:

1. **`state.py`**: Define la clase `State`, que representa un estado en el autómata. Cada estado puede tener transiciones hacia otros estados, las cuales son disparadas por símbolos específicos. Además, las transiciones pueden ejecutar funciones (callbacks) cuando se activan.

2. **`automaton.py`**: Contiene la clase `Automaton`, que define el comportamiento general del autómata. Esta clase incluye métodos para hacer coincidir cadenas de entrada con el autómata (`match`) y para generar una representación gráfica del autómata (`graph`).

3. **`sm.py`**: Define el autómata específico para este lexer. Aquí se construyen los estados y se definen las transiciones entre ellos, estableciendo así la lógica que permite identificar los diferentes tipos de tokens en una expresión aritmética.

4. **`main.py`**: Es el punto de entrada del programa. Carga el archivo de entrada que contiene las expresiones aritméticas, ejecuta el autómata sobre cada línea del archivo y muestra los tokens y sus tipos correspondientes en la consola.

### Requisitos

- **Lenguaje de Programación**: Python 3.x
- **Sistema Operativo**: Compatible con cualquier SO que soporte Python (Windows, macOS, Linux)
- **Software Adicional**: Ninguno

### Instalación

No se requiere una instalación específica más allá de tener Python 3.x instalado en tu máquina. Puedes descargar Python desde el sitio oficial en [python.org](https://www.python.org/).

### Cómo Ejecutar el Programa

1. **Preparar el Entorno**:
   - Asegúrate de que los archivos del programa (`state.py`, `automaton.py`, `sm.py`, `main.py`) estén guardados en el mismo directorio.
   - Crea un archivo de texto de entrada llamado `input.txt` en el mismo directorio, que contenga las expresiones aritméticas que deseas analizar.

2. **Ejecutar el Programa**:
   - Abre una terminal o línea de comandos y navega hasta el directorio donde se encuentran los archivos.
   - Ejecuta el programa con el siguiente comando:

     ```bash
     python main.py
     ```

   - Esto procesará las expresiones en `input.txt` y mostrará los tokens y sus tipos correspondientes en la consola.

3. **Salida del Programa**:
   - El programa imprime una tabla en la consola con dos columnas: `Token` y `Type`. La columna `Token` muestra el token real extraído del archivo de entrada, mientras que la columna `Type` indica la categoría de cada token (por ejemplo, `variable`, `integer`, `assignment`, `sum`, `subtract`, `product`, `division`, `left parenthesis`, `right parenthesis`).

4. **Generación de Gráficos** (Opcional):
   - Si deseas visualizar gráficamente el autómata, puedes descomentar la línea correspondiente en `main.py` que genera el archivo `automaton.png`. Este archivo mostrará una representación visual del autómata, lo cual puede ser útil para entender mejor su estructura y funcionamiento.

### Ejemplo de Formato de Entrada

El archivo de entrada (`input.txt`) debe contener expresiones aritméticas correctamente formateadas según las especificaciones del proyecto:

**Formato Correcto:**

```text
b=7
a = 32.4 * ( - 8.6 - b ) / 6.1
d=a*b
```

**Formato Incorrecto:**

- Números negativos o operadores unarios aplicados directamente a números (e.g., `-5` o `+3`).
- Nombres de variables con letras mayúsculas o caracteres no alfabéticos (e.g., `Var1`, `a_2`).
- Uso de operadores en contextos no permitidos (e.g., `++` o `**`).

### Solución de Problemas

- **Python no Reconocido**: Asegúrate de que Python esté correctamente instalado en tu sistema y añadido a la variable PATH de tu entorno.
- **Error de Archivo No Encontrado**: Verifica que el archivo `input.txt` esté en el mismo directorio que `main.py` y que el path en la terminal coincida con la ubicación de estos archivos.
- **Error de Caracter Inválido**: Revisa tu archivo de entrada para asegurarte de que solo contenga caracteres que coincidan con las reglas de tokenización especificadas en la descripción del proyecto.

### Generación de Representación Gráfica del Autómata

El archivo `automaton.py` incluye un método `graph()` que genera un gráfico del autómata utilizando `networkx` y `matplotlib`. Este gráfico muestra los estados y transiciones del autómata, lo cual es especialmente útil para la visualización y depuración del autómata. La imagen resultante se guarda como `automaton.png` en el directorio del proyecto.
