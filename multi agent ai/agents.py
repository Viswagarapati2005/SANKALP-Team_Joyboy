# agents.py
from ollama_client import query_ollama

# ---------------------------
# Individual specialized agents
# ---------------------------

class ElicitationAgent:
    def run(self, user_input: str) -> str:
        return query_ollama(
            f"Extract the core requirement clearly and concisely from the following user input:\n\n{user_input}",
            model="gemma:2b"
        )

class AnalysisAgent:
    def run(self, text: str) -> str:
        return query_ollama(
            f"Analyze the following requirement in detail. Break down scope, challenges, and feasibility:\n\n{text}",
            model="gemma:2b"
        )

class DeveloperAgent:
    def run(self, text: str) -> str:
        return query_ollama(
            f"Generate a minimal but working Python implementation for this requirement:\n\n{text}",
            model="gemma:2b"
        )

class ValidationAgent:
    def run(self, text: str) -> str:
        return query_ollama(
            f"Check feasibility, correctness, and potential issues of this proposed solution:\n\n{text}",
            model="gemma:2b"
        )

class RefinementAgent:
    def run(self, text: str) -> str:
        return query_ollama(
            f"Refine, optimize, and improve clarity of this solution while keeping it simple:\n\n{text}",
            model="gemma:2b"
        )

# ---------------------------
# Helper to fetch all agents
# ---------------------------
def get_agents():
    return [
        ElicitationAgent(),
        AnalysisAgent(),
        DeveloperAgent(),
        ValidationAgent(),
        RefinementAgent()
    ]
