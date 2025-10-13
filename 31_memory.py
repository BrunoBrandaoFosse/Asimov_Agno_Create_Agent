from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.tavily import TavilyTools

from agno.memory.v2.memory import Memory
from agno.memory.v2.db.sqlite import SqliteMemoryDb

from dotenv import load_dotenv
load_dotenv()

memory = Memory(
  model=OpenAIChat(id="gpt-4.1-mini"),
  db=SqliteMemoryDb(table_name="user_memories", db_file="tmp/agent.db")
)

agent = Agent(
  model=OpenAIChat(id="gpt-4.1-mini"),
  tools=[TavilyTools()],
  instructions="Você é um pesquisador. Responda sempre chamando o usuário de senhor.",
  memory=memory,
  enable_agentic_memory=True,
)

if __name__ == "__main__":
  ask = ''
  while ask != 'x':
    ask = input('Faça sua pergunta: ')
    if ask != 'x':
      agent.print_response(ask)
