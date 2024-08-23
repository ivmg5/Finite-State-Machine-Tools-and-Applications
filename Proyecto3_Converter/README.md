## Project 3: Automaton Converter Web Application

### Descripción

Este miniproyecto es una aplicación web desarrollada utilizando la biblioteca `shiny` para Python, diseñada para convertir reglas de producción en un autómata. Luego, el autómata se representa gráficamente utilizando la biblioteca `visual-automata`. La aplicación permite a los usuarios introducir reglas de producción y visualizar el autómata correspondiente, lo que facilita la comprensión y el análisis de las gramáticas formales y los autómatas finitos no deterministas (NFA).

### Estructura del Código

El proyecto se compone de los siguientes archivos:

1. **`app.py`**: Este es el punto de entrada de la aplicación `shiny`. Incluye la interfaz de usuario y la lógica para procesar las reglas de producción introducidas por el usuario. Convierte estas reglas en un autómata y llama al método `graph()` para generar y mostrar la representación gráfica del autómata.

2. **`automaton.py`**: Contiene la clase `Automaton`, que define la estructura y comportamiento del autómata. Incluye un método `graph()` modificado para utilizar la biblioteca `visual-automata`, que genera la representación gráfica del NFA basado en las reglas de producción ingresadas.

3. **`state.py`**: Define la clase `State`, que representa un estado en el autómata. Permite definir transiciones entre estados y almacenar callbacks que se ejecutan durante dichas transiciones.

### Notas Importantes

1. Esta aplicación no utiliza el lenguaje de programación `R`, sino la biblioteca `shiny` para Python. Esto fue confirmado como aceptable por el profesor.
2. Este proyecto reutiliza las clases `Automaton` y `State` del proyecto anterior de Análisis Léxico.
3. La única modificación significativa en `automaton.py` es en el método `graph()`, que ahora utiliza la biblioteca `visual-automata` para la representación gráfica.
4. El estado final `Z` se representa con un doble círculo en el autómata, en lugar de ser coloreado en rojo, lo cual también fue aprobado por el profesor.
5. El estado inicial `S` se denota con una flecha que apunta hacia él en el autómata.

### Requisitos

- **Lenguaje de Programación**: Python 3.x
- **Sistema Operativo**: Compatible con cualquier SO que soporte Python (Windows, macOS, Linux)
- **Dependencias**: `shiny`, `visual-automata`, `forbiddenfruit`, `frozendict`

### Cómo Ejecutar la Aplicación

1. **Instalar Graphviz**:

   Asegúrate de que `graphviz` esté instalado y en el PATH de tu sistema. Si no está instalado, puedes hacerlo con los siguientes comandos:

   - En Ubuntu:

     ```bash
     sudo apt-get install graphviz
     ```

   - En macOS:

     ```bash
     brew install graphviz
     ```

   - En Windows:

     Es recomendable utilizar WSL2 con Ubuntu y seguir las instrucciones para Ubuntu, ya que la instalación en Windows puede ser más complicada.

2. **Clonar el Repositorio e Instalar Dependencias**:

   Clona el repositorio, configura un entorno virtual, e instala las dependencias necesarias:

   ```bash
   git clone https://github.com/YOUR-USERNAME/automaton-graph-converter.git
   cd automaton-graph-converter
   python3 -m venv .venv
   source .venv/bin/activate
   pip install shiny visual-automata forbiddenfruit frozendict
   ```

3. **Ejecutar la Aplicación**:

   Ejecuta la aplicación utilizando el siguiente comando:

   ```bash
   shiny run app.py
   ```

4. **Acceder a la Aplicación**:

   Abre tu navegador web y ve a `http://localhost:8000/`. Desde allí, podrás introducir reglas de producción y generar gráficas del autómata resultante.
