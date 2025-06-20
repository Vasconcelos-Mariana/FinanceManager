import customtkinter as ctk

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(fg_color='#1d6b43')
        self.build_ui()

    def build_ui(self):
        font_title = ctk.CTkFont("Arial Rounded MT Bold", size=40, weight="bold")

        ctk.CTkLabel(
            self,
            text="Gestor de Finanças",
            font=font_title,
            text_color="#ffffff"
        ).pack(pady=(20, 10))
