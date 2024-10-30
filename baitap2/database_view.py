
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

class DatabaseView:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        
        # Database connection fields
        self.user = tk.StringVar(value='postgres')
        self.password = tk.StringVar(value='123456')

        # Create the login GUI elements
        self.create_login_widgets()
        

    def create_login_widgets(self):
        connection_frame = tk.Frame(self.root, bg="#f2f2f2", bd=5)
        connection_frame.pack(pady=20, padx=20)

        tk.Label(connection_frame, text="User:", font=("Arial", 12, "bold"), bg="#f2f2f2").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(connection_frame, textvariable=self.user, font=("Arial", 12), width=25).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(connection_frame, text="Password:", font=("Arial", 12, "bold"), bg="#f2f2f2").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(connection_frame, textvariable=self.password, show="*", font=("Arial", 12), width=25).grid(row=2, column=1, padx=10, pady=10)

        tk.Button(connection_frame, text="Login", command=self.on_login, font=("Arial", 12), bg="#4CAF50", fg="white", padx=20, pady=5).grid(row=3, columnspan=2, pady=10)

    def on_login(self):
        if self.login_callback:
            self.login_callback(self.user.get(), self.password.get())
            messagebox.showinfo("Success", "Login successfully!")
            self.root.withdraw()

    def open_data_window(self):
        self.data_window = tk.Toplevel(self.root)
        self.data_window.title("Quản Lí Sinh Viên")
        self.data_window.configure(bg="#e6f7ff")

        query_frame = tk.Frame(self.data_window, bg="#e6f7ff")
        query_frame.pack(pady=10, padx=20)

        self.table_name = tk.StringVar(value='sinhvien')
        tk.Label(query_frame, text="Table Name:", font=("Arial", 12, "bold"), bg="#e6f7ff").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(query_frame, textvariable=self.table_name, font=("Arial", 12), width=30).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(query_frame, text="Load Data", command=self.load_data_callback, font=("Arial", 12), bg="#008CBA", fg="white", padx=10, pady=5).grid(row=1, columnspan=2, pady=10)

        self.data_display = tk.Text(self.data_window, height=10, width=50, font=("Arial", 12))
        self.data_display.pack(pady=10, padx=20)

        action_frame = tk.Frame(self.data_window, bg="#e6f7ff")
        action_frame.pack(pady=20)

        tk.Button(action_frame, text="Insert Data", command=self.open_insert_window, font=("Arial", 12), bg="#4CAF50", fg="white", padx=15, pady=5).grid(row=2, columnspan=2, pady=10)
        tk.Button(action_frame, text="Update Data", command=self.open_update_window, font=("Arial", 12), bg="#FF9800", fg="white", padx=15, pady=5).grid(row=3, columnspan=2, pady=10)
        tk.Button(action_frame, text="Delete Data", command=self.open_delete_window, font=("Arial", 12), bg="#F44336", fg="white", padx=15, pady=5).grid(row=4, columnspan=2, pady=10)

    def set_login_callback(self, callback):
        self.login_callback = callback

    def set_load_data_callback(self, callback):
        self.load_data_callback = callback

    def load_data(self, rows):
        self.data_display.delete(1.0, tk.END)
        for row in rows:
            self.data_display.insert(tk.END, f"{row}\n")

    def open_insert_window(self):
        self.insert_window = tk.Toplevel(self.data_window)
        self.insert_window.title("Insert Data")
        self.insert_window.configure(bg="#ffebcc")
        

        self.insert_name = tk.StringVar()
        self.insert_mssv = tk.StringVar()
        self.insert_dob = tk.StringVar()

        tk.Label(self.insert_window, text="Ho ten:", font=("Arial", 12, "bold"), bg="#ffebcc").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.insert_window, textvariable=self.insert_name, font=("Arial", 12), width=25).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.insert_window, text="MSSV:", font=("Arial", 12, "bold"), bg="#ffebcc").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.insert_window, textvariable=self.insert_mssv, font=("Arial", 12), width=25).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.insert_window, text="Ngày sinh:", font=("Arial", 12, "bold"), bg="#ffebcc").grid(row=2, column=0, padx=10, pady=10)
        DateEntry(self.insert_window, textvariable=self.insert_dob, font=("Arial", 12), width=25).grid(row=2, column=1, padx=10, pady=10)

        tk.Button(self.insert_window, text="Insert", command=self.insert_data_callback, font=("Arial", 12), bg="#4CAF50", fg="white", padx=15, pady=5).grid(row=3, columnspan=2, pady=10)

    def set_insert_data_callback(self, callback):
        self.insert_data_callback = callback
        
    
    
        

    def open_update_window(self):
        self.update_window = tk.Toplevel(self.data_window)
        self.update_window.title("Update Data")
        self.update_window.configure(bg="#ffebcc")

        self.update_name = tk.StringVar()
        self.update_mssv = tk.StringVar()
        self.update_dob = tk.StringVar()

        tk.Label(self.update_window, text="New Ho ten:", font=("Arial", 12, "bold"), bg="#ffebcc").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.update_window, textvariable=self.update_name, font=("Arial", 12), width=25).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.update_window, text="MSSV:", font=("Arial", 12, "bold"), bg="#ffebcc").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.update_window, textvariable=self.update_mssv, font=("Arial", 12), width=25).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.update_window, text="New Ngày sinh:", font=("Arial", 12, "bold"), bg="#ffebcc").grid(row=2, column=0, padx=10, pady=10)
        DateEntry(self.update_window, textvariable=self.update_dob, font=("Arial", 12), width=25).grid(row=2, column=1, padx=10, pady=10)

        tk.Button(self.update_window, text="Update", command=self.update_data_callback, font=("Arial", 12), bg="#FF9800", fg="white", padx=15, pady=5).grid(row=3, columnspan=2, pady=10)

    def set_update_data_callback(self, callback):
        self.update_data_callback = callback

    
        

    def open_delete_window(self):
        self.delete_window = tk.Toplevel(self.data_window)
        self.delete_window.title("Delete Data")
        self.delete_window.configure(bg="#ffebcc")

        self.delete_mssv = tk.StringVar()

        tk.Label(self.delete_window, text="MSSV:", font=("Arial", 12, "bold"), bg="#ffebcc").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.delete_window, textvariable=self.delete_mssv, font=("Arial", 12), width=25).grid(row=0, column=1, padx=10, pady=10)

        tk.Button(self.delete_window, text="Delete", command=self.delete_data_callback, font=("Arial", 12), bg="#F44336", fg="white", padx=15, pady=5).grid(row=1, columnspan=2, pady=10)

    def set_delete_data_callback(self, callback):
        self.delete_data_callback = callback
