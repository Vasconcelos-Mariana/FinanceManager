import db_manager

def save_transaction(account_id, category_id, amount, type_, description, date):
    db_manager.add_transaction(account_id, category_id, amount, type_, description, date)

def fetch_recent_transactions(limit=5):
    return db_manager.get_recent_transactions(limit)