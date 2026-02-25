# 🧠 RAG Pipeline com LangChain + LangGraph

Implementação de um sistema de Retrieval-Augmented Generation (RAG) utilizando LangChain, LangGraph e OpenAI, integrando múltiplas fontes de conhecimento (PDF e conteúdo externo) para geração de respostas contextualizadas e fundamentadas.

---

## 🚀 Visão Geral

Este projeto implementa um pipeline completo de RAG capaz de:

- Ingerir documentos de diferentes fontes
- Dividir o conteúdo em chunks estratégicos
- Gerar embeddings semânticos
- Armazenar em banco vetorial
- Recuperar trechos relevantes via similaridade
- Injetar contexto no prompt
- Gerar respostas fundamentadas usando LLM

A orquestração do fluxo foi realizada com **LangGraph**, organizando o sistema em etapas modulares de recuperação e geração.

---

## 🏗️ Arquitetura do Sistema

O pipeline segue as seguintes etapas:

### 1️⃣ Ingestão de Dados

Fontes utilizadas:

- 📄 PDF (TCC sobre Matemática / Álgebra Booleana)
- 📦 Conteúdo externo carregado via loader

Ferramentas:
- `PyPDFLoader`
- `YoutubeLoaderDL`
- `langchain_community.document_loaders`

---

### 2️⃣ Chunking

Utilização de:

- `RecursiveCharacterTextSplitter`
- `chunk_size = 1000`
- `chunk_overlap = 200`

Objetivo:
- Preservar contexto semântico
- Reduzir perda de informação
- Melhorar precisão da busca vetorial

---

### 3️⃣ Vetorização

- Modelo de embeddings: `text-embedding-ada-002`
- Banco vetorial: `InMemoryVectorStore`

Cada chunk é transformado em embedding e armazenado para posterior busca por similaridade semântica.

---

### 4️⃣ Recuperação (Retrieval)

```python
def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"])
    return {"context": retrieved_docs}
