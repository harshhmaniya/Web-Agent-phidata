from phi.agent import Agent
from phi.model.ollama import Ollama
from phi.tools.duckduckgo import DuckDuckGo

web_agent = Agent(
    name="Web Agent",
    model=Ollama(id='llama3.2'),
    tools=[DuckDuckGo()],
    description="Searches web and finds relevant information.",
    instructions=["Always include sources in your answers."],
    task="Find information from the web.",
    show_tool_calls=True,
    markdown=True,
    add_chat_history_to_messages=True,
)

web_agent.print_response("Tell me about yourself", stream=True)