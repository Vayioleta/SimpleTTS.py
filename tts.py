import os
import shutil
from gtts import gTTS

current_directory = os.path.dirname(__file__)
texto_file_path = os.path.join(current_directory, "input.txt")

def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='es')  # Elige el idioma (en este caso, español)
    tts.save(filename)

# Lee el contenido del archivo de texto
with open(texto_file_path, "r", encoding="utf-8") as texto_file:
    texto = texto_file.read()
    text_to_speech( texto, "audio_salida.mp3" )

print("File Saved")