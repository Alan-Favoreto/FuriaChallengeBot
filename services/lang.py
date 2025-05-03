MESSAGES = {
    'pt': {
        'welcome': "Olá, eu sou o bot da Furia E-Sports",
        'select_language': "Selecione seu idioma:",
        'menu_prompt': "Escolha uma opção:",
        'curiosities': "Curiosidades",
        'quiz': "Quiz", 
        'store': "Loja",
        'next_curiosity': "Próxima curiosidade ➡️",
        'back': "Voltar ↩️"
    },
    'en': {
        'welcome': "Hello, I'm the Furia E-Sports bot",
        'select_language': "Select your language:",
        'menu_prompt': "Choose an option:",
        'curiosities': "Curiosities",
        'quiz': "Quiz",
        'store': "Store",
        'next_curiosity': "Next curiosity ➡️",
        'back': "Back ↩️"
    }
}

def get_message(lang, key):
    return MESSAGES.get(lang, {}).get(key, key)