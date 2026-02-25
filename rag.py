# %pip install langgraph langchain-openai langchain-core pypdf unstructured pypdf -U langchain-community -U langchain-openai langchain-yt-dlp

# configurando chatgpt
import getpass
import os
from google.colab import userdata
from langchain.chat_models import init_chat_model
from langchain_core.vectorstores import InMemoryVectorStore

os.environ["OPENAI_API_KEY"] = userdata.get('OPENAI_API_KEY')
llm = init_chat_model("gpt-4o-mini", model_provider="openai")

#selecionando o embedding
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

vector_store = InMemoryVectorStore(embeddings)

from langchain_yt_dlp.youtube_loader import YoutubeLoaderDL

# Basic transcript loading
loader = YoutubeLoaderDL.from_youtube_url(
    "https://github.com/mobizt/Firebase-ESP32.git", add_video_info=True
)

docs1 = loader.load()

docs1[0].metadata

#criando uma base de cohecimento
import bs4
from langchain_community.document_loaders import PyPDFLoader

file_path = "/content/PAULO DENIZAR ARAÚJO SOUSA - TCC - MATEMÁTICA.pdf"
loader = PyPDFLoader(file_path)

docs2 = loader.load()

docs2[0]

docs2 = loader.load()

docs2[0].metadata

docs_final =  docs1 + docs2

#fazendo o splitting dos documentos
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter (
    chunk_size=1000,  # chunk size (characters)
    chunk_overlap=200,  # chunk overlap (characters)
    add_start_index=True,  # track index in original document
)
all_splits = text_splitter.split_documents(docs_final)

print(f"Split pdf into {len(all_splits)} sub-documents.")

all_splits[0]

#guardando os dados em um banco de dados
document_ids = vector_store.add_documents(documents=all_splits)

print(document_ids[:3])

## recuperando informações para ajudar o chatgpt
from langchain import hub

prompt = hub.pull("rlm/rag-prompt")

example_messages = prompt.invoke(
    {"context": "(context goes here)", "question": "(question goes here)"}
).to_messages()

assert len(example_messages) == 1
print(example_messages[0].content)

# Como atualizar o prompt:

prompt.messages[0].prompt.template = '''You are a virtual assistant who will answer questions on a test about Boolean logic and solar energy. If the answer is not in the context, say that the information was not found.
Question: {question}
Context: {context}
Answer:'''

prompt

from langchain_core.documents import Document
from typing_extensions import List, TypedDict


class State(TypedDict):
    question: str
    context: List[Document]
    answer: str

def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"])
    return {"context": retrieved_docs}


def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response.content}

#definindo o fluxo de trabalho
from langgraph.graph import START, StateGraph

graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()

result = graph.invoke({"question": "Como os conceitos de álgebra booleana podem ser aplicados na construção de circuitos digitais?"})

print(f'Context: {result["context"]}\n\n')
print(f'Answer: {result["answer"]}')

result["context"]
