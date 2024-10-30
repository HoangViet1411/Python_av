
import tkinter as tk
from database_model import DatabaseModel
from database_view import DatabaseView

class Application:
    def __init__(self, root):
        self.root = root
        self.view = DatabaseView(self.root)
        self.model = None

        self.view.set_login_callback(self.login)
        self.view.set_load_data_callback(self.load_data)
        self.view.set_insert_data_callback(self.insert_data)
        self.view.set_update_data_callback(self.update_data)
        self.view.set_delete_data_callback(self.delete_data)

    def login(self, user, password):
        try:
            self.model = DatabaseModel('dbtest1', user, password)  
            self.view.open_data_window()
        except Exception as e:
            tk.messagebox.showerror("Login Failed", str(e))

    def load_data(self):
        if self.model:
            rows = self.model.load_data(self.view.table_name.get())
            self.view.load_data(rows)

    def insert_data(self):
        if self.model:
            self.model.insert_data(self.view.table_name.get(), self.view.insert_mssv.get(), self.view.insert_name.get(), self.view.insert_dob.get())
           
    
    def update_data(self):
        if self.model:
            self.model.update_data(self.view.table_name.get(), self.view.update_mssv.get(), self.view.update_name.get(), self.view.update_dob.get())
            

    def delete_data(self):
        if self.model:
            self.model.delete_data(self.view.table_name.get(), self.view.delete_mssv.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
