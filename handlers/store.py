from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from handlers.start import traduzir

async def store_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get('lang', 'pt')

    product = {
        'name': "SacoChila FURIA Preta",
        'image_url': "https://furiagg.fbitsstatic.net/img/p/sacochila-furia-preta-150267/337499-1.jpg?w=1280&h=1280&v=202504101318",
        'product_url': "https://www.furia.gg/produto/sacochila-furia-preta-150267"
    }

    caption = f"*{product['name']}*"

    keyboard = [
        [InlineKeyboardButton(
            await traduzir("🛍️ Visitar Loja Oficial", lang),
            url=product['product_url']
        )],
        [InlineKeyboardButton(
            await traduzir("🔙 Voltar", lang),
            callback_data='back_to_menu'
        )]
    ]

    await context.bot.send_photo(
        chat_id=query.message.chat_id,
        photo=product['image_url'],
        caption=caption,
        parse_mode='Markdown',
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

    await query.message.delete()