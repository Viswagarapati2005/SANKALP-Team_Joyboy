# agent.py
from ollama_client import query_ollama  # make sure ollama_client.py has query_ollama()

class RefinementAgent:
    def run(self, text: str) -> str:
        prompt = f"""
You are a helpful assistant. Refine the following solution and present it in a **clear, structured format**.

✅ Format Guidelines:
- Use short headings (## Heading).
- Add bullet points for clarity.
- Keep explanations concise and easy to understand.
- End with a short summary.

Here is the text to refine:
{text}
"""
        return query_ollama(prompt, model="gemma:2b")
