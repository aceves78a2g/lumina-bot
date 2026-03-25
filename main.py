from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os
import random

TOKEN = os.getenv("TELEGRAM_TOKEN")

respuestas_generales = [
    "A ver... vamos despacio... ¿que es lo que realmente te esta moviendo?",
    "Respira tantito... cuentamelo bien desde el principio...",
    "Eso que dijiste... ya te escuchaste?",
    "No te aceleres... ¿que parte de eso es la que mas te pesa?",
    "A ver... bajale tantito... ¿que esta pasando en realidad?"
]

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()

    if "lumina" in texto:
        respuesta = "Te escucho... sueltalo sin filtro."

    elif "piensa como" in texto:
        respuesta = "Ok... si lo ves desde otra perspectiva... ¿que ya sabes que estas evitando ver?"

    elif "confundido" in texto:
        respuesta = "Cuando te sientes confundido normalmente es porque hay varias opciones... ¿ya las pusiste en orden?"

    elif "ayuda" in texto:
        respuesta = "Claro que te ayudo... pero primero bajale tantito... dime exactamente que esta pasando"

    else:
        respuesta = random.choice(respuestas_generales)

    await update.message.reply_text(respuesta)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, responder))

print("Lumina funcionando inteligente...")
app.run_polling()
