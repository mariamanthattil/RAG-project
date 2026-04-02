import reflex as rx
from typing import List
from RAG.backend.rag import get_answer
from pydantic import BaseModel
import os

class ChatItem(BaseModel):
    question: str
    answer: str
    sources: str

class ChatState(rx.State):
    question: str = ""
    history: List[ChatItem] = []
    is_loading: bool = False

    def handle_submit(self, form_data: dict):
        self.question = form_data.get("chat_input", "").strip()
        self.ask_question()

    def ask_question(self):
        if not self.question:
            return

        self.is_loading = True

        # 🔥 Get answer from backend
        answer, sources = get_answer(self.question)

        # ✅ SAFE SOURCE HANDLING
        if isinstance(sources, list) and len(sources) > 0:
            sources = ", ".join([os.path.basename(s) for s in sources])
        else:
            sources = "Uploaded Documents"

        new_item = ChatItem(
            question=self.question,
            answer=answer,
            sources=sources
        )

        self.history = self.history + [new_item]

        self.question = ""
        self.is_loading = False

    def clear_history(self):
        self.history = []

    # ✅ OPTIONAL (safe PDF download)
    def download_chat(self):
        try:
            import io
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
            from reportlab.lib.styles import getSampleStyleSheet

            buffer = io.BytesIO()
            doc = SimpleDocTemplate(buffer)
            styles = getSampleStyleSheet()
            elements = []

            for item in self.history:
                elements.append(Paragraph(f"<b>Question:</b> {item.question}", styles["Normal"]))
                elements.append(Spacer(1, 10))

                elements.append(Paragraph(f"<b>Answer:</b> {item.answer}", styles["Normal"]))
                elements.append(Spacer(1, 10))

                elements.append(Paragraph(f"<b>Sources:</b> {item.sources}", styles["Normal"]))
                elements.append(Spacer(1, 20))

            doc.build(elements)

            pdf_data = buffer.getvalue()
            buffer.close()

            return rx.download(data=pdf_data, filename="chat_history.pdf")

        except Exception as e:
            print("PDF Error:", e)
            return