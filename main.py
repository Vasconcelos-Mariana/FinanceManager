from controllers.app_controller import AppController
from db_manager import init_db

if __name__ == '__main__':
    init_db()
    app = AppController()
    app.mainloop()