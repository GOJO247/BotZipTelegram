import gspread
from google.oauth2.service_account import Credentials
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Ruta al archivo JSON de credenciales
CREDENTIALS_PATH = 'json.json'

# ID de la hoja de cálculo
SPREADSHEET_ID = '1-B5vl7z1PYtznEQB_23D3tVSIIrc-J7M2BS34Hguw3Q'

# Token del bot de Telegram
BOT_TOKEN = '7501411396:AAFXv_unSqYDi9i_8ni85rOMHDsC93Xzbxw'

# Autenticación con Google Sheets
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(CREDENTIALS_PATH, scopes=scopes)
client = gspread.authorize(creds)

try:
    sheet = client.open_by_key(SPREADSHEET_ID)  # Abre la hoja de cálculo
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
    print(f"Error general: {str(e)}")