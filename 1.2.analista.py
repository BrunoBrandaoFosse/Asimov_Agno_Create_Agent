from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from agno.models.groq import Groq

from dotenv import load_dotenv
load_dotenv()

agent = Agent(
  model=Groq(id="llama-3.3-70b-versatile"),
  tools=[YFinanceTools()],
  instructions="Use tabelas para mostrar a informação final. Não inclua nenhum outro texto."
)

"""
Com stream=True ao invés de esperar a resposta, 
ele vai mostrando a resposta igual ao ChatGPT
"""
agent.print_response("Qual é a cotação atual da Apple?", stream=True)

"""
# Instalar dependência
uv add yfinance

# Executar o agente:
uv run 1.1.analista.py
"""
