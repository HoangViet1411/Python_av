
import psycopg2
from psycopg2 import sql
from tkinter import messagebox

class DatabaseModel:
    def __init__(self, dbname, user, password, host='localhost', port='5432'):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cur = self.conn.cursor()

    def load_data(self, table_name):
        try:
            query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
            self.cur.execute(query)
            return self.cur.fetchall()
        except Exception as e:
            messagebox.showerror("Error", f"Error loading data: {e}")
            return []

    def insert_data(self, table_name, massv, hoten, ngaysinh):
        try:
            insert_query = sql.SQL("INSERT INTO {} (massv, hoten, ngaysinh) VALUES (%s, %s, %s)").format(sql.Identifier(table_name))
            self.cur.execute(insert_query, (massv, hoten, ngaysinh))
            self.conn.commit()
            messagebox.showinfo("Success", "Insert thanh cong!")
        except Exception as e:
            messagebox.showerror("Error", f"Error inserting data: {e}")

    def update_data(self, table_name, massv, hoten, ngaysinh):
        try:
            update_query = sql.SQL("UPDATE {} SET hoten = %s, ngaysinh = %s WHERE massv = %s").format(sql.Identifier(table_name))
            self.cur.execute(update_query, (hoten, ngaysinh, massv))
            self.conn.commit()
            messagebox.showinfo("Success", "Update thanh cong!")
        except Exception as e:
            messagebox.showerror("Error", f"Error updating data: {e}")

    def delete_data(self, table_name, massv):
        try:
            delete_query = sql.SQL("DELETE FROM {} WHERE massv = %s").format(sql.Identifier(table_name))
            self.cur.execute(delete_query, (massv,))
            self.conn.commit()
            messagebox.showinfo("Success", "Delete thanh cong!")
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting data: {e}")

    def close(self):
        self.cur.close()
        self.conn.close()
