import telepot
import requests
import zipfile
import rarfile  # Si necesitas soporte para RAR
import tarfile
import os
import time
from telepot.loop import MessageLoop

# TOKEN de tu bot (reemplaza con el tuyo)
TOKEN ="7501411396:AAFXv_unSqYDi9i_8ni85rOMHDsC93Xzbxw"

bot = telepot.Bot(TOKEN)

# Función para manejar mensajes
def handler(msg):
    msg_type, chat_type, chat_id = telepot.glance(msg)

    if msg_type == 'text':
        texto = msg['text']

        if texto.startswith('/descargar'):
            # Obtener la URL del mensaje
            url = texto.split(' ')[1]  # Asume que la URL está después del comando /descargar

            try:
                # Descargar el archivo
                response = requests.get(url, stream=True)
                response.raise_for_status()  # Lanza una excepción si la descarga falla

                # Guardar el archivo temporalmente
                with open('archivo_descargado.zip', 'wb') as f:  # Ajusta la extensión según el tipo de archivo
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)

                # Descomprimir el archivo
                if url.endswith('.zip'):
                    with zipfile.ZipFile('archivo_descargado.zip', 'r') as zip_ref:
                        zip_ref.extractall('archivos_descomprimidos')
                # ... (Agregar soporte para otros tipos de archivos: rar, tar, etc.)

                # Mostrar archivos y carpetas
                mostrar_archivos(chat_id, 'archivos_descomprimidos')

            except requests.exceptions.RequestException as e:
                bot.sendMessage(chat_id, f"Error al descargar el archivo: {e}")
            except Exception as e:
                bot.sendMessage(chat_id, f"Error al procesar el archivo: {e}")

# Función para mostrar archivos y carpetas
def mostrar_archivos(chat_id, ruta):
    archivos = os.listdir(ruta)
    mensaje = "Archivos y carpetas:\n"

    for archivo in archivos:
        mensaje += f"- {archivo}\n"

    bot.sendMessage(chat_id, mensaje)

# Bucle principal del bot
MessageLoop(bot, handler).run_as_thread()

while True:
    time.sleep(10)

