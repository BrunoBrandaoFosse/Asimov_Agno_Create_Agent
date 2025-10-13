from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from agno.vectordb.chroma import ChromaDb
from dotenv import load_dotenv
load_dotenv()

vector_db = ChromaDb(collection="pdf_agent", path="tmp/chroma_db")

knowledge = PDFKnowledgeBase(
  path='GlobalEVOutlook2025.pdf',
  vector_db=vector_db,
  reader=PDFReader(chunk=True),
)

db = SqliteStorage(table_name="agent_session", db_file="tmp/agent.db")

agent = Agent(
  name="Agente do tempo",
  model=OpenAIChat(id="gpt-4.1-mini"),
  # Armazena o estado e o histórico do agente em um banco de dados SQLite
  storage=db,
  # Adiciona conhecimento ao agente
  knowledge=knowledge,
  # Adiciona histórico as mensagens
  add_history_to_messages=True,
  # Quantas das mensagens anteriores que foram enviadas
  # Basicamente quantas mensagens anteriores ele deve considerar (janela de contexto)
  # Padrão: 3
  num_history_runs=3,
  # Permite que o agente pesquise no conhecimento quando não souber a resposta
  search_knowledge=True,
)

if __name__ == "__main__":
  # Carrega o conhecimento (PDF)
  # Se o conhecimento já foi carregado anteriormente, ele não será recarregado
  # Rodar só na primeira vez ou se o PDF mudar
  knowledge.load(recreate=True)
  ask = ''
  while ask != 'x':
    ask = input('Faça sua pergunta: ')
    if ask != 'x':
      agent.print_response(ask)

