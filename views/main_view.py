import customtkinter as ctk
import os
import utils.styles

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.place(relwidth=1, relheight=1)
        self.pack_propagate(False)
        self.main_frame = MainFrame(self, controller=None)
        self.main_frame.pack(fill="both", expand=True)
        self.build_ui()

    def build_ui(self):
        title_label = ctk.CTkLabel(self, text="Finance Manager", font=ctk.CTkFont(size=24, weight="bold"))






