import customtkinter as ctk
from views.main_view import MainFrame

class AppController(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Gestor de Finanças')
        self.after(0, lambda: self.state("zoomed"))
        self.frames = {}
        self.build_frames()
        self.show_frame("main")

    def build_frames(self):
        self.frames["main"] = MainFrame(self, self)

        for frame in self.frames.values():
            frame.place(relwidth=1, relheight=1)


    def show_frame(self, name, **kwargs):
        for frame in self.frames.values():
            frame.place_forget()

        frame = self.frames[name]
        frame.place(relwidth=1, relheight=1)
        frame.tkraise()

        if name == "timer" and "project" in kwargs:
            frame.start(kwargs["project"])

        if hasattr(frame, "on_show"):
            frame.on_show()