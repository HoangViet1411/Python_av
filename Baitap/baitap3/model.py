import psycopg2
from psycopg2 import sql
from tkinter import messagebox

class Database:
    def __init__(self, dbname, user, password, host='localhost', port='5432'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connect(self):
        try:
            connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            return connection
        except Exception as e:
            messagebox.showerror("Error", f"Không thể kết nối tới cơ sở dữ liệu: {e}")
            return None

    def add_room(self, room_number, room_type, status, price, description):
        connection = self.connect()
        if connection:
            try:
                cursor = connection.cursor()
                query = sql.SQL("""
                    INSERT INTO rooms (room_number, room_type, status, price, description)
                    VALUES (%s, %s, %s, %s, %s)
                """)
                cursor.execute(query, (room_number, room_type, status, price, description))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Exception as e:
                messagebox.showerror("Error", f"Lỗi khi thêm phòng: {e}")
                return False
        return False

    

    
    def update_room(self, room_number, room_type, status, price, description):
        connection = self.connect()
        if connection:
            try:
                cursor = connection.cursor()
                query = sql.SQL("""
                    UPDATE rooms 
                    SET room_type = %s, status = %s, price = %s, description = %s 
                    WHERE room_number = %s
                """)
                cursor.execute(query, (room_type, status, price, description, room_number))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Exception as e:
                messagebox.showerror("Error", f"Lỗi khi sửa phòng: {e}")
                return False
        return False

    def delete_room(self, room_number):
        connection = self.connect()
        if connection:
            try:
                cursor = connection.cursor()
                query = sql.SQL("""
                    DELETE FROM rooms WHERE room_number = %s
                """)
                cursor.execute(query, (room_number,))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Exception as e:
                messagebox.showerror("Error", f"Lỗi khi xóa phòng: {e}")
                return False
        return False
    
    def get_all_rooms(self):
        connection = self.connect()
        rooms = []
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM rooms ORDER BY room_number ASC")  # Sắp xếp phòng theo số phòng
                rooms = cursor.fetchall()
                cursor.close()
                connection.close()
            except Exception as e:
                messagebox.showerror("Error", f"Lỗi khi lấy danh sách phòng: {e}")
        return rooms
    
    def get_room_by_number(self, room_number):
        connection = self.connect()
        room = None
        if connection:
            try:
                cursor = connection.cursor()
                query = sql.SQL("SELECT * FROM rooms WHERE room_number = %s")
                cursor.execute(query, (room_number,))
                room = cursor.fetchone()
                cursor.close()
                connection.close()
            except Exception as e:
                print(f"Lỗi khi lấy thông tin phòng: {e}")
        return room
    
    
