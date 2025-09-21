# query_ollama.py
import requests

def query_ollama(prompt: str, model: str = "mistral") -> str:
    """
    Query a local Ollama model.
    Args:
        prompt (str): Input text to send to Ollama
        model (str): Model name (default = mistral)
    Returns:
        str: Model's response text
    """
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt},
            stream=True,
            timeout=60
        )
        response.raise_for_status()

        # Ollama streams JSON lines, so collect them
        output = ""
        for line in response.iter_lines():
            if line:
                try:
                    data = line.decode("utf-8")
                    if data.startswith("{"):
                        import json
                        j = json.loads(data)
                        output += j.get("response", "")
                except Exception:
                    continue

        return output.strip()

    except Exception as e:
        return f"❌ Ollama Error: {e}"
