def tool_calculator(expression):
    return eval(expression)

def tool_search(query):
    return f"Search Result for {query}: The answer is 42."

class Agent:
    def __init__(self, name):
        self.name = name

    def run(self, task):
        print(f"[{self.name}] Received task: {task}")

        # Simulation of LLM reasoning loop
        if "calculate" in task:
            expression = task.split("calculate ")[1]
            print(f"[{self.name}] Decided to use Calculator Tool.")
            result = tool_calculator(expression)
            print(f"[{self.name}] Tool Output: {result}")
        elif "search" in task:
            query = task.split("search ")[1]
            print(f"[{self.name}] Decided to use Search Tool.")
            result = tool_search(query)
            print(f"[{self.name}] Tool Output: {result}")
        else:
            print(f"[{self.name}] I don't know how to do that.")

def run_agent_simulation():
    print("--- Agent Simulation ---")
    agent = Agent("RoboHelper")

    agent.run("Please calculate 2 + 2 * 10")
    print("-" * 20)
    agent.run("Please search meaning of life")

if __name__ == "__main__":
    run_agent_simulation()
