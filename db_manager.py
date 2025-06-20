import sqlite3
import os

DB_PATH = os.path.join("data", "finances.db")

def connect():
    return sqlite3.connect(DB_PATH)

def init_db():
    with connect() as conn:
        c = conn.cursor()

        # Tabela de contas
        c.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                balance REAL DEFAULT 0.0
            )
        ''')

        # Tabela de categorias
        c.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        ''')

        # Tabela de transações
        c.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_id INTEGER,
                category_id INTEGER,
                amount REAL NOT NULL,
                type TEXT CHECK(type IN ('income', 'expense')) NOT NULL,
                description TEXT,
                date TEXT NOT NULL,
                FOREIGN KEY(account_id) REFERENCES accounts(id),
                FOREIGN KEY(category_id) REFERENCES categories(id)
            )
        ''')

        # Tabela de objetivos
        c.execute('''
            CREATE TABLE IF NOT EXISTS goals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                target_amount REAL NOT NULL,
                current_amount REAL DEFAULT 0.0,
                deadline TEXT
            )
        ''')

        conn.commit()

def add_account(name, balance):
    with connect() as conn:
        conn.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, balance))
        conn.commit()

def get_accounts():
    with connect() as conn:
        cursor = conn.execute("SELECT * FROM accounts")
        return cursor.fetchall()

def add_transaction(account_id, category_id, amount, type_, description, date):
    with connect() as conn:
        conn.execute("""
            INSERT INTO transactions (account_id, category_id, amount, type, description, date)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (account_id, category_id, amount, type_, description, date))
        conn.commit()

def get_recent_transactions(limit=5):
    with connect() as conn:
        cursor = conn.execute("""
            SELECT t.id, a.name AS account, c.name AS category, t.amount, t.type, t.description, t.date
            FROM transactions t
            LEFT JOIN accounts a ON t.account_id = a.id
            LEFT JOIN categories c ON t.category_id = c.id
            ORDER BY date(t.date) DESC
            LIMIT ?
        """, (limit,))
        return cursor.fetchall()
