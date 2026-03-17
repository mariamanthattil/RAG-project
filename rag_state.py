import reflex as rx
from RAG.retriever import corrective_rag

class RAGState(rx.State):

    question: str = ""
    answer: str = ""
    sources: list[str] = []

    def ask_question(self):
        result = corrective_rag(self.answer,self.sources)
        self.answer = result[ "answer"]
        self.sources = result["sources"]