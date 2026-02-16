from langchain_community.document_loaders import (
    DirectoryLoader,
    UnstructuredPDFLoader,
    TextLoader,
    CSVLoader,
    WebBaseLoader
)

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

#1st step
pdf_loader = DirectoryLoader(
    path="./data",
    glob="**/*.pdf",
    loader_cls=UnstructuredPDFLoader
)

text_loader = DirectoryLoader(
    path="./data",
    glob="**/*.txt",
    loader_cls=TextLoader
)

csv_loader = DirectoryLoader(
    path="./data",
    glob="**/*.csv",
    loader_cls=CSVLoader
)

from langchain_community.document_loaders import WebBaseLoader
url="https://www.python.org"
loader= WebBaseLoader (url)
docs =loader.load()
print(docs) 

#2nd step

# 2nd step - Split documents
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=3000,
    chunk_overlap=200
)

split_docs = text_splitter.split_documents(docs)


# 3rd step - Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 4th step - Create vector store
vector_store = Chroma.from_documents(
    documents=split_docs,
    embedding=embedding_model,
    persist_directory="./chroma_db",
    collection_name="fresh_session"
)

print("Vector store created successfully!")
