import reflex as rx

from RAG.components.navbar import navbar
from RAG.states.rag_state import ChatState


def chat() -> rx.Component:
    return rx.vstack(
        navbar(),

        rx.box(
            rx.vstack(
                # Header
                rx.hstack(
                    rx.hstack(
                        rx.icon(tag="message_square", size=24, color="#2563eb"),  # ✅ FIX
                        rx.heading("Secure AI Assistant", size="6"),
                        spacing="2",
                        align="center",
                    ),
                    rx.spacer(),
                    rx.button(
                        rx.icon(tag="plus"),
                        "New Chat",
                        on_click=ChatState.clear_history,
                    ),
                    width="100%",
                ),

                # Chat Area
                rx.box(
                    rx.vstack(
                        # Empty
                        rx.cond(
                            ChatState.history.length() == 0,
                            rx.text("Ask questions from your uploaded files")
                        ),

                        # Messages
                        rx.foreach(
                            ChatState.history,
                            lambda item: message_pair(item)
                        ),

                        # Loading
                        rx.cond(
                            ChatState.is_loading,
                            rx.hstack(
                                rx.spinner(),
                                rx.text("Thinking...")
                            )
                        ),
                    ),
                    flex="1",
                    width="100%",
                    overflow_y="auto",
                ),

                # Input
                rx.form(
                    rx.hstack(
                        rx.input(
                            name="chat_input",
                            placeholder="Ask something...",
                            width="100%",
                        ),
                        rx.button(
                            rx.icon(tag="send"),
                            type="submit",
                        ),
                        width="100%",
                    ),
                    on_submit=ChatState.handle_submit,
                    reset_on_submit=True,
                ),

                height="85vh",
                width="100%",
                max_width="900px",
                margin="auto",
            ),
            width="100%",
        )
    )


# --------------------------
# Message UI
# --------------------------
def message_pair(item):
    return rx.vstack(

        # User
        rx.hstack(
            rx.spacer(),
            rx.box(
                rx.text(item.question),
                background="#2563eb",
                color="white",
                padding="10px",
            ),
            width="100%",
        ),

        # AI
        rx.hstack(
            rx.icon(tag="bot"),
            rx.vstack(
                rx.text(item.answer),

                # ✅ safe condition
                rx.cond(
                    item.sources != "",
                    rx.text("Source: " + item.sources)
                ),
            ),
            width="100%",
        ),
    )