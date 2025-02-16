import gspread
from google.oauth2.service_account import Credentials
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Ruta al archivo JSON de credenciales no se debe codificar aquí.
CREDENTIALS_PATH = os.getenv("json.json")  # Se recomienda usar variables de entorno

# ID de la hoja de cálculo
1-B5vl7z1PYtznEQB_23D3tVSIIrc-J7M2BS34Hguw3Q = os.getenv("1-B5vl7z1PYtznEQB_23D3tVSIIrc-J7M2BS34Hguw3Q")  # También debería estar en variable de entorno

# Token del bot de Telegram
BOT_TOKEN = os.getenv("7501411396:AAFXv_unSqYDi9i_8ni85rOMHDsC93Xzbxw")  # Se debe cargar desde la variable de entorno

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(CREDENTIALS_PATH, scopes=scopes)
client = gspread.authorize(creds)

try:
    sheet = client.open_by_key(1-B5vl7z1PYtznEQB_23D3tVSIIrc-J7M2BS34Hguw3Q)  # Abre la hoja de cálculo
    print("Conexión a la hoja de cálculo exitosa.")

    # Función para manejar el comando /start
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("¡Hola! Soy tu bot de Telegram y puedo interactuar con tu hoja de cálculo.")
        try:
            worksheet = sheet.sheet1  # Obtener la primera hoja
            cell_value = worksheet.cell(1, 1).value  # Leer la celda A1
            await update.message.reply_text(f"El valor de la celda A1 es: {cell_value}")
        except Exception as e:
            await update.message.reply_text(f"Error al leer la hoja: {str(e)}")

    # Iniciar el bot
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Agrega un manejador para el comando /start
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()

except Exception as e:
    print(f"Error general: {str(e)}")"

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(credentials_path, scopes=scopes)
client = gspread.authorize(creds)

try:
    sheet = client.open_by_key(1-B5vl7z1PYtznEQB_23D3tVSIIrc-J7M2BS34Hguw3Q)  # Abre la hoja de cálculo
    print("Conexión a la hoja de cálculo exitosa.")

    # Ejemplo de función para manejar un comando
    def start(update: Update, context):
        update.message.reply_text("¡Hola! Soy tu bot de Telegram y puedo interactuar con tu hoja de cálculo.")
        try:
           #Ejemplo de como leer datos
           worksheet = sheet.sheet1 #Obtener la primera hoja
           cell_value = worksheet.cell(1,1).value #Leer la celda A1
           update.message.reply_text(f"El valor de la celda A1 es: {cell_value}")
        except Exception as e:
           update.message.reply_text(f"Error al leer la hoja: {e}")

    # Iniciar el bot
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Agrega un manejador para el comando /start
    start_handler = CommandHandler('start', start)  # Crea un manejador para el comando /start
    application.add_handler(start_handler)  # Agrega el manejador al bot

    application.run_polling(allowed_updates=Update.ALL_TYPES)

except Exception as e:
    print(f"Error: {e}")


