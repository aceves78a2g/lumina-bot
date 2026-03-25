from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from gtts import gTTS
import os

TOKEN = "TU_TOKEN_AQUI"

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()

    # 🔥 lógica simple
    if "confundido" in texto:
        respuesta = "Cuando te sientes confundido es porque hay varias opciones... vamos despacio."
    elif "no se" in texto or "no sé" in texto:
        respuesta = "Ok... si no sabes, entonces vamos a bajarle tantito... ¿qué es lo primero que te viene a la cabeza?"
    else:
        respuesta = "A ver... vamos despacio... cuéntamelo otra vez."

    # 🔊 convertir a voz
    tts = gTTS(respuesta, lang='es')
    archivo = "voz.mp3"
    tts.save(archivo)

    # 🎤 enviar como voz
    await update.message.reply_voice(voice=open(archivo, 'rb'))

    # borrar archivo
    os.remove(archivo)


app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

print("Lumina está viva...")
app.run_polling()
