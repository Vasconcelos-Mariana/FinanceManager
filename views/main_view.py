import customtkinter as ctk

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(fg_color='#1d6b43')
        self.build_ui()

    def build_ui(self):

# Sidebar
        sidebar = ctk.CTkFrame (self,width=200, fg_color="#033520",corner_radius=0)
        sidebar.pack(side="left",fill="both", expand='false')

        ctk.CTkLabel(
            sidebar,
            text="    Menu Principal    ",
            font=ctk.CTkFont("Calibri", 20, weight="bold"),
            text_color="white"
        ).pack(pady=20)

        buttons = [
            ("Dasboard", self.go_dashboard),
            ("Accounts", self.go_accounts),
            ("Transactions", self.go_transactions),
            ("Goals", self.go_goals),
            ("Categories", self.go_category),
            ("Statistics", self.go_statistics),
            ("Settings", self.go_settings)
        ]

        for text, command in buttons:
            ctk.CTkButton(sidebar,
                text=text,
                command=command,
                fg_color="#033520",
                hover_color="#27815f",
                text_color="white",
                font=ctk.CTkFont(size=13),
                height=30,
                anchor="w",
            ).pack(pady=10, padx=20, fill="x")


        ctk.CTkLabel(
            sidebar,
            text="    v  0.1.0",
            font=ctk.CTkFont(size=11),
            text_color="white",
        ).pack(side="bottom", anchor='w', pady=10)


# Dashboard

        self.main_area = ctk.CTkFrame(self, fg_color="#7adca4",corner_radius=0)
        self.main_area.pack(side="left", fill="both", expand=True)

        ctk.CTkLabel(
            self.main_area,
            text="Dashboard View",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#0f3d2e"
        ).pack(pady=50)



    def go_dashboard(self):
        print("Dashboard clicked")

    def go_accounts(self):
        print("Accounts clicked")

    def go_transactions(self):
        print("Transactions clicked")

    def go_goals(self):
        print("Goals clicked")

    def go_category(self):
        print('Category clicked')

    def go_statistics(self):
        print('statistics clicked')


    def go_settings(self):
        print("Settings clicked")