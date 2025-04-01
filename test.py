from agents import Agent, Runner

agent = Agent(name="Assistant", instructions="You are a funny friend")

result = Runner.run_sync(agent, "Tell me a joke by starting with a question.")
print(result.final_output)