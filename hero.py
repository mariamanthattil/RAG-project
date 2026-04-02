import reflex as rx


def hero():
    return rx.vstack(

        # 🔥 Animation styles
        rx.html("""
        <style>
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        </style>
        """),

        rx.box(
            # ---------------- TEXT ----------------
            rx.text(
                "Enterprise Ready",
                font_size="14px",
                font_weight="700",
                color="#2563eb",
                text_transform="uppercase",
                text_align="center"
            ),

            rx.heading(
                rx.text.span(
                    "AI Document Intelligence",
                    background_image="linear-gradient(90deg, #1e3a8a, #2563eb, #0ea5e9)",
                    background_clip="text",
                    color="transparent"
                ),
                rx.text.span("\nSearch & Retrieval", color="white"),
                size="9",
                text_align="center",
                style={
                    "animation": "fadeIn 1.2s ease-in-out",
                    "font_size": "clamp(3rem, 5vw, 4rem)"
                }
            ),

            rx.text(
                "Chat with your documents instantly using AI-powered RAG system.",
                color="#e2e8f0",
                font_size="18px",
                text_align="center",
                max_width="600px",
                margin_y="20px"
            ),

            # ---------------- BUTTON ----------------
            rx.button(
                "Get Started",
                rx.icon(tag="arrow-right"),
                on_click=lambda: rx.redirect("/upload"),   # ✅ FIXED
                background="linear-gradient(90deg, #2563eb, #3b82f6)",
                color="white",
                size="4",
                radius="full",
                padding_x="30px",
                padding_y="20px",
                style={
                    "_hover": {
                        "transform": "translateY(-3px) scale(1.05)",
                        "box_shadow": "0 0 25px rgba(59,130,246,0.8)"
                    },
                    "transition": "all 0.3s ease"
                }
            ),

            padding="80px 20px",
            text_align="center",

            # ---------------- BACKGROUND IMAGE ----------------
            style={
                "background_image": "linear-gradient(rgba(15,23,42,0.7), rgba(15,23,42,0.7)), url('/images.jpg')",  # ✅ FIXED NAME
                "background_size": "cover",
                "background_position": "center",
                "background_repeat": "no-repeat",

                "backdrop_filter": "blur(6px)",
                "border_radius": "16px",
                "border": "1px solid rgba(255,255,255,0.1)"
            }
        ),

        align="center"
    )