import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# Tạo cửa sổ chính
win = tk.Tk()
win.title("Profile GUI")

# Tạo tabControl và các tab
tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)  # Tạo Tab 1
tabControl.add(tab1, text='Profile')  # Thêm Tab 1 vào tabControl

tab2 = ttk.Frame(tabControl)  # Tạo Tab 2
tabControl.add(tab2, text='máy tính')  # Thêm Tab 2 vào tabControl

tabControl.pack(expand=1, fill="both")  # Hiển thị tabControl

# Tạo LabelFrame chính trong Tab 1
profile_frame = ttk.LabelFrame(tab1, text=' Profile ')
profile_frame.grid(column=0, row=0, padx=8, pady=4)

# Nhập tên
name_label = ttk.Label(profile_frame, text="Tên:")
name_label.grid(column=0, row=0, sticky=tk.W)
name_entry = ttk.Entry(profile_frame, width=30)
name_entry.grid(column=1, row=0)

# Nhập nghề nghiệp
job_label = ttk.Label(profile_frame, text="Nghề nghiệp:")
job_label.grid(column=0, row=1, sticky=tk.W)
job_entry = ttk.Entry(profile_frame, width=30)
job_entry.grid(column=1, row=1)

# Combobox chọn năm sinh
year_label = ttk.Label(profile_frame, text="Năm sinh:")
year_label.grid(column=0, row=2, sticky=tk.W)
year_combobox = ttk.Combobox(profile_frame, width=28)
year_combobox['values'] = list(range(1950, 2025))  # Danh sách năm từ 1950 đến 2024
year_combobox.grid(column=1, row=2)
year_combobox.current(0)  # Thiết lập giá trị mặc định

# Spinbox chọn tháng sinh
month_label = ttk.Label(profile_frame, text="Tháng sinh:")
month_label.grid(column=0, row=3, sticky=tk.W)
month_spinbox = tk.Spinbox(profile_frame, from_=1, to=12, width=5, bd=3, relief=tk.SUNKEN)
month_spinbox.grid(column=1, row=3)

# Radio buttons cho giới tính
gender_label = ttk.Label(profile_frame, text="Giới tính:")
gender_label.grid(column=0, row=4, sticky=tk.W)

gender_var = tk.StringVar(value= None)  # Giá trị mặc định là Nam

male_radio = ttk.Radiobutton(profile_frame, text="Nam", variable=gender_var, value="Nam")
male_radio.grid(column=1, row=4, sticky=tk.W)

female_radio = ttk.Radiobutton(profile_frame, text="Nữ", variable=gender_var, value="Nữ")
female_radio.grid(column=1, row=5, sticky=tk.W)

other_radio = ttk.Radiobutton(profile_frame, text="Khác", variable=gender_var, value="Khác")
other_radio.grid(column=1, row=6, sticky=tk.W)

# ScrolledText để hiển thị thông tin
info_label = ttk.Label(profile_frame, text="Thông tin hiển thị:")
info_label.grid(column=0, row=7, sticky=tk.W)
scr = scrolledtext.ScrolledText(profile_frame, width=40, height=5, wrap=tk.WORD)
scr.grid(column=0, columnspan=2, row=8)

# Hàm để hiển thị thông tin
def show_info():
    name = name_entry.get()
    job = job_entry.get()
    year = year_combobox.get()
    month = month_spinbox.get()
    gender = gender_var.get()
    scr.delete(1.0, tk.END)  # Xóa nội dung cũ
    scr.insert(tk.INSERT, f"Tên: {name}\nNghề nghiệp: {job}\nTháng sinh: {month}\nNăm sinh: {year}\nGiới tính: {gender}")

# Nút hiển thị thông tin
submit_button = ttk.Button(profile_frame, text="Hiển thị thông tin", command=show_info)
submit_button.grid(column=0, columnspan=2, row=9, pady=5)

# Tạo LabelFrame cho máy tính
calc_frame = ttk.LabelFrame(tab2, text=' Máy tính ')
calc_frame.pack(padx=8, pady=4)

# Nhập số thứ nhất
first_number_label = ttk.Label(calc_frame, text="Số thứ nhất:")
first_number_label.grid(column=0, row=0, sticky=tk.W)
first_number_entry = ttk.Entry(calc_frame, width=15)
first_number_entry.grid(column=1, row=0)

# Nhập số thứ hai
second_number_label = ttk.Label(calc_frame, text="Số thứ hai:")
second_number_label.grid(column=0, row=1, sticky=tk.W)
second_number_entry = ttk.Entry(calc_frame, width=15)
second_number_entry.grid(column=1, row=1)

# Label để hiển thị kết quả
result_label = ttk.Label(calc_frame, text="Kết quả:")
result_label.grid(column=0, row=2, sticky=tk.W)
result_var = tk.StringVar()
result_display = ttk.Label(calc_frame, textvariable=result_var, width=15)
result_display.grid(column=1, row=2)

# Hàm thực hiện phép toán
def calculate(op):
    try:
        num1 = float(first_number_entry.get())
        num2 = float(second_number_entry.get())
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2 if num2 != 0 else "Không thể chia cho 0"
        result_var.set(result)
    except ValueError:
        result_var.set("Nhập số hợp lệ")

# Nút tính toán
add_button = ttk.Button(calc_frame, text="+", command=lambda: calculate("+"))
add_button.grid(column=0, row=3, pady=5)

subtract_button = ttk.Button(calc_frame, text="-", command=lambda: calculate("-"))
subtract_button.grid(column=1, row=3, pady=5)

multiply_button = ttk.Button(calc_frame, text="*", command=lambda: calculate("*"))
multiply_button.grid(column=0, row=4, pady=5)

divide_button = ttk.Button(calc_frame, text="/", command=lambda: calculate("/"))
divide_button.grid(column=1, row=4, pady=5)

win.mainloop()  