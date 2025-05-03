from deep_translator import GoogleTranslator

QUIZ_QUESTIONS = [
    {
        'question_pt': 'Em que ano a FURIA E-Sports foi fundada?',
        'options': ['2016', '2017', '2018', '2019'],
        'answer': 1
    },
    {
        'question_pt': 'Quem é o atual capitão da equipe principal de CS:GO?',
        'options': ['arT', 'KSCERATO', 'yuurih', 'saffee'],
        'answer': 0
    },
    {
        'question_pt': 'Quantos títulos internacionais a FURIA venceu em 2022?',
        'options': ['1', '2', '3', '4'],
        'answer': 2
    }
]

def get_quiz_questions(lang='pt'):
    questions = []
    for q in QUIZ_QUESTIONS:
        question = {
            'question': q['question_pt'] if lang == 'pt' else GoogleTranslator(source='pt', target='en').translate(q['question_pt']),
            'options': q['options'],
            'answer': q['answer']
        }
        questions.append(question)
    return questions