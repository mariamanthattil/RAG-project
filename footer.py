import reflex as rx


def footer():
    return rx.box(
        rx.vstack(

            rx.hstack(
                # Left
                rx.vstack(
                    rx.heading("AI Doc Assistant", size="5", color="white"),
                    rx.text(
                        "Chat with your documents using AI-powered RAG system.",
                        color="#94a3b8",
                        font_size="14px",
                    ),
                    align="start",
                ),

                # Middle
                rx.vstack(
                    rx.text("Quick Links", color="white", font_weight="bold"),
                    rx.link("Home", href="/"),
                    rx.link("Upload", href="/upload"),
                    rx.link("Chat", href="/chat"),
                    align="start",
                ),

                # Right
                rx.vstack(
                    rx.text("Contact", color="white", font_weight="bold"),
                    rx.text("Email: support@example.com", color="#94a3b8"),
                    rx.text("Phone: +91 9876543210", color="#94a3b8"),
                    align="start",
                ),

                spacing="8",
                justify="between",
                width="100%",
            ),

            rx.divider(),

            rx.text(
                "© 2026 AI Document Assistant",
                color="#64748b",
                font_size="13px",
                text_align="center"
            ),

            spacing="4",
            width="100%",
        ),

        width="100%",          # ✅ FULL WIDTH
        padding="40px 80px",   # ✅ SIDE SPACE
        margin_top="60px",

        style={
            "background": "#0f172a",
            "border_top": "1px solid #1e293b"
        }
    )