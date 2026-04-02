import reflex as rx
from RAG.components.navbar import navbar
from RAG.components.hero import hero
from RAG.components.footer import footer

def home():
    return rx.vstack(
        navbar(),
        hero(),
        footer(),
    )