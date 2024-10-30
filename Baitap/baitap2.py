import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import sql
from tkcalendar import DateEntry  # Import DateEntry from tkcalendar

class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")

        # Database connection fields
        self.user = tk.StringVar(value='postgres')
        self.password = tk.StringVar(value='123456')

        # Create the login GUI elements
        self.create_login_widgets()

    def create_login_widgets(self):
        # Connection section
        connection_frame = tk.Frame(self.root, bg="#f2f2f2", bd=5)
        connection_frame.pack(pady=20, padx=20)

        tk.Label(connection_frame, text="User:", font=("Arial", 12, "bold"), bg="#f2f2f2").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(connection_frame, textvariable=self.user, font=("Arial", 12), width=25).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(connection_frame, text="Password:", font=("Arial", 12, "bold"), bg="#f2f2f2").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(connection_frame, textvariable=self.password, show="*", font=("Arial", 12), width=25).grid(row=2, column=1, padx=10, pady=10)

        tk.Button(connection_frame, text="Login", command=self.connect_db, font=("Arial", 12), bg="#4CAF50", fg="white", padx=20, pady=5).grid(row=3, columnspan=2, pady=10)

    def connect_db(self):
        try:
            self.conn = psycopg2.connect(
                dbname='dbtest1',
                user=self.user.get(),
                password=self.password.get(),
                host='localhost',
                port='5432'
            )
            self.cur = self.conn.cursor()
            messagebox.showinfo("Success", "Connected to the database successfully!")
            self.root.withdraw()  # Close the login window
            self.open_data_window()  # Open new window to load, insert, update, and delete data
        except Exception as e:
            messagebox.showerror("Error", f"Error connecting to the database: {e}")

    def open_data_window(self):
        # Create a new window for loading, inserting, updating, and deleting data
        self.data_window = tk.Toplevel(self.root)
        self.data_window.title("Quản Lí Sinh Viên")
        self.data_window.configure(bg="#e6f7ff")  # Background color for the window

        # Query section
        query_frame = tk.Frame(self.data_window, bg="#e6f7ff")
        query_frame.pack(pady=10, padx=20)

        self.table_name = tk.StringVar(value='sinhvien')
        tk.Label(query_frame, text="Table Name:", font=("Arial", 12, "bold"), bg="#e6f7ff").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(query_frame, textvariable=self.table_name, font=("Arial", 12), width=30).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(query_frame, text="Load Data", command=self.load_data, font=("Arial", 12), bg="#008CBA", fg="white", padx=10, pady=5).grid(row=1, columnspan=2, pady=10)

        self.data_display = tk.Text(self.data_window, height=10, width=50, font=("Arial", 12))
        self.data_display.pack(pady=10, padx=20)

        # Insert, Update, Delete section
        action_frame = tk.Frame(self.data_window, bg="#e6f7ff")
        action_frame.pack(pady=20)

        tk.Button(action_frame, text="Insert Data", command=self.open_insert_window, font=("Arial", 12), bg="#4CAF50", fg="white", padx=15, pady=5).grid(row=2, columnspan=2, pady=10)
        tk.Button(action_frame, text="Update Data", command=self.open_update_window, font=("Arial", 12), bg="#FF9800", fg="white", padx=15, pady=5).grid(row=3, columnspan=2, pady=10)
        tk.Button(action_frame, text="Delete Data", command=self.open_delete_window, font=("Arial", 12), bg="#F44336", fg="white", padx=15, pady=5).grid(row=4, columnspan=2, pady=10)

    def load_data(self):
        try:
            query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(self.table_name.get()))
            self.cur.execute(query)
            rows = self.cur.fetchall()
            self.data_display.delete(1.0, tk.END)
            for row in rows:
                self.data_display.insert(tk.END, f"{row}\n")
        except Exception as e:
            messagebox.showerror("Error", f"Error loading data: {e}")

    def open_insert_window(self):
        self.insert_window = tk.Toplevel(self.data_window)
        self.insert_window.title("Insert Data")
        self.insert_window.configure(bg="#ffebcc")

        self.insert_name = tk.StringVar()
        self.insert_mssv = tk.StringVar()
        self.insert_dob = tk.StringVar()  # Date of Birth

        tk.Label(self.insert_window, text="Ho ten:", font=("Arial", 12, "bold"), bg="#ffebcc").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.insert_window, textvariable=self.insert_name, font=("Arial", 12), width=25).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.insert_window, text="MSSV:", font=("Arial", 12, "bold"), bg="#ffebcc").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.insert_window, textvariable=self.insert_mssv, font=("Arial", 12), width=25).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.insert_window, text="Ngày sinh:", font=("Arial", 12, "bold"), bg="#ffebcc").grid(row=2, column=0, padx=10, pady=10)
        DateEntry(self.insert_window, textvariable=self.insert_dob, font=("Arial", 12), width=25).grid(row=2, column=1, padx=10, pady=10)  # Calendar widget

        tk.Button(self.insert_window, text="Insert", command=self.insert_data, font=("Arial", 12), bg="#4CAF50", fg="white", padx=15, pady=5).grid(row=3, columnspan=2, pady=10)

    def insert_data(self):
        try:
            insert_query = sql.SQL("INSERT INTO {} (massv, hoten, ngaysinh) VALUES (%s, %s, %s)").format(sql.Identifier(self.table_name.get()))
            data_to_insert = (self.insert_mssv.get(), self.insert_name.get(), self.insert_dob.get())  # MSSV first, then Name, then DOB
            self.cur.execute(insert_query, data_to_insert)
            self.conn.commit()
            messagebox.showinfo("Success", "Data inserted successfully!")
            self.insert_window.destroy()  # Close insert window
        except Exception as e:
            messagebox.showerror("Error", f"Error inserting data: {e}")

    def open_update_window(self):
        self.update_window = tk.Toplevel(self.data_window)
        self.update_window.title("Update Data")
        self.update_window.configure(bg="#ffebcc")

        self.update_name = tk.StringVar()
        self.update_mssv = tk.StringVar()
        self.update_dob = tk.StringVar()  # Date of Birth

        tk.Label(self.update_window, text="New Ho ten:", font=("Arial", 12, "bold"), bg="#ffebcc").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.update_window, textvariable=self.update_name, font=("Arial", 12), width=25).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.update_window, text="MSSV:", font=("Arial", 12, "bold"), bg="#ffebcc").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.update_window, textvariable=self.update_mssv, font=("Arial", 12), width=25).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.update_window, text="New Ngày sinh:", font=("Arial", 12, "bold"), bg="#ffebcc").grid(row=2, column=0, padx=10, pady=10)
        DateEntry(self.update_window, textvariable=self.update_dob, font=("Arial", 12), width=25).grid(row=2, column=1, padx=10, pady=10)  # Calendar widget

        tk.Button(self.update_window, text="Update", command=self.update_data, font=("Arial", 12), bg="#4CAF50", fg="white", padx=15, pady=5).grid(row=3, columnspan=2, pady=10)

    def update_data(self):
        try:
            update_query = sql.SQL("UPDATE {} SET hoten = %s, ngaysinh = %s WHERE massv = %s").format(sql.Identifier(self.table_name.get()))
            data_to_update = (self.update_name.get(), self.update_dob.get(), self.update_mssv.get())  # Name, DOB, MSSV
            self.cur.execute(update_query, data_to_update)
            self.conn.commit()
            messagebox.showinfo("Success", "Data updated successfully!")
            self.update_window.destroy()  # Close update window
        except Exception as e:
            messagebox.showerror("Error", f"Error updating data: {e}")

    def open_delete_window(self):
        self.delete_window = tk.Toplevel(self.data_window)
        self.delete_window.title("Delete Data")
        self.delete_window.configure(bg="#ffebcc")

        self.delete_mssv = tk.StringVar()

        tk.Label(self.delete_window, text="MSSV:", font=("Arial", 12, "bold"), bg="#ffebcc").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.delete_window, textvariable=self.delete_mssv, font=("Arial", 12), width=25).grid(row=0, column=1, padx=10, pady=10)

        tk.Button(self.delete_window, text="Delete", command=self.delete_data, font=("Arial", 12), bg="#4CAF50", fg="white", padx=15, pady=5).grid(row=1, columnspan=2, pady=10)

    def delete_data(self):
        try:
            delete_query = sql.SQL("DELETE FROM {} WHERE massv = %s").format(sql.Identifier(self.table_name.get()))
            self.cur.execute(delete_query, (self.delete_mssv.get(),))
            self.conn.commit()
            messagebox.showinfo("Success", "Data deleted successfully!")
            self.delete_window.destroy()  # Close delete window
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting data: {e}")

    def close_db(self):
        if hasattr(self, 'cur'):
            self.cur.close()
        if hasattr(self, 'conn'):
            self.conn.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.protocol("WM_DELETE_WINDOW", app.close_db)
    root.mainloop()
