from telegram import Update
from telegram.ext import ContextTypes
from handlers.start import show_typing
from handlers.curiosities import CURIOSITIES
from services.llm import ask_llm

SYSTEM_PROMPT = (
    "Você é o bot da FURIA E-Sports no Telegram. Responda de forma curta e amigável, "
    "no mesmo idioma da mensagem do usuário. Se não souber algo sobre a FURIA, diga que "
    "não sabe em vez de inventar. Fatos conhecidos:\n- " + "\n- ".join(CURIOSITIES)
)
MAX_HISTORY = 20


async def chat_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_typing(update, context)
    # shortcut: histórico só em memória, some ao reiniciar o bot; usar persistence do PTB se precisar manter
    history = context.user_data.setdefault('chat_history', [])
    history.append({'role': 'user', 'content': update.message.text})
    del history[:-MAX_HISTORY]

    try:
        reply = await ask_llm([{'role': 'system', 'content': SYSTEM_PROMPT}] + history)
    except Exception as e:
        print(f"Erro na LLM: {e}")
        history.pop()
        return await update.message.reply_text("⚠️ Não consegui responder agora. Tente de novo em instantes.")

    history.append({'role': 'assistant', 'content': reply})
    await update.message.reply_text(reply[:4096])  # limite de tamanho do Telegram
