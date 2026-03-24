from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

import os
from gtts import gTTS

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()

    if "lumina" in texto:
        respuesta = "Te escucho... sueltalo sin filtro."
    elif "piensa como" in texto:
        respuesta = "Ok... si lo ves desde otra perspectiva... ¿que ya sabes que estas evitando ver?"
    else:
        respuesta = f"A ver... te escucho diciendo: {texto}. No te me aceleres... ¿que parte de eso es la que mas te pesa?"

    # 🔥 convertir a voz
    tts = gTTS(respuesta, lang='es')
    tts.save("voz.ogg")

    # 🔥 enviar audio
    with open("voz.ogg", "rb") as audio:
        await update.message.reply_voice(audio)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, responder))

print("Lumina con voz activa...")

app.run_polling()
