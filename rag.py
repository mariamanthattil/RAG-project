from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv

import os

# ✅ LOAD ENV
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY missing in .env")

# ✅ LLM
llm = ChatGroq(
    model='llama-3.1-8b-instant',
    temperature=0.3
)

vectorstore = None
retriever = None

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCUMENT_PATH = os.path.join(BASE_DIR, "documents")


# -------------------------------
def build_vectorstore():
    global retriever, vectorstore

    print("🔄 Building Vector DB...")

    pdf_loader = DirectoryLoader(DOCUMENT_PATH, glob="*.pdf", loader_cls=PyPDFLoader)
    txt_loader = DirectoryLoader(DOCUMENT_PATH, glob="*.txt", loader_cls=TextLoader)

    pdf_docs = list(pdf_loader.lazy_load())
    txt_docs = list(txt_loader.lazy_load())

    docs = pdf_docs + txt_docs

    print("📄 Docs found:", len(docs))

    if not docs:
        retriever = None
        return

    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma.from_documents(chunks, embeddings)

    retriever = vectorstore.as_retriever()

    print("✅ Vector DB Ready")


# -------------------------------
def get_answer(query: str):
    global retriever

    if retriever is None:
        print("⚠️ No DB → rebuilding...")
        build_vectorstore()

    if retriever is None:
        return "❌ No documents found. Please upload files first.", []

    docs = retriever.invoke(query)

    if not docs:
        return "❌ This question is not from uploaded documents.", []

    context = "\n".join([d.page_content for d in docs])
    sources = list(set([d.metadata.get("source", "") for d in docs]))

    prompt = f"""
    Answer ONLY using the context below.

    If answer not found, say:
    "I don't know based on the provided documents."

    Context:
    {context}

    Question: {query}
    """

    response = llm.invoke(prompt)

    return response.content, sources