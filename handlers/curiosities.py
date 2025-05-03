from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from handlers.start import traduzir, show_main_menu

CURIOSITIES = [
    "A FURIA foi fundada em 2017 e rapidamente se tornou uma das principais organizações de CS:GO do Brasil",
    "O capitão arT é conhecido por seu estilo agressivo de liderança e plays inovadoras",
    "Em 2022, a FURIA se tornou o primeiro time brasileiro a vencer o Intel Grand Slam",
    "O maior prêmio conquistado pela equipe foi de $500,000 no ESL Pro League Season 13",
    "A equipe principal tem 5 brasileiros: arT, KSCERATO, yuurih, saffee e chelo"
]

async def curiosities_handler(update, context):
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get('lang', 'pt')

    if query.data == 'back_to_menu':
        context.user_data.pop('curiosity_index', None)
        return await show_main_menu(query, context)

    if query.data == 'curiosities':
        context.user_data['curiosity_index'] = 0
    elif query.data == 'next_curiosity':
        if 'curiosity_index' not in context.user_data:
            context.user_data['curiosity_index'] = 0
        else:
            context.user_data['curiosity_index'] += 1

    idx = context.user_data.get('curiosity_index', 0)
    if idx >= len(CURIOSITIES):
        idx = len(CURIOSITIES) - 1
        context.user_data['curiosity_index'] = idx

    next_text = await traduzir("Próxima curiosidade", lang) + " ➡️"
    back_text = await traduzir("Voltar ao menu", lang) + " ↩️"

    keyboard = []
    if idx < len(CURIOSITIES) - 1:
        keyboard.append([InlineKeyboardButton(next_text, callback_data='next_curiosity')])
    keyboard.append([InlineKeyboardButton(back_text, callback_data='back_to_menu')])

    try:
        await query.edit_message_text(
            text=f"🧐 {await traduzir('Curiosidade', lang)} {idx + 1}/{len(CURIOSITIES)}:\n\n{await traduzir(CURIOSITIES[idx], lang)}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    except:
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text=f"🧐 {await traduzir('Curiosidade', lang)} {idx + 1}/{len(CURIOSITIES)}:\n\n{await traduzir(CURIOSITIES[idx], lang)}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )