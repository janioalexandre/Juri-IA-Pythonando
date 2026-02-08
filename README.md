# Juri.IA da Pythonando

Sistema web inteligente para assistência jurídica com IA, combinando análise automatizada de documentos, consulta processual e assistente virtual.

## 📋 Sobre o Projeto

Juri.IA é uma plataforma completa que utiliza Inteligência Artificial para auxiliar profissionais do direito em suas atividades diárias. O sistema oferece desde consulta de processos judiciais até análise detalhada de documentos jurídicos, além de um assistente virtual para atendimento e agendamento.

## ✨ Principais Funcionalidades

### 🤖 Assistente Jurídico Virtual (Chat IA)
- Chat interativo com streaming de respostas em tempo real
- Sistema RAG (Retrieval Augmented Generation) para busca em base de conhecimento
- Memória de conversação para contexto persistente
- Integração com base vetorial para respostas fundamentadas
- Referências e fontes das informações utilizadas

### 📊 Análise Automatizada de Jurisprudência
- Análise completa de documentos jurídicos (petições, contratos, recursos, contestações)
- **Índice de Risco (0-100)**: Avaliação automática do risco de indeferimento ou perda processual
- **Classificação de Risco**: Baixo, Médio, Alto ou Crítico
- **Detecção de Problemas**:
  - Erros de coerência entre fatos narrados e pedidos
  - Riscos jurídicos e fragilidades argumentativas
  - Problemas de formatação e estrutura
  - Red flags críticas que podem levar a indeferimento imediato
- Sugestões práticas e acionáveis para correção
- Tempo de processamento monitorado

### 🔍 Consulta de Processos Judiciais
- Integração com API DataJud do CNJ (Conselho Nacional de Justiça)
- Busca de processos em tribunais brasileiros (TST, TSE, STJ, STM, TRFs, TJs)
- Acesso a informações de movimentações, decisões e partes processuais
- Consulta através do número do processo no formato CNJ

### 📅 Assistente de Secretaria Virtual
- Atendimento automatizado ao cliente
- Agendamento inteligente via Google Calendar
- Horário comercial configurável (13h-18h)
- Verificação automática de disponibilidade
- Acesso a base de conhecimento sobre produtos e serviços
- Foco em conversão e agendamento de reuniões

### 👥 Gestão de Clientes e Documentos
- Cadastro de clientes (PF e PJ)
- Upload e organização de documentos jurídicos
- Suporte a múltiplos tipos: Contratos, Petições, Contestações, Recursos
- Editor Markdown integrado para conteúdo dos documentos
- Histórico de análises e interações

### 💬 Integração WhatsApp
- Wrapper para Evolution API
- Envio automatizado de mensagens
- Notificações e alertas via WhatsApp

## 🛠️ Tecnologias Utilizadas

### Backend & Framework
- **Django 6.0.1**: Framework web principal
- **Python 3.x**: Linguagem de programação
- **Django Q2**: Sistema de filas para processamento assíncrono de tarefas

### Inteligência Artificial & Machine Learning
- **LangChain**: Framework para desenvolvimento de aplicações com LLMs
- **LangChain-OpenAI**: Integração com modelos OpenAI
- **OpenAI GPT-4 e GPT-4.1-mini**: Modelos de linguagem para análise e chat
- **Agno**: Framework para criação de agentes inteligentes

### Banco de Dados Vetorial & RAG
- **LanceDB**: Banco de dados vetorial para embeddings
- **OpenAI Embedder**: Geração de embeddings para busca semântica
- **SQLite**: Banco de dados relacional para memória e persistência

### Processamento de Documentos
- **Docling**: Processamento e análise de documentos
- **Docling Core & IBM Models**: Modelos especializados para extração de conteúdo
- **PyPDF e similares**: Manipulação de arquivos PDF

### APIs & Integrações Externas
- **DataJud API (CNJ)**: Consulta de processos judiciais brasileiros
- **Google Calendar API**: Agendamento de reuniões
- **Evolution API**: Integração com WhatsApp
- **Google Auth & OAuth2**: Autenticação para serviços Google

### Processamento de Linguagem Natural
- **Beautiful Soup 4**: Parsing de HTML
- **lxml**: Processamento XML/HTML otimizado

### Interface & Frontend
- **Martor**: Editor Markdown rico para Django
- **Markdown-it**: Processamento de Markdown
- **Bleach**: Sanitização de HTML

### Computação & Performance
- **NVIDIA CUDA**: Aceleração GPU para processamento ML
- **PyTorch & Transformers**: Frameworks de deep learning
- **NumPy & Pandas**: Manipulação de dados científicos
- **OpenCV**: Processamento de imagens

### Utilitários
- **python-dotenv**: Gerenciamento de variáveis de ambiente
- **Requests & HTTPX**: Cliente HTTP para APIs externas
- **Faker**: Geração de dados de teste
- **GitPython**: Integração com Git

## 📂 Estrutura do Projeto

```
juri-ia-pythonando/
├── core/                    # Configurações do Django
├── ia/                      # Módulo principal de IA
│   ├── agents.py           # Agentes JuriAi e SecretariaAI (Agno)
│   ├── agent_langchain.py  # Agente de análise (LangChain)
│   ├── models.py           # Modelos de dados
│   ├── views.py            # Views e lógica de negócio
│   ├── tasks.py            # Tarefas assíncronas
│   └── templates/          # Templates HTML
├── usuarios/               # Gestão de usuários e clientes
│   ├── models.py           # Modelos Cliente e Documentos
│   └── templates/          # Templates de autenticação
├── lancedb/                # Banco de dados vetorial
│   └── documentos.lance/   # Embeddings de documentos
├── media/                  # Arquivos de upload
├── staticfiles/            # Arquivos estáticos
└── templates/              # Templates base

```

## 🚀 Como o Sistema Funciona

### Fluxo de Chat Jurídico
1. Cliente envia pergunta através da interface web
2. Sistema cria registro da pergunta no banco de dados
3. Agente JuriAi processa a pergunta com:
   - Busca na base de conhecimento (RAG)
   - Consulta a API DataJud se necessário
   - Acesso à memória de conversação
4. Resposta é gerada em streaming para o usuário
5. Referências e contextos são salvos para auditoria

### Fluxo de Análise de Jurisprudência
1. Usuário faz upload de documento jurídico
2. Sistema extrai conteúdo do documento
3. Agente JurisprudenciaAI (GPT-4.1-mini) analisa:
   - Coerência argumentativa
   - Riscos jurídicos
   - Problemas de formatação
   - Red flags críticas
4. Sistema calcula índice de risco (0-100)
5. Análise estruturada é salva e apresentada ao usuário
6. Relatório inclui sugestões práticas de correção

### Sistema RAG (Retrieval Augmented Generation)
1. Documentos são processados e convertidos em chunks
2. Embeddings são gerados via OpenAI
3. Vetores são armazenados no LanceDB
4. Na consulta, similaridade semântica recupera contexto relevante
5. Contexto é injetado no prompt do LLM para resposta fundamentada

## ⚙️ Configuração e Instalação

### Pré-requisitos
- Python 3.10+
- Conta OpenAI com API Key
- Credenciais Google Calendar API (opcional)
- CUDA/GPU (opcional, para melhor performance)

### Instalação

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd juri-ia-pythonando

# Crie e ative ambiente virtual
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Configure variáveis de ambiente
# Crie arquivo .env com:
# OPENAI_API_KEY=sua-chave-aqui
# DATAJUD_API_KEY=sua-chave-cnj

# Execute migrações
python manage.py migrate

# Crie superusuário
python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver
```

## 📝 Licença

Projeto desenvolvido para fins educacionais pela Pythonando.

## 🤝 Contribuições

Este é um projeto educacional. Sugestões e melhorias são bem-vindas!

## 📧 Contato

Para mais informações, visite: [Pythonando](https://pythonando.com.br)

