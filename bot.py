from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from handlers.start import start_handler, language_handler, menu_handler
from handlers.quiz import start_quiz, handle_answer
from handlers.curiosities import curiosities_handler
from handlers.store import store_handler
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler('start', start_handler))
app.add_handler(CallbackQueryHandler(language_handler, pattern='^(pt|en|ug)$'))
app.add_handler(CallbackQueryHandler(menu_handler, pattern='^(curiosities|quiz|store)$'))
app.add_handler(CallbackQueryHandler(start_quiz, pattern='^start_quiz$'))
app.add_handler(CallbackQueryHandler(handle_answer, pattern='^quiz_answer_'))
app.add_handler(CallbackQueryHandler(curiosities_handler, pattern='^(curiosities|next_curiosity|back_to_menu)$'))
app.add_handler(CallbackQueryHandler(store_handler, pattern='^store$'))

if __name__ == '__main__':
    print("Bot rodando!")
    app.run_polling()