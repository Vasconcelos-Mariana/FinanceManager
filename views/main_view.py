import customtkinter as ctk
from controllers import main_controller


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

        ctk.CTkLabel(sidebar,
            text="    Menu Principal    ",font=ctk.CTkFont("Calibri", 20, weight="bold"),text_color="white"
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

# Version
        ctk.CTkLabel(sidebar,
            text="    v  0.1.0",font=ctk.CTkFont(size=11),text_color="white",).pack(side="bottom", anchor='w', pady=10)


# Dashboard

        self.main_area = ctk.CTkFrame(self, fg_color="#1c6a42",corner_radius=0)
        self.main_area.pack(side="left", fill="both", expand=True)

        ctk.CTkLabel(
            self.main_area,
            text="Dashboard View",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="white",
        ).pack(pady=(20,10))

# COLUMNS CONTAINER
        content_container = ctk.CTkFrame(self.main_area, fg_color="transparent")
        content_container.pack(fill="both", expand=True, padx=20, pady=20)

# LEFT COLUMN (mais estreita)
        left_col = ctk.CTkFrame(content_container, fg_color="transparent", width=800)
        left_col.pack(side="left", fill="y", expand=False, padx=(0, 10))
        left_col.pack_propagate(False)

# RIGHT COLUMN (ocupa o resto)
        right_col = ctk.CTkFrame(content_container, fg_color="transparent")
        right_col.pack(side="left", fill="both", expand=True)

# LEFT TOP CONTENT - mais alto
        frame_balance = ctk.CTkFrame(left_col, fg_color="#e0f6e6", corner_radius=10, height=350)
        frame_balance.pack(fill="x", padx=(0.0), pady=(0, 10))
        frame_balance.pack_propagate(False)

# CONTAINER - LEFT BOTTOM (ocupa tudo)
        left_bottom_container = ctk.CTkFrame(left_col, fg_color="transparent")
        left_bottom_container.pack(fill="both", expand=True)
        left_bottom_container.pack_propagate(False)

# LEFT COLUMN - BOTTOM LEFT CONTENT (Recent Transactions)
        def display_recent_transactions(self):
    # Limpa o conteúdo anterior do frame
            for widget in self.frame_transactions.winfo_children():
                widget.destroy()

    # Título
            ctk.CTkLabel(
                self.frame_transactions,
                text="Recent Transactions",
                font=ctk.CTkFont(size=16, weight="bold"),
                text_color="black"
            ).pack(pady=(10, 5))

    # Obter transações do controller principal
            transactions = main_controller.get_recent_transactions()

    # Se não houver transações, mostrar mensagem
            if not transactions:
                ctk.CTkLabel(
                    self.frame_transactions,
                    text="No transactions yet.",
                    font=ctk.CTkFont(size=12),
                    text_color="gray"
                ).pack(pady=10)
                return

    # Mostrar cada transação
            for tx in transactions:
                tx_text = f"[{tx[6]}] {tx[3]:.2f}€ ({tx[4]})\n{tx[5]} – {tx[2]} ({tx[1]})"
                label = ctk.CTkLabel(
                    self.frame_transactions,
                    text=tx_text,
                    anchor="w",
                    justify="left",
                    font=ctk.CTkFont(size=12),
                    text_color="#1a1a1a"
                )
                label.pack(fill="x", padx=10, pady=4)

# LEFT COLUMN - BOTTOM RIGHT CONTENT (Statistics)
        frame_statistics = ctk.CTkFrame(
            left_bottom_container,
            fg_color="#e0f6e6",
        corner_radius=10,
        width=200,
        height=100
        )
        frame_statistics.pack(side="left", fill="both", expand=True, padx=(5, 0))
        frame_statistics.pack_propagate(False)


# RIGHT TOP CONTENT
        frame_spending = ctk.CTkFrame(right_col, fg_color="#e0f6e6", corner_radius=10, height=400)
        frame_spending.pack(fill="x", pady=(0,10))
        frame_spending.pack_propagate(False)

# RIGHT BOTTOM CONTENT
        frame_goals = ctk.CTkFrame(right_col, fg_color="#e0f6e6", corner_radius=10, height=300)
        frame_goals.pack(fill="x")
        frame_goals.pack_propagate(False)

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