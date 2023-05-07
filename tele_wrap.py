from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# TODO (saif) put in correct token / read config
TELEGRAM_BOT_API_TOKEN = ""

count = 0
async def handle_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    count += 1
    await update.message.reply_text("Response: {}".format(count))

app = ApplicationBuilder().token(TELEGRAM_BOT_API_TOKEN).build()
app.add_handler(CommandHandler("hello", handle_query))
app.run_polling()

