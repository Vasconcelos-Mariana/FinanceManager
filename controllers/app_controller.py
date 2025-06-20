import customtkinter as ctk
from views.main_view import MainFrame

class AppController(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Time Manager')
        self.configure(fg_color='#2d804f')
        self.state("zoomed")

        self.frames = {}
        self.build_frames()
        self.show_frame("main")

    def build_frames(self):
        self.frames["main"] = MainFrame(self, self)

        for frame in self.frames.values():
            frame.place_forget()