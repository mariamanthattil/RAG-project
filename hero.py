import reflex as rx


def hero_section():
    return rx.box(
        rx.vstack(
            
            # 🔹 Badge
            rx.badge(
                "RAG Powered Knowledge Assistant",
                color_scheme="green",
                variant="soft",  # ✅ FIXED (was "subtle")
                margin_bottom="10px",
            ),

            # 🔹 Main Heading
            rx.heading(
                "AI Document Knowledge Assistant",
                size="8",
                text_align="center",
            ),

            # 🔹 Description Text
            rx.text(
                "Upload documents and ask questions to get accurate, context-aware answers.",
                text_align="center",
                color="gray",
                max_width="600px",
            ),

            # 🔹 Buttons
            rx.hstack(
                rx.button(
                    "Upload Documents",
                    color_scheme="green",
                    size="3",
                ),
                rx.button(
                    "Ask Questions",
                    variant="outline",
                    size="3",
                ),
                spacing="4",
                margin_top="20px",
            ),

            spacing="4",
            align="center",
        ),

        # 🔹 Full Page Styling
        height="80vh",
        display="flex",
        align_items="center",
        justify_content="center",
    )