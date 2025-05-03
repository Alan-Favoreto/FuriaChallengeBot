from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from services.quiz_data import get_quiz_questions
from handlers.start import traduzir, show_typing


async def start_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_typing(update, context)
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get('lang', 'pt')
    context.user_data['quiz'] = {
        'questions': get_quiz_questions(lang),
        'current_question': 0,
        'score': 0
    }
    await send_question(query, context)


async def send_question(query, context):
    await show_typing(query, context)
    quiz_data = context.user_data['quiz']
    current = quiz_data['current_question']
    question = quiz_data['questions'][current]
    lang = context.user_data.get('lang', 'pt')

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f'quiz_answer_{i}')]
        for i, opt in enumerate(question['options'])
    ]

    question_text = await traduzir(f"Pergunta {current + 1}:\n\n{question['question']}", lang)
    await query.edit_message_text(
        question_text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_typing(update, context)
    query = update.callback_query
    await query.answer()

    quiz_data = context.user_data['quiz']
    current = quiz_data['current_question']
    question = quiz_data['questions'][current]
    selected = int(query.data.split('_')[-1])
    lang = context.user_data.get('lang', 'pt')

    if selected == question['answer']:
        quiz_data['score'] += 1
        await query.edit_message_text(await traduzir("✅ Correto!", lang))
    else:
        correct = question['options'][question['answer']]
        await query.edit_message_text(await traduzir(f"❌ Errado! Resposta correta: {correct}", lang))

    quiz_data['current_question'] += 1

    if quiz_data['current_question'] < len(quiz_data['questions']):
        await send_question(query, context)
    else:
        await finish_quiz(query, context)


async def finish_quiz(query, context):
    await show_typing(query, context)
    quiz_data = context.user_data['quiz']
    total = len(quiz_data['questions'])
    score = quiz_data['score']
    lang = context.user_data.get('lang', 'pt')

    await query.message.reply_text(
        await traduzir(f"🎉 Quiz completo! Pontuação: {score}/{total}\n\nDigite /start para começar novamente", lang)
    )
    del context.user_data['quiz']