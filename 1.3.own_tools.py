"""
uv add tavily-python
uv run 1.3.own_tools.py
"""
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
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

agent = Agent(
  model=Groq(id="llama-3.3-70b-versatile"),
  tools=[
    TavilyTools(),
    celsius_to_fh,
  ],
  debug_mode=False
)

agent.print_response("""
Use suas ferramentas para pesquisar a temperatura de hoje em Venda Nova do Imigrante e convertê-la para Fahrenheit.

INSTRUÇÕES IMPORTANTES:
1. Primeiro, use a ferramenta de pesquisa para encontrar a temperatura atual
2. Extraia o valor numérico da temperatura dos resultados (ex: se encontrar "25°C", use 25)
3. Use a função celsius_to_fh com o valor numérico extraído (não use strings como "temperatura_encontrada")
4. Apresente o resultado final em Fahrenheit

Exemplo correto: celsius_to_fh(25) - onde 25 é o valor numérico da temperatura
Exemplo incorreto: celsius_to_fh("temperatura_encontrada") - não use strings
""")

