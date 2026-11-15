import os
import httpx


async def ask_llm(messages):
    """Envia o histórico (lista de {'role', 'content'}) ao Ollama e devolve a resposta."""
    url = os.getenv('OLLAMA_URL', 'http://localhost:11434')
    async with httpx.AsyncClient(timeout=120) as client:
        r = await client.post(f'{url}/api/chat', json={
            'model': os.getenv('OLLAMA_MODEL', 'qwen3:8b'),
            'messages': messages,
            'stream': False,
            'think': False,  # qwen3 "pensa" por padrão: lento demais para chat
        })
        r.raise_for_status()
        return r.json()['message']['content'].strip()


if __name__ == '__main__':
    import asyncio
    resposta = asyncio.run(ask_llm([{'role': 'user', 'content': 'Responda apenas: ok'}]))
    assert resposta, 'Ollama devolveu resposta vazia'
    print(resposta)
