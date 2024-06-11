
# Proyecto de Encriptación

Este proyecto implementa diferentes métodos de encriptación y desencriptación utilizando Python y la biblioteca PyQt5 para la interfaz gráfica de usuario. El proyecto fue desarrollado por Jose Andres Galarza Chavez como parte de un entregable final.

## Descripción del Proyecto

El proyecto permite al usuario cifrar y descifrar texto utilizando tres métodos diferentes:

1. **Cifrado Único**: Un método de cifrado simple basado en un generador de números aleatorios.
2. **Cifrado de Sustitución Simple**: Un método de sustitución donde cada letra del alfabeto se sustituye por otra letra según una tabla predefinida.
3. **Cifrado César**: Un método clásico de cifrado que desplaza las letras del alfabeto un número fijo de posiciones.

## Requisitos

- Python 3.x
- PyQt5

## Instalación

1. Clona el repositorio en tu máquina local:

    ```bash
    git clone https://github.com/andresgeecee/PyQtEncryption.git
    cd PyQtEncryption
    ```

2. Instala los paquetes requeridos:

    ```bash
    pip install pyqt5
    ```

## Uso

Para ejecutar la aplicación, simplemente ejecuta el archivo `cifrado-app.py`:

```bash
python main.py
```

## Funcionalidades

### Cifrado Único

- Introduce el texto que deseas cifrar.
- Introduce una clave para generar el texto cifrado.
- Haz clic en el botón "Cifrar" para cifrar el texto.
- Haz clic en el botón "Descifrar" para descifrar el texto.

### Cifrado de Sustitución Simple

- Introduce el texto que deseas cifrar.
- Haz clic en el botón "Cifrar" para cifrar el texto.
- Haz clic en el botón "Descifrar" para descifrar el texto.

### Cifrado César

- Introduce el texto que deseas cifrar.
- Haz clic en el botón "Cifrar" para cifrar el texto (desplazamiento de 3).
- Haz clic en el botón "Descifrar" para descifrar el texto (desplazamiento de 3).

## Estructura del Proyecto

- `main.py`: Archivo principal que ejecuta la aplicación.
- `cifrado_unico.py`: Módulo que contiene las funciones de cifrado y descifrado único.
- `cifrado_sustitucion.py`: Módulo que contiene las funciones de cifrado y descifrado de sustitución.
- `cifrado_cesar.py`: Módulo que contiene las funciones de cifrado y descifrado César.
- `gui.py`: Módulo que contiene la lógica de la interfaz gráfica usando PyQt5.

## 📁 Anexos

![Texto alternativo](https://github.com/andresgeecee/PyQtEncryption/blob/master/img/proyecto-cifrados%20-%20Visual%20Studio%20Code.png?raw=true)
