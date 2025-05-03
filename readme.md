# Documentação do Bot da FURIA E-Sports

## Visão Geral

Este é um bot para Telegram desenvolvido para a FURIA E-Sports, oferecendo funcionalidades como:
- Seleção de idioma (Português/Inglês)
- Quiz sobre a organização
- Curiosidades sobre a equipe
- Loja oficial com produtos

## Estrutura de Arquivos

### bot.py
Arquivo principal que configura e inicia o bot. Responsável por:
- Carregar variáveis de ambiente
- Registrar handlers para comandos e callbacks
- Iniciar o polling do bot

### lang.py
Contém mensagens traduzidas para o sistema de quiz, com suporte a:
- Português (pt)
- Inglês (en)

### quiz_data.py
Armazena as perguntas do quiz e fornece tradução automática para inglês.

### curiosities.py
Gerencia as curiosidades sobre a FURIA E-Sports, incluindo:
- Navegação entre curiosidades
- Tradução automática
- Controle de índice atual

### quiz.py
Lógica completa do sistema de quiz, incluindo:
- Inicialização do quiz
- Controle de perguntas/respostas
- Cálculo de pontuação
- Feedback imediato

### start.py
Manipuladores principais do bot:
- Seleção de idioma
- Menu principal
- Funções auxiliares (tradução, indicador de digitação)

### store.py
Integração com a loja oficial da FURIA, mostrando:
- Produtos em destaque
- Link para loja
- Imagem do produto

## Configuração

1. Crie um arquivo `.env` com:
   ```
   TELEGRAM_TOKEN=seu_token_aqui
   ```

2. Instale as dependências:
   ```bash
   pip install python-telegram-bot deep-translator python-dotenv
   ```

3. Execute o bot:
   ```bash
   python bot.py
   ```

## Fluxo Principal

1. Usuário inicia com `/start`
2. Seleciona idioma (pt/en)
3. Acessa menu com opções:
   - Curiosidades
   - Quiz
   - Loja

## Melhorias Futuras

- Adicionar mais perguntas ao quiz
- Expandir sistema de curiosidades
- Integração mais profunda com a loja
- Suporte a mais idiomas

## Dependências

- `python-telegram-bot` - Framework do bot Telegram
- `deep-translator` - Tradução de textos
- `python-dotenv` - Gerenciamento de variáveis de ambiente

## Observações

O bot foi desenvolvido para ser extensível, permitindo fácil adição de novas funcionalidades e traduções.