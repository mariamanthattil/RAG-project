import reflex as rx
from RAG.components.navbar import nav_bar


def upload_page():
    return rx.vstack(
        nav_bar(),
        rx.heading("Upload Documents"),
        rx.text("Upload your files here"),
        rx.button("Upload"),
        padding="20px"
    )