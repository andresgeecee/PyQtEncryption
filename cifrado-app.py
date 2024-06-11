# ENTREGABLE FINAL - CÓDIGO ENCRIPTACIÓN
# Elaborado con el lenguaje Python y para la interfas grafica PyQt5
# Integrantes del proyecto: 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize
import random

def cifrado_unico(texto, clave):
    # Variable para almacenar el texto cifrado
    resultado = "" 
    # Semilla el generador de números aleatorios con la clave proporcionada
    random.seed(clave)
    # Itera sobre cada caracter en el texto de entrada  
    for char in texto:
        # Verifica si el caracter es una letra del alfabeto
        if char.isalpha():
            # Genera un número aleatorio entre 1 y 26
            aleatorio = random.randint(1, 26)
            # Calcula el nuevo código ASCII para el caracter
            nuevo_codigo = ord(char) + aleatorio
            # Si el caracter es mayúscula
            if char.isupper():  
                # Si el nuevo código excede el código ASCII de 'Z'
                if nuevo_codigo > ord('Z'):  
                    # Vuelve al inicio del alfabeto
                    nuevo_codigo -= 26  
            # Si el caracter es minúscula
            else:  
                # Si el nuevo código excede el código ASCII de 'z'
                if nuevo_codigo > ord('z'):
                    # Vuelve al inicio del alfabeto  
                    nuevo_codigo -= 26  
            # Agrega el caracter cifrado al resultado
            resultado += chr(nuevo_codigo)  
        # Si el caracter no es una letra del alfabeto
        else:  
            # Agrega el caracter tal como está (por ejemplo, espacio en blanco o puntuación)
            resultado += char  
    # Devuelve el texto cifrado
    return resultado  

def descifrado_unico(texto, clave):
    # Variable para almacenar el texto descifrado
    resultado = ""  
    # Semilla el generador de números aleatorios con la clave proporcionada
    random.seed(clave)  
    # Itera sobre cada caracter en el texto cifrado
    for char in texto:  
        # Verifica si el caracter es una letra del alfabeto
        if char.isalpha():  
            # Genera un número aleatorio entre 1 y 26
            aleatorio = random.randint(1, 26)  
            # Calcula el código ASCII original del caracter
            nuevo_codigo = ord(char) - aleatorio  
            # Si el caracter es mayúscula
            if char.isupper():  
                # Si el código original es menor que el código ASCII de 'A'
                if nuevo_codigo < ord('A'):  
                    # Vuelve al final del alfabeto
                    nuevo_codigo += 26  
            # Si el caracter es minúscula
            else:  
                # Si el código original es menor que el código ASCII de 'a'
                if nuevo_codigo < ord('a'):  
                    # Vuelve al final del alfabeto
                    nuevo_codigo += 26  
            # Agrega el caracter descifrado al resultado
            resultado += chr(nuevo_codigo)  
        # Si el caracter no es una letra del alfabeto
        else:  
            # Agrega el caracter tal como está (por ejemplo, espacio en blanco o puntuación)
            resultado += char  
    # Devuelve el texto descifrado
    return resultado  

# Tabla de sustitución donde cada letra del alfabeto se sustituye por otra letra
tabla_sustitucion = {
    "A": "X", "B": "Y", "C": "Z", "D": "A", "E": "B", "F": "C", "G": "D", "H": "E", "I": "F", "J": "G", "K": "H", 
    "L": "I", "M": "J", "N": "K", "O": "L", "P": "M", "Q": "N", "R": "O", "S": "P", "T": "Q", "U": "R", "V": "S", 
    "W": "T", "X": "U", "Y": "V", "Z": "W",
    "a": "x", "b": "y", "c": "z", "d": "a", "e": "b", "f": "c", "g": "d", "h": "e", "i": "f", "j": "g", "k": "h", 
    "l": "i", "m": "j", "n": "k", "o": "l", "p": "m", "q": "n", "r": "o", "s": "p", "t": "q", "u": "r", "v": "s", 
    "w": "t", "x": "u", "y": "v", "z": "w"
}

def cifrado_sustitucion(texto):
    # Variable para almacenar el texto cifrado
    resultado = ""  
    # Itera sobre cada caracter en el texto de entrada
    for char in texto:  
        # Verifica si el caracter está en la tabla de sustitución
        if char in tabla_sustitucion:  
            # Agrega el caracter sustituido al resultado
            resultado += tabla_sustitucion[char]  
        # Si el caracter no está en la tabla de sustitución
        else:  
            # Agrega el caracter tal como está (por ejemplo, espacio en blanco o puntuación)
            resultado += char  
    # Devuelve el texto cifrado
    return resultado  

def descifrado_sustitucion(texto):
    # Variable para almacenar el texto descifrado
    resultado = ""  
    # Crea una tabla de sustitución inversa intercambiando las claves y los valores de la tabla de sustitución original
    tabla_sustitucion_inversa = {v: k for k, v in tabla_sustitucion.items()}
    # Itera sobre cada caracter en el texto cifrado
    for char in texto:  
        # Verifica si el caracter está en la tabla de sustitución inversa
        if char in tabla_sustitucion_inversa:  
            # Agrega el caracter original al resultado
            resultado += tabla_sustitucion_inversa[char]  
        # Si el caracter no está en la tabla de sustitución inversa
        else:  
            # Agrega el caracter tal como está (por ejemplo, espacio en blanco o puntuación)
            resultado += char  
    # Devuelve el texto descifrado
    return resultado  

