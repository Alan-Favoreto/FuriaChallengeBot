from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from telegram.constants import ChatAction
from deep_translator import GoogleTranslator
import asyncio


async def traduzir(texto, lang='en'):
    if lang == 'en':
        return GoogleTranslator(source='pt', target='en').translate(texto)
    return texto


async def show_typing(update, context):
    try:
        if hasattr(update, 'message') and update.message:
            chat_id = update.message.chat_id
        elif hasattr(update, 'callback_query') and update.callback_query and update.callback_query.message:
            chat_id = update.callback_query.message.chat_id
        else:
            return

        await context.bot.send_chat_action(
            chat_id=chat_id,
            action=ChatAction.TYPING
        )
        await asyncio.sleep(0.5)
    except Exception as e:
        print(f"Erro em show_typing: {e}")


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_typing(update, context)
    keyboard = [
        [InlineKeyboardButton("Português 🇧🇷", callback_data='pt')],
        [InlineKeyboardButton("English 🇺🇸", callback_data='en')]
    ]
    mensagem = ("🇧🇷 Selecione seu idioma:\n\n🇺🇸 Select your language:")
    await update.message.reply_text(mensagem, reply_markup=InlineKeyboardMarkup(keyboard))


async def language_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_typing(update, context)
    query = update.callback_query
    await query.answer()
    lang = query.data
    context.user_data['lang'] = lang

    base_msg = "Olá, eu sou o bot da Furia E-Sports\nVocê selecionou: Português 🇧🇷" if lang == 'pt' else "Hello, I'm the Furia E-Sports bot\nYou selected: English 🇺🇸"
    await query.edit_message_text(await traduzir(base_msg, lang))
    await show_main_menu(query, context)


async def show_main_menu(query, context):
    await show_typing(query, context)
    lang = context.user_data.get('lang', 'pt')

    curiosities_text = await traduzir("Curiosidades", lang)
    quiz_text = await traduzir("Quiz", lang)
    store_text = await traduzir("Loja", lang)

    buttons = [
        [InlineKeyboardButton(curiosities_text, callback_data='curiosities')],
        [InlineKeyboardButton(quiz_text, callback_data='quiz')],
        [InlineKeyboardButton(store_text, callback_data='store')]
    ]

    prompt = await traduzir("Escolha uma opção:", lang)
    await query.message.reply_text(prompt, reply_markup=InlineKeyboardMarkup(buttons))


async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_typing(update, context)
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get('lang', 'pt')

    if query.data == 'back_to_menu':
        return await show_main_menu(query, context,)

    if query.data == 'curiosities':
        from handlers.curiosities import curiosities_handler
        await curiosities_handler(update, context)
    elif query.data == 'quiz':
        from handlers.quiz import start_quiz
        await start_quiz(update, context)
    elif query.data == 'store':
        from handlers.store import  store_handler
        await store_handler(update, context)