import os
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.tracers.langchain import LangChainTracer

from dotenv import load_dotenv
load_dotenv() # take env variable from .env

app = FastAPI()

class Urls(BaseModel):
    urls: list[str]

class Question(BaseModel):
    query: str

llm = ChatOpenAI(temperature=0.8, max_tokens=500)
embeddings = OpenAIEmbeddings()
file_path= "vector_index"

@app.post("/process_urls")
def process_urls(payload: Urls):
    # Load data
    loader = UnstructuredURLLoader(urls=payload.urls)
    data = loader.load()

    # Split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n','\n','.',','],
        chunk_size= 1000
    )
    docs= text_splitter.split_documents(data)

    # Create embeddings and save it to FAISS index
    vectorindex_openai = FAISS.from_documents(docs,embeddings)

    # Save vector database
    vectorindex_openai.save_local(file_path)

    return {"body":"embedding created and saved to FAISS index",
            "num_urls":len(payload.urls),
            "num_chunks": len(docs)}

@app.post("/ask")
def ask(payload: Question):
    query = payload.query.strip()
    if not query:
        return {"error": "Empty query"}
    if not os.path.exists(file_path):
        return {"error": "FAISS index not found. Run /process_urls first"}

    #Load vector index
    vector_index = FAISS.load_local(
        file_path,
        embeddings,
        allow_dangerous_deserialization=True
    )
    retriever = vector_index.as_retriever()

    prompt= ChatPromptTemplate.from_template(
            """Use the context below to answer the question.
            If you don't know, say you don't know.
    
            Context:
            {context}
    
            Question: {question}
                
            Answer (with sources in hyperlink):
            """
    )

    chain = (
            {
            "context": retriever,
            "question": lambda x: x
            }
            |prompt
            | llm
            | StrOutputParser()
    )

    # LangSmith tracer
    tracer = LangChainTracer(project_name="my-LLM-Analyst-project")

    result = chain.invoke(query, config={'callbacks':[tracer]})

    return {"answer": result}




