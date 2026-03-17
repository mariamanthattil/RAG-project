import reflex as rx

from RAG.components.navbar import nav_bar
from RAG.components.hero import hero_section
from RAG.pages.chat import chat_page
from RAG.pages.upload import upload_page


def home():
    return rx.vstack(
        nav_bar(),
        hero_section(),
        spacing="0"
    )


app = rx.App()
app.add_page(home, route="/")
app.add_page(chat_page, route="/chat")
app.add_page(upload_page, route="/upload")