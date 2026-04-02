import reflex as rx
import os

from RAG.components.navbar import navbar
from RAG.backend.rag import build_vectorstore

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = os.path.join(BASE_DIR, "documents")

os.makedirs(UPLOAD_DIR, exist_ok=True)


class UploadState(rx.State):
    files: list[str] = []
    is_uploading: bool = False
    show_success_dialog: bool = False

    # -------------------
    def load_files(self):
        if os.path.exists(UPLOAD_DIR):
            self.files = os.listdir(UPLOAD_DIR)

    # -------------------
    # ✅ FIXED DELETE
    def delete_file(self, filename):
        if not filename:
            print("❌ Invalid filename")
            return

        if isinstance(filename, dict):
            filename = filename.get("name")

        if not filename:
            print("❌ Filename is None")
            return

        file_path = os.path.join(UPLOAD_DIR, filename)

        print("Deleting:", file_path)

        if os.path.exists(file_path):
            os.remove(file_path)
            print("✅ Deleted")
        else:
            print("❌ File not found")

        self.load_files()
        build_vectorstore()

        yield  # 🔥 UI refresh

    # -------------------
    def close_dialog(self):
        self.show_success_dialog = False

    # -------------------
    # ✅ FIXED UPLOAD
    async def handle_upload(self, files: list[rx.UploadFile]):
        if not files:
            return

        self.is_uploading = True
        yield

        for file in files:
            save_path = os.path.join(UPLOAD_DIR, file.filename)

            content = await file.read()
            with open(save_path, "wb") as f:
                f.write(content)

            print("Saved:", file.filename)

        self.load_files()

        print("🔥 Building vectorstore...")
        build_vectorstore()

        self.is_uploading = False
        self.show_success_dialog = True

        yield rx.clear_selected_files("upload1")


# -------------------
# UI
# -------------------
def upload():
    return rx.vstack(
        navbar(),

        rx.vstack(
            rx.heading("Data Knowledge Base", size="8"),
            rx.text("Upload PDF or text files"),

            rx.upload(
                rx.text("Drag & drop or click"),
                id="upload1",
            ),

            rx.button(
                "Upload",
                on_click=UploadState.handle_upload(
                    rx.upload_files(upload_id="upload1")
                ),
            ),

            # ✅ FILE LIST (FIXED BUTTON)
            rx.foreach(
                UploadState.files,
                lambda file: rx.hstack(
                    rx.text(file),
                    rx.button(
                        "Delete",
                        on_click=lambda f=file: UploadState.delete_file(f),  # 🔥 IMPORTANT FIX
                        color_scheme="red"
                    )
                )
            ),

            # SUCCESS POPUP
            rx.cond(
                UploadState.show_success_dialog,
                rx.box(
                    rx.vstack(
                        rx.text("Upload Complete"),
                        rx.button("Go to Chat", on_click=rx.redirect("/chat")),
                        rx.button("Stay", on_click=UploadState.close_dialog)
                    )
                )
            ),

            on_mount=UploadState.load_files,
            align="center"
        )
    )