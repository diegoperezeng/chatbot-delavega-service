# Backend Python - ChatBot DeLaVega

Python backend for ChatBot DeLaVega, an advanced chat platform that supports multiple LLM providers.

## Main Features

- **Multiple LLM Providers:**
  - OpenAI (GPT-4, GPT-3.5)
  - Anthropic (Claude 3)
  - Google (Gemini Pro)
  - Llama (HTTP Server)


- **Advanced Features:**
  - Response streaming
  - Conversation memory
  - Function calling (OpenAI)
  - Security settings (Google)
  - Document processing
  - Supabase integration

## Requirements

- Python 3.9+
- pip (Python package manager)
- API keys from desired providers

## Installation

1. Clone the repository:
```bash
git clone https://github.com/diegoperezeng/chatbot-delavega-service.git
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Configure environment variables:
```bash
cp .env.example .env
```

6. Edit the `.env` file with your settings:
```env
# Server Settings
PORT=8000
HOST=0.0.0.0
DEBUG=True

# Secret Key (Generate a strong key)
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Supabase
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key

# Provider API Keys
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_API_KEY=your_google_key
AZURE_API_KEY=your_azure_key
GROQ_API_KEY=your_groq_key
MISTRAL_API_KEY=your_mistral_key
OPENROUTER_API_KEY=your_openrouter_key
```

## Running the Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The server will be available at `http://localhost:8000`

## API Documentation

- **Swagger UI:** `http://localhost:8000/docs`
  - Interactive documentation with examples
  - Test endpoints directly
  - Complete model schemas

- **ReDoc:** `http://localhost:8000/redoc`
  - Cleaner and more organized documentation
  - Better for reading

## Project Structure

```
backend/
├── app/
│   ├── api/
│   │   ├── chat/
│   │   │   ├── anthropic/
│   │   │   │   ├── anthropic_controller.py  # Rotas e endpoints FastAPI
│   │   │   │   ├── anthropic_models.py      # Entidades e enums básicos
│   │   │   │   ├── anthropic_schemas.py     # DTOs e validação
│   │   │   │   └── anthropic_service.py     # Lógica de negócios
│   │   │   ├── google/
│   │   │   │   ├── google_controller.py     # Rotas e endpoints FastAPI
│   │   │   │   ├── google_models.py         # Entidades e enums básicos
│   │   │   │   ├── google_schemas.py        # DTOs e validação
│   │   │   │   └── google_service.py        # Lógica de negócios
│   │   │   ├── llama/
│   │   │   │   ├── llama_controller.py     # Rotas e endpoints FastAPI
│   │   │   │   ├── llama_models.py         # Entidades e enums básicos
│   │   │   │   ├── llama_schemas.py        # DTOs e validação
│   │   │   │   └── llama_service.py        # Lógica de negócios
│   │   │   └── openai/
│   │   │       ├── openai_controller.py    # Rotas e endpoints FastAPI
│   │   │       ├── openai_models.py        # Entidades e enums básicos
│   │   │       ├── openai_schemas.py       # DTOs e validação
│   │   │       └── openai_service.py       # Lógica de negócios
│   │   ├── keys/
│   │   │   └── keys_controller.py
│   │   ├── messages/
│   │   │   └── messages_controller.py
│   │   ├── retrieval/
│   │   │   ├── process/
│   │   │   │   └── process_controller.py
│   │   │   ├── retrieve/
│   │   │   │   └── retrieve_controller.py
│   │   │   └── retrieval_router.py
│   │   └── username/
│   │       └── username_controller.py
│   ├── core/
│   │   ├── llm_providers/
│   │   │   ├── anthropic_manager.py
│   │   │   ├── google_manager.py
│   │   │   ├── llama_manager.py
│   │   │   └── openai_manager.py
│   │   ├── config.py
│   │   ├── llm_factory.py
│   │   ├── llm_manager.py
│   │   └── security.py
│   ├── lib/
│   │   ├── processing.py
│   │   └── embeddings.py
│   ├── schemas/
│   │   ├── chat.py
│   │   ├── keys.py
│   │   ├── messages.py
│   │   └── retrieval.py
│   ├── __init__.py
│   └── main.py
├── tests/
├── .env.example
├── requirements.txt
└── README.md
```

## Main Dependencies

- **Web Framework:**
  - FastAPI 0.109.2
  - Uvicorn 0.27.1

- **LLM Providers:**
  - OpenAI 1.12.0
  - Anthropic 0.18.1
  - Google AI Platform 1.43.0
  - Groq 0.4.2
  - Mistral AI 0.0.12

- **LangChain:**
  - langchain 0.1.9
  - langchain-openai 0.0.8
  - langchain-anthropic 0.0.6
  - langchain-google-genai 0.0.9
  - langchain-mistralai 0.0.5
  - langchain-groq 0.0.1

- **Data Processing:**
  - python-docx 1.1.0
  - numpy 1.26.4
  - nltk 3.8.1
  - markdown 3.5.2
  - chromadb 0.4.22

- **Utilities:**
  - pydantic 2.6.1
  - python-jose 3.3.0
  - passlib 1.7.4
  - httpx 0.26.0
  - tiktoken 0.6.0

## Contributing

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT license - see the [LICENSE](LICENSE) file for details. 