def cifrado_cesar(texto):
    # Variable para almacenar el texto cifrado
    resultado = ""  
    # Itera sobre cada caracter en el texto de entrada
    for char in texto:  
        # Verifica si el caracter es una letra del alfabeto
        if char.isalpha():  
            # Obtiene el código ASCII del caracter
            codigo = ord(char)  
            # Si el caracter es mayúscula
            if char.isupper():  
                # Aplica el cifrado César (desplazamiento de 3) a letras mayúsculas
                nuevo_codigo = (codigo - 65 + 3) % 26 + 65 
            # Si el caracter es minúscula 
            else:  
                # Aplica el cifrado César (desplazamiento de 3) a letras minúsculas
                nuevo_codigo = (codigo - 97 + 3) % 26 + 97  
            # Agrega el caracter cifrado al resultado
            resultado += chr(nuevo_codigo)  
        # Si el caracter no es una letra del alfabeto
        else: 
            # Agrega el caracter tal como está (por ejemplo, espacio en blanco o puntuación) 
            resultado += char  
    # Devuelve el texto cifrado
    return resultado  

def descifrado_cesar(texto):
    # Variable para almacenar el texto descifrado
    resultado = ""  
    # Itera sobre cada caracter en el texto cifrado
    for char in texto:  
        # Verifica si el caracter es una letra del alfabeto
        if char.isalpha():  
            # Obtiene el código ASCII del caracter
            codigo = ord(char)  
            # Si el caracter es mayúscula
            if char.isupper():  
                # Aplica el descifrado César (desplazamiento de 3) a letras mayúsculas
                nuevo_codigo = (codigo - 65 - 3) % 26 + 65  
            # Si el caracter es minúscula
            else:  
                # Aplica el descifrado César (desplazamiento de 3) a letras minúsculas
                nuevo_codigo = (codigo - 97 - 3) % 26 + 97  
            # Agrega el caracter descifrado al resultado
            resultado += chr(nuevo_codigo)  
        # Si el caracter no es una letra del alfabeto
        else:  
            # Agrega el caracter tal como está (por ejemplo, espacio en blanco o puntuación)
            resultado += char  
    # Devuelve el texto descifrado
    return resultado  

