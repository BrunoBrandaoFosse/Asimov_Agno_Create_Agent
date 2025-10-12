from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from dotenv import load_dotenv
load_dotenv()

# LLM usa a documentação docstring para entender o que a tool faz.
def celsius_to_fh(temperatura_celsius: float):
  """
  Converte uma temperatura de Celsius para Fahrenheit.
  
  IMPORTANTE: Este parâmetro deve ser um número (float), não uma string.
  Extraia o valor numérico da temperatura dos resultados da pesquisa antes de chamar esta função.

  Args:
      temperatura_celsius (float): Temperatura em graus Celsius (deve ser um número).

  Returns:
      float: Temperatura convertida para Fahrenheit.
  """
  return (temperatura_celsius * 9/5) + 32

db = SqliteStorage(table_name="agent_session", db_file="tmp/agent.db")

agent = Agent(
  name="Agente do tempo",
  model=OpenAIChat(id="gpt-4.1-mini"),
  tools=[
    TavilyTools(),
    celsius_to_fh,
  ],
  debug_mode=False,
  # ==================================
  # Armazena o estado e o histórico do agente em um banco de dados SQLite
  storage=db,
  # Adiciona histórico as mensagens
  add_history_to_messages=True,
  # Quantas das mensagens anteriores que foram enviadas
  # Basicamente quantas mensagens anteriores ele deve considerar (janela de contexto)
  # Padrão: 3
  num_history_runs=3,
  # ==================================
)

if __name__ == '__main__':
  ask = ''
  while ask != 'x':
    ask = input('Faça sua pergunta: ')
    if ask != 'x':
      agent.print_response(ask)

