# É um adaptador para o modelo OpenAI
# from agno.models.openai import OpenAIChat

# É um adaptador para o Groq
from agno.models.groq import Groq

# É uma mensagem que pode ser enviada para o modelo
from agno.models.message import Message

import json

from dotenv import load_dotenv
load_dotenv()

model = Groq(id="llama-3.3-70b-versatile")

msg = Message(
  role="user",
  content=[{"type": "text", "text": "Olá, meu nome é Bruno"}]
)

response = model.invoke([msg])

print('========================================')
print(json.dumps(response.__dict__, indent=4, ensure_ascii=False, default=str))
print('========================================')
print(response.choices[0].message.content)
print('========================================')

