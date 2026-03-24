from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8690678791:AAHn5tfW1q6S3ORPZhO4GwakhpvXjnXKF6o"

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()

    if "lumina" in texto:
        await update.message.reply_text("Te escucho… sueltalo sin filtro.")
        return

    if "piensa como" in texto:
        await update.message.reply_text(
            "Ok… si lo ves desde otra perspectiva… ¿que ya sabes que estas evitando ver?"
        )
        return

    await update.message.reply_text(
        f"A ver… te escucho diciendo:\n\n{texto}\n\nNo te me aceleres… ¿que parte de eso es la que mas te pesa?"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

print("🔥 Lumina esta viva...")
app.run_polling()
