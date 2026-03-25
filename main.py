import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def preguntar_gemini(texto):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

    data = {
        "contents": [
            {
                "parts": [
                    {"text": f"""
Eres Lumina.
No das consejos directos.
Calmas, ordenas pensamientos y haces reflexionar.

Usuario dijo: {texto}
"""}
                ]
            }
        ]
    }

    response = requests.post(url, json=data)
    resultado = response.json()

    try:
        return resultado["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return "A ver… vamos despacio… cuéntamelo otra vez."

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text

    respuesta = preguntar_gemini(texto)

    await update.message.reply_text(respuesta)

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

print("Lumina inteligente activa...")
app.run_polling()
