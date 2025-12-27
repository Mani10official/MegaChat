import config
import logging
from telegram import Update
from telegram.ext import CommandHandler, ApplicationBuilder, MessageHandler, filters, ContextTypes

API_TOKEN = config.API_TOKEN

logging.basicConfig(
    filename='sample.log', 
    level=logging.INFO, 
    format='%(asctime)s, %(levelname)s, %(message)s',  
    encoding='utf-8'
)


# handlers

    # start command
async def start(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('سلام ، خوش آمدید🌹')
    
    
# echo function
async def echo(update:Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat_id = update.effective_chat.id
    
    message = update.message.text
    
    logging.info(f'{user.first_name} {chat_id}: {message}')
    
    await update.message.reply_text(message)


def main():
    app = ApplicationBuilder().token(API_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    app.run_polling()

if __name__ == "__main__":
    main()