import reflex as rx


def nav_bar():
    return rx.hstack(
        
        # 🔹 Left side (Icon + Title)
        rx.hstack(
            rx.icon(tag="brain"),
            rx.text(
                "AI Document Search",
                font_weight="bold",
                font_size="20px",
            ),
            spacing="2",
            align="center",
        ),

        rx.spacer(),

        # 🔹 Right side (Navigation links)
        rx.hstack(
            rx.link("Home", href="/"),
            rx.link("Upload", href="/upload"),
            rx.link("Chat", href="/chat"),
            rx.link("History", href="/history"),
            rx.link("About", href="/about"),
            spacing="6",
            align="center",
        ),

        # 🔹 Styling
        width="100%",
        padding="15px",
        border_bottom="1px solid #eaeaea",
        align="center",
    )