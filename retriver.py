
# Step 1: Your source documents
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

# Step 2: Initialize embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
# Step 3: Create Chroma vector store in memory

vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="my_collection"
)
# Step 4: Convert vectorstore into a retriever
retriever = vectorstore.as_retriever(
    search_type="mmr",                 # <-- This enables MMR
    search_kwargs={
        "k": 3,                        # top results
        "lambda_mult": 1               # relevance–diversity balance
    }
)

Query = "what is the chroma used for?"
Results = retriever.invoke(Query)

for i, doc in enumerate(Results):
      print(f"\n----Results {i+1} ----"),
      print(doc)