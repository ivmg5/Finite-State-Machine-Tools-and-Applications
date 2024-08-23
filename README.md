# Herramientas y Aplicaciones de Máquinas de Estados Finitos

Este repositorio contiene una colección de tres miniproyectos enfocados en la implementación y aplicación de Máquinas de Estados Finitos (FSM). Cada proyecto demuestra diferentes usos de las FSM, abarcando desde el análisis léxico hasta la representación gráfica de autómatas derivados de reglas de producción. Los proyectos están implementados en Python y muestran el poder de las FSM en diversos contextos computacionales.

## Descripción General de los Proyectos

### 1. Programa Lexer Aritmético

**Descripción**: Este proyecto implementa una Máquina de Estados Finitos Determinista (DFSM) para analizar y procesar expresiones aritméticas. El lexer categoriza secuencias de caracteres en tokens como enteros, números de punto flotante, identificadores, operadores y símbolos, según un conjunto predefinido de reglas y transiciones. El programa lee de un archivo de entrada y genera una tabla de tokens y sus respectivos tipos.

**Características Clave**:
- Reconoce enteros, números de punto flotante, operadores, símbolos e identificadores.
- Utiliza una máquina de estados para navegar a través de la cadena de entrada, haciendo transiciones entre estados según el carácter actual.
- Genera una representación gráfica del autómata.

**Cómo Ejecutar**:
- Prepara un archivo de entrada (`input.txt`) que contenga expresiones aritméticas.
- Ejecuta el programa con `python main.py`.
- Opcionalmente, genera una representación gráfica del autómata descomentando la línea relevante en el código.

Para más instrucciones detalladas, consulta la carpeta específica del proyecto: [Programa Lexer Aritmético](./Arithmetic-Lexer-Program).

### 2. Analizador Léxico de Python

**Descripción**: Este proyecto proporciona un analizador léxico para código Python, identificando categorías léxicas como palabras reservadas, operadores, literales, comentarios, identificadores y estructuras de datos. El analizador utiliza expresiones regulares para escanear el código y resaltar diferentes tokens en un archivo HTML generado.

**Características Clave**:
- Identifica y resalta palabras clave, operadores, literales, comentarios y más en Python.
- Genera el código analizado con resaltado de sintaxis en un archivo HTML (`out.html`).
- Proporciona una interfaz fácil de usar para entrada y salida.

**Cómo Ejecutar**:
- Prepara los archivos requeridos (`main.py`, `template.html`, `input.txt`).
- Ejecuta el programa con `python main.py`.
- Visualiza la sintaxis resaltada en el archivo generado `out.html`.

Para más instrucciones detalladas, consulta la carpeta específica del proyecto: [Analizador Léxico de Python](./Python-Lexical-Analyzer).

### 3. Aplicación Web de Conversión de Autómatas

**Descripción**: Esta aplicación web convierte reglas de producción en un autómata y luego representa gráficamente el autómata utilizando la biblioteca `visual-automata`. La aplicación está construida utilizando la biblioteca `shiny` para Python, proporcionando una interfaz simple e interactiva para que los usuarios ingresen reglas de producción y visualicen el NFA (Autómata Finito No Determinista) resultante.

**Características Clave**:
- Convierte reglas de producción proporcionadas por el usuario en un NFA.
- Representa gráficamente el NFA con un diagrama claro e interactivo.
- Utiliza la biblioteca `shiny` para la funcionalidad de la aplicación web y `visual-automata` para la representación gráfica.

**Cómo Ejecutar**:
- Asegúrate de que `graphviz` esté instalado y accesible en el PATH.
- Clona el repositorio, configura un entorno virtual e instala las dependencias necesarias.
- Ejecuta la aplicación web con `shiny run app.py`.
- Accede a la aplicación en `http://localhost:8000/` en tu navegador web.

Para más instrucciones detalladas, consulta la carpeta específica del proyecto: [Aplicación Web de Conversión de Autómatas](./Automaton-Converter-Web-Application).

## Instalación

1. **Clonar el Repositorio**:

   ```bash
   git clone https://github.com/YOUR-USERNAME/Finite-State-Machine-Tools-and-Applications.git
   cd Finite-State-Machine-Tools-and-Applications
   ```

2. **Configurar el Entorno de Python**:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Instalar Graphviz (Para la Aplicación Web de Conversión de Autómatas)**:

   - En Ubuntu:

     ```bash
     sudo apt-get install graphviz
     ```

   - En macOS:

     ```bash
     brew install graphviz
     ```

   - En Windows:

     Se recomienda utilizar WSL2 con Ubuntu y seguir las instrucciones para Ubuntu.
