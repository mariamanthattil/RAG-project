import reflex as rx
from RAG.components.navbar import navbar
from RAG.components.hero import hero

def home():
    return rx.vstack(
        navbar(),
        hero(),
        spacing="0",
    )


