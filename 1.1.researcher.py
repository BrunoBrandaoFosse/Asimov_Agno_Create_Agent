from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq

from dotenv import load_dotenv
load_dotenv()

agent = Agent(
  model=Groq(id="llama-3.3-70b-versatile"),
  tools=[TavilyTools()],
  debug_mode=True
)

agent.print_response("Use suas ferramentas para pesquisar a temperatura de hoje em Venda Nova do Imigrante")

"""
# Instalar dependência
uv add tavily-python

# Executar o agente:
uv run 1.1.researcher.py
"""
