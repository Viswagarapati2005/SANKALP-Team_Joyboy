from agents import get_agents

def run_pipeline(user_input):
    agents = get_agents()
    text = user_input

    for agent in agents:
        text = agent.run(text)

    return text   # ✅ Only the final answer