class CipherSelection(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Selección de Cifrado")
        self.setMinimumSize(QSize(300, 200))
        self.resize(400, 300)
        layout = QVBoxLayout()

        self.unique_button = QPushButton("Cifrado Único")
        self.unique_button.clicked.connect(self.open_unique_window)
        layout.addWidget(self.unique_button)

        self.substitution_button = QPushButton("Cifrado de Sustitución Simple")
        self.substitution_button.clicked.connect(self.open_substitution_window)
        layout.addWidget(self.substitution_button)

        self.caesar_button = QPushButton("Cifrado César")
        self.caesar_button.clicked.connect(self.open_caesar_window)
        layout.addWidget(self.caesar_button)

        self.setLayout(layout)
        self.setStyleSheet("background-color: black; color: lime;")

    def open_unique_window(self):
        self.unique_window = UniqueWindow(self)
        self.unique_window.show()
        self.unique_window.setStyleSheet("background-color: black; color: lime;")
        self.hide()

    def open_substitution_window(self):
        self.substitution_window = SubstitutionWindow(self)
        self.substitution_window.show()
        self.substitution_window.setStyleSheet("background-color: black; color: lime;")
        self.hide()

    def open_caesar_window(self):
        self.caesar_window = CaesarWindow(self)
        self.caesar_window.show()
        self.caesar_window.setStyleSheet("background-color: black; color: lime;")
        self.hide()

class UniqueWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Cifrado Único")
        layout = QVBoxLayout()

        self.text_label = QLabel("Texto:")
        layout.addWidget(self.text_label)
        self.text_edit = QLineEdit()
        layout.addWidget(self.text_edit)

        self.key_label = QLabel("Clave:")
        layout.addWidget(self.key_label)
        self.key_edit = QLineEdit()
        layout.addWidget(self.key_edit)

        self.encrypt_button = QPushButton("Cifrar")
        self.encrypt_button.clicked.connect(self.encrypt)
        layout.addWidget(self.encrypt_button)

        self.decrypt_button = QPushButton("Descifrar")
        self.decrypt_button.clicked.connect(self.decrypt)
        layout.addWidget(self.decrypt_button)

        self.result_label = QLabel("Resultado:")
        layout.addWidget(self.result_label)
        self.result_edit = QLineEdit()
        self.result_edit.setReadOnly(True)
        layout.addWidget(self.result_edit)

        self.history_label = QLabel("Historial:")
        layout.addWidget(self.history_label)
        self.history_list = QListWidget()
        layout.addWidget(self.history_list)

        self.back_button = QPushButton("Volver a la selección de cifrado")
        self.back_button.clicked.connect(self.back_to_selection)
        layout.addWidget(self.back_button)

        self.setLayout(layout)
        self.setStyleSheet("background-color: black; color: lime;")

    def encrypt(self):
        text = self.text_edit.text()
        key = self.key_edit.text()
        encrypted_text = cifrado_unico(text, key)
        self.result_edit.setText(encrypted_text)
        self.history_list.addItem(f"Cifrado '{text}' con clave '{key}' a '{encrypted_text}'")

    def decrypt(self):
        text = self.text_edit.text()
        key = self.key_edit.text()
        decrypted_text = descifrado_unico(text, key)
        self.result_edit.setText(decrypted_text)
        self.history_list.addItem(f"Descifrado '{text}' con clave '{key}' a '{decrypted_text}'")

    def back_to_selection(self):
        self.parent.show()
        self.close()

class SubstitutionWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Cifrado de Sustitución Simple")
        layout = QVBoxLayout()

        self.text_label = QLabel("Texto:")
        layout.addWidget(self.text_label)
        self.text_edit = QLineEdit()
        layout.addWidget(self.text_edit)

        self.encrypt_button = QPushButton("Cifrar")
        self.encrypt_button.clicked.connect(self.encrypt)
        layout.addWidget(self.encrypt_button)
        self.decrypt_button = QPushButton("Descifrar")
        self.decrypt_button.clicked.connect(self.decrypt)
        layout.addWidget(self.decrypt_button)

        self.result_label = QLabel("Resultado:")
        layout.addWidget(self.result_label)
        self.result_edit = QLineEdit()
        self.result_edit.setReadOnly(True)
        layout.addWidget(self.result_edit)

        self.history_label = QLabel("Historial:")
        layout.addWidget(self.history_label)
        self.history_list = QListWidget()
        layout.addWidget(self.history_list)

        self.back_button = QPushButton("Volver a la selección de cifrado")
        self.back_button.clicked.connect(self.back_to_selection)
        layout.addWidget(self.back_button)

        self.setLayout(layout)
        self.setStyleSheet("background-color: black; color: lime;")

    def encrypt(self):
        text = self.text_edit.text()
        encrypted_text = cifrado_sustitucion(text)
        self.result_edit.setText(encrypted_text)
        self.history_list.addItem(f"Cifrado '{text}' a '{encrypted_text}'")

    def decrypt(self):
        text = self.text_edit.text()
        decrypted_text = descifrado_sustitucion(text)
        self.result_edit.setText(decrypted_text)
        self.history_list.addItem(f"Descifrado '{text}' a '{decrypted_text}'")

    def back_to_selection(self):
        self.parent.show()
        self.close()

class CaesarWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Cifrado César")
        layout = QVBoxLayout()

        self.text_label = QLabel("Texto:")
        layout.addWidget(self.text_label)
        self.text_edit = QLineEdit()
        layout.addWidget(self.text_edit)

        self.encrypt_button = QPushButton("Cifrar")
        self.encrypt_button.clicked.connect(self.encrypt)
        layout.addWidget(self.encrypt_button)
        self.decrypt_button = QPushButton("Descifrar")
        self.decrypt_button.clicked.connect(self.decrypt)
        layout.addWidget(self.decrypt_button)

        self.result_label = QLabel("Resultado:")
        layout.addWidget(self.result_label)
        self.result_edit = QLineEdit()
        self.result_edit.setReadOnly(True)
        layout.addWidget(self.result_edit)

        self.history_label = QLabel("Historial:")
        layout.addWidget(self.history_label)
        self.history_list = QListWidget()
        layout.addWidget(self.history_list)

        self.back_button = QPushButton("Volver a la selección de cifrado")
        self.back_button.clicked.connect(self.back_to_selection)
        layout.addWidget(self.back_button)

        self.setLayout(layout)
        self.setStyleSheet("background-color: black; color: lime;")

    def encrypt(self):
        text = self.text_edit.text()
        encrypted_text = cifrado_cesar(text)
        self.result_edit.setText(encrypted_text)
        self.history_list.addItem(f"Cifrado '{text}' a '{encrypted_text}' con un desplazamiento de 3")

    def decrypt(self):
        text = self.text_edit.text()
        decrypted_text = descifrado_cesar(text)
        self.result_edit.setText(decrypted_text)
        self.history_list.addItem(f"Descifrado '{text}' a '{decrypted_text}' con un desplazamiento de 3")

    def back_to_selection(self):
        self.parent.show()
        self.close()

if __name__ == "__main__":
    # Crea una instancia de la aplicación QApplication con los argumentos de la línea de comandos
    app = QApplication(sys.argv) 
    # Crea una instancia de la clase CipherSelection, que representa la ventana principal de la aplicación
    cipher_selection = CipherSelection() 
    # Muestra la ventana principal
    cipher_selection.show()
    # Inicia el bucle de eventos de la aplicación y sale con el código de salida del bucle
    sys.exit(app.exec_())