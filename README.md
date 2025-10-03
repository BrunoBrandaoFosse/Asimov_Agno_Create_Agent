# Criando Agente com Agno

## Processo de criação do projeto

```bash
# No Agno 2.0, o projeto é instalado com pip

python3 -m venv ~/.venvs/agno
source ~/.venvs/agno/bin/activate

pip install -U agno

# =============================

# Instala o "uv"
python3 -m pip install -U uv

# Inicia o projeto
uv init

# Cria o ambiente virtual
uv venv

# Executa o ambiente virtual
source .venv/bin/activate

# Instala o Agno
uv add agno

# Lista os pacotes instalados
uv pip list

# Variáveis de ambiente (instalar pacote)
uv add python-dotenv
```
