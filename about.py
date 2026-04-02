import reflex as rx
from RAG.components.navbar import navbar
from RAG.components.footer import footer

def about():
    return rx.box(
        navbar(),

        rx.box(
            rx.vstack(

                # Title
                rx.heading("🧠 About DocuAI", size="8", text_align="center"),
                rx.text(
                    "AI-powered document intelligence for smarter search and insights.",
                    color="#64748b",
                    text_align="center",
                    max_width="600px",
                ),

                # 🔥 Grid ഉപയോഗിക്കുക (simple_grid അല്ല)
                rx.grid(

                    rx.box(
                        rx.heading("⚙️ Key Features", size="5"),
                        rx.text("• Upload PDF, TXT, CSV"),
                        rx.text("• Natural language queries"),
                        rx.text("• Context-aware AI"),
                        style=card_style()
                    ),

                    rx.box(
                        rx.heading("🏗️ Architecture", size="5"),
                        rx.text("1. Upload"),
                        rx.text("2. Processing"),
                        rx.text("3. Chunking"),
                        rx.text("4. Embeddings"),
                        style=card_style()
                    ),

                    rx.box(
                        rx.heading("🧪 Technologies", size="5"),
                        rx.text("• Reflex + Python"),
                        rx.text("• Groq (LLaMA 3.1)"),
                        rx.text("• ChromaDB"),
                        style=card_style()
                    ),

                    rx.box(
                        rx.heading("🎯 Use Cases", size="5"),
                        rx.text("• Research"),
                        rx.text("• Resume analysis"),
                        rx.text("• Business insights"),
                        style=card_style()
                    ),

                    # 👇 grid settings
                    template_columns="repeat(auto-fit, minmax(250px, 1fr))",
                    gap="20px",
                    width="100%"
                ),

                spacing="6",
                align="center",
                max_width="1000px",
                margin="0 auto",
                padding="40px 20px"
            ),

            style={
                "background": "linear-gradient(135deg, #eff6ff, #ffffff)"
            }
        ),

        footer()
    )


def card_style():
    return {
        "background": "white",
        "padding": "20px",
        "border_radius": "16px",
        "border": "1px solid #e2e8f0",
        "box_shadow": "0 10px 20px rgba(0,0,0,0.05)",
        "transition": "0.3s",
        "_hover": {
            "transform": "translateY(-5px)",
            "box_shadow": "0 20px 30px rgba(0,0,0,0.1)"
        }
    }