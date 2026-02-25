# 🧠 RAG System – Retrieval-Augmented Generation

Implementação personalizada de um sistema de Retrieval-Augmented Generation (RAG), capaz de integrar múltiplas fontes de conhecimento e gerar respostas contextualizadas com base em documentos externos.

---

## 🚀 Sobre o Projeto

Este projeto implementa um pipeline de RAG que combina:

- Busca semântica em documentos
- Banco de vetores (vector database)
- Modelo de linguagem (LLM)
- Geração de respostas contextualizadas

A proposta foi personalizar uma base inicial fornecida em aula e expandir a arquitetura para integrar diferentes tipos de fontes de conhecimento.

---

## 📚 Fontes Utilizadas

O sistema foi configurado para processar e consultar:

- 📄 PDF sobre Álgebra Booleana  
- 🎥 Vídeo do YouTube sobre Energia Solar  

Os conteúdos são convertidos em texto, divididos em trechos menores (chunking) e armazenados em um banco vetorial.

---

## ⚙️ Como Funciona

1. **Ingestão de Dados**
   - Extração de texto do PDF
   - Transcrição do vídeo do YouTube
   - Divisão do conteúdo em chunks

2. **Vetorização**
   - Conversão dos trechos em embeddings
   - Armazenamento em banco de vetores

3. **Consulta**
   - O usuário faz uma pergunta
   - O sistema busca os trechos semanticamente mais relevantes
   - Os trechos são enviados junto ao prompt para o modelo de linguagem

4. **Geração da Resposta**
   - O LLM gera uma resposta baseada no contexto recuperado
   - Redução de alucinações
   - Respostas mais precisas e fundamentadas

---

## 🧠 Conceitos Aplicados

- Retrieval-Augmented Generation (RAG)
- Embeddings
- Busca semântica
- Engenharia de Prompt
- Chunking Strategy
- Context Injection
- Redução de alucinação em LLMs

---

## 🛠️ Tecnologias Utilizadas

- Python
- Biblioteca de embeddings
- Banco de vetores
- API de modelo de linguagem
- Processamento de texto
- Transcrição de vídeo

---

## 🎯 Objetivo do Projeto

Explorar como a personalização de um pipeline RAG pode:

- Melhorar a precisão de respostas
- Integrar diferentes fontes de conhecimento
- Criar sistemas de IA mais confiáveis
- Aplicar conceitos avançados de NLP na prática

---

## 🔎 Aprendizados

Mesmo partindo de uma base fornecida, a personalização da arquitetura, da estratégia de chunking e do fluxo de consulta foi fundamental para:

- Melhorar a qualidade das respostas
- Entender o funcionamento interno de sistemas baseados em LLM
- Desenvolver visão crítica sobre limitações e melhorias possíveis

---

## ▶️ Como Executar

```bash
# Clone o repositório
git clone <url-do-repositorio>

# Instale as dependências
pip install -r requirements.txt

# Execute o projeto
python main.py
