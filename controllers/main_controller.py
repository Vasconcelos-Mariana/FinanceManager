from controllers import transactions_controller

def get_recent_transactions(limit=5):
    return transactions_controller.fetch_recent_transactions(limit)