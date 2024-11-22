from flask import Flask, render_template, request, redirect, url_for, flash
from model import Database

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

# Tạo đối tượng Database kết nối với PostgreSQL
db = Database(dbname="dbtest2", user="postgres", password="123456")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_room', methods=['GET', 'POST'])
def add_room():
    if request.method == 'POST':
        room_number = request.form['room_number']
        room_type = request.form['room_type']
        status = request.form['status']
        price = request.form['price']
        description = request.form['description']
        
        if db.add_room(room_number, room_type, status, price, description):
            flash("Phòng đã được thêm thành công!", "success")
        else:
            flash("Lỗi khi thêm phòng.", "error")
        return redirect(url_for('index'))
    
    return render_template('add_room.html')

@app.route('/update_room/<room_number>', methods=['GET', 'POST'])
def update_room(room_number):
    if request.method == 'POST':
        room_type = request.form['room_type']
        status = request.form['status']
        price = request.form['price']
        description = request.form['description']
        
        if db.update_room(room_number, room_type, status, price, description):
            flash("Phòng đã được cập nhật thành công!", "success")
        else:
            flash("Lỗi khi cập nhật phòng.", "error")
        return redirect(url_for('view_rooms'))
    
    # Load current room details
    room = db.get_room_by_number(room_number)
    return render_template('update_room.html', room=room)

@app.route('/delete_room/<room_number>', methods=['POST'])
def delete_room(room_number):
    if db.delete_room(room_number):
        flash("Phòng đã được xóa thành công!", "success")
    else:
        flash("Lỗi khi xóa phòng.", "error")
    return redirect(url_for('view_rooms'))

@app.route('/view_rooms')
def view_rooms():
    rooms = db.get_all_rooms()
    return render_template('view_rooms.html', rooms=rooms)

@app.route('/register')
def login():
    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)
