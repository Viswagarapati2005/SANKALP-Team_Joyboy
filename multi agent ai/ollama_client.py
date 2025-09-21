# ollama_client.py
import requests

def query_ollama(prompt: str, model: str = "gemma:2b") -> str:
    """
    Query a local Ollama model.
    """
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt},
            timeout=1000
        )

        # Ollama streams responses. If `response.json()` fails, handle line-streaming.
        try:
            data = response.json()
            return data.get("response", "").strip()
        except Exception:
            text = ""
            for line in response.iter_lines():
                if line:
                    try:
                        part = line.decode("utf-8")
                        if '"response":"' in part:
                            text += part.split('"response":"')[1].split('"')[0]
                    except:
                        continue
            return text.strip()

    except Exception as e:
        return f"❌ Ollama Error: {e}"
