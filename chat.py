import reflex as rx
from RAG.states.rag_state import RAGState
from RAG.components.navbar import nav_bar


def chat_page():
    return rx.vstack(

        # 🔹 Navbar
        nav_bar(),

        # 🔹 Title
        rx.heading(
            "Ask Questions About Your Documents",
            size="6",
        ),

        # 🔹 Input box
        rx.input(
            placeholder="Ask something...",
            on_change=RAGState.set_question,
            width="100%",
        ),

        # 🔹 Ask button
        rx.button(
            "Ask",
            on_click=RAGState.ask_question,
        ),

        # 🔹 Answer box
        rx.box(
            rx.heading("Answer"),
            rx.text(RAGState.answer),
            margin_top="20px",
        ),

        # 🔹 Sources list
        rx.box(
            rx.heading("Sources"),
            rx.foreach(
                RAGState.sources,
                lambda src: rx.text(src)
            ),
            margin_top="10px",
        ),

        spacing="4",
        padding="20px",
    )