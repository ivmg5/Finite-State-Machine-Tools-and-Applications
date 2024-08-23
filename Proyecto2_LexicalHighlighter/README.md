## Project 2: Python Lexical Analyzer

### Descripción

Este miniproyecto implementa un analizador léxico en Python, diseñado para identificar y categorizar los diferentes componentes léxicos en código fuente de Python. El programa utiliza expresiones regulares para reconocer palabras reservadas, operadores, literales, comentarios, identificadores y estructuras de datos en el código fuente. El resultado es un archivo HTML que muestra el código original con un resaltado de sintaxis que facilita la identificación de cada uno de estos elementos.

### Estructura del Código

El proyecto se compone de los siguientes archivos:

1. **`main.py`**: Este es el script principal que ejecuta el análisis léxico. Lee el código fuente desde un archivo de entrada (`input.txt`), aplica una serie de expresiones regulares para identificar los diferentes componentes léxicos, y genera un archivo HTML (`out.html`) que presenta el código con resaltado de sintaxis.

2. **`template.html`**: Este archivo HTML sirve como plantilla para la salida generada. Contiene un marcador de posición `{{CODE}}` que será reemplazado con el código fuente resaltado.

3. **`input.txt`**: Contiene el código fuente en Python que será analizado por el programa. Este archivo debe estar en el mismo directorio que `main.py` y `template.html`.

### Requisitos

- **Lenguaje de Programación**: Python 3.x
- **Sistema Operativo**: Compatible con cualquier SO que soporte Python (Windows, macOS, Linux)
- **Software Adicional**: Ninguno

### Instalación

Asegúrate de tener Python 3.x instalado en tu máquina. No se requieren otras instalaciones específicas.

### Cómo Ejecutar el Programa

1. **Preparar el Entorno**:
   - Guarda los archivos `main.py`, `template.html`, e `input.txt` en el mismo directorio.

2. **Crear el Archivo de Entrada**:
   - El archivo `input.txt` debe contener el código fuente en Python que deseas analizar. Puedes escribir o pegar código Python en este archivo para su análisis.

3. **Ejecutar el Programa**:
   - Abre una terminal o línea de comandos y navega hasta el directorio donde se encuentran los archivos.
   - Ejecuta el programa con el siguiente comando:

     ```bash
     python main.py
     ```

   - Esto procesará el código en `input.txt` y generará un archivo HTML (`out.html`) con el código resaltado.

4. **Revisar el Resultado**:
   - Después de ejecutar el programa, abre el archivo `out.html` con un navegador web para ver el código fuente con las categorías léxicas destacadas según los colores y estilos definidos en `template.html`. Por ejemplo:
     - Comentarios: Resaltados en gris y en itálica.
     - Literales: Resaltados en verde.
     - Palabras clave (`def`, `if`, etc.): Resaltadas en rojo y en negrita.

### Ejemplo de Categorías Léxicas

El programa reconoce las siguientes categorías léxicas:

1. **Palabras Reservadas**: Como `def`, `if`, `else`, `return`, `class`, `for`, `while`, `break`, `continue`, y operadores lógicos (`and`, `or`, `not`).
2. **Operadores**: Operadores aritméticos (`+`, `-`, `*`, `/`, `**`, `//`, `%`), operadores de comparación (`==`, `!=`, `<`, `>`, `<=`, `>=`), y operadores de asignación (`=`, `+=`, `-=` etc.).
3. **Literales**: Incluye números enteros y flotantes (`123`, `3.14`), literales de cadena (`"Hola"`, `'Mundo'`), booleanos (`True`, `False`) y el literal `None`.
4. **Comentarios**: Denotados por `#` y todo lo que sigue en la línea.
5. **Identificadores**: Nombres de variables y funciones que comienzan con una letra o un guion bajo, seguido de letras, guiones bajos o dígitos.
6. **Estructuras de Datos**: Listas (`[1, 2, 3]`), tuplas (`(1, 2, 3)`), diccionarios (`{'clave': 'valor'}`) y conjuntos (`{1, 2, 3}`).

### Solución de Problemas

- **Python no Reconocido**: Asegúrate de que Python esté correctamente instalado y añadido a la variable PATH de tu sistema.
- **Error al Leer Archivos**: Verifica que los archivos `main.py`, `template.html`, e `input.txt` estén en el mismo directorio y que sus nombres estén escritos correctamente.
- **HTML no Resalta Correctamente**: Asegúrate de que `input.txt` esté correctamente formateado y sigue las convenciones esperadas por el programa.
