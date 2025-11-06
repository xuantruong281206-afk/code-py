from tkinter import *
import webbrowser
from PIL import Image, ImageTk
import pandas as pd
import os

# --- Cấu hình đường dẫn CSV ---
csv_path = "/Users/vuxuantruong/Documents/code/oop/Taikhoan.csv"
# --- File dữ liệu khách hàng thân thiết ---
customer_csv = "/Users/vuxuantruong/Documents/code/oop/KhachHang.csv"

if not os.path.exists(customer_csv):
    df_cus = pd.DataFrame(columns=["MaKH", "TenKH", "SoDienThoai", "DiemTichLuy"])
    df_cus.to_csv(customer_csv, index=False)


# --- Nếu chưa có file -> tạo mới ---
if not os.path.exists(csv_path):
    df_init = pd.DataFrame(columns=["MaNV", "TenDangNhap", "MatKhau", "VaiTro"])
    df_init.to_csv(csv_path, index=False)

# --- Cửa sổ chính (đăng nhập) ---
root = Tk()
root.title('Quản Lý Siêu Thị - Đăng Nhập')
root.geometry('800x600')
root.configure(bg='lightgray')

# --- Tiêu đề ---
Label(
    root,
    text='APP SUPER MARKET',
    fg='black',
    font=('Cambria', 16, 'bold'),
    width=30,
    bg='lightgray'
).pack(pady=10)

# --- Ảnh minh họa ---
try:
    img = Image.open("/Users/vuxuantruong/Downloads/m.png")
    img = img.resize((250, 180))
    photo = ImageTk.PhotoImage(img)
    Label(root, image=photo, bg='lightgray').pack(pady=10)
except:
    Label(root, text="(Không tải được ảnh )", bg='lightgray', fg='gray').pack()

# --- Danh sách thông báo ---
listbox = Listbox(root, width=60, height=5)
listbox.pack(padx=10, pady=10)

# --- Khu vực nhập thông tin ---
form_frame = Frame(root, bg='lightgray')
form_frame.pack(pady=10)

Label(form_frame, text='Tên đăng nhập:', bg='lightgray').grid(row=1, column=0, sticky=E, padx=5, pady=5)
entry_name = Entry(form_frame, width=30)
entry_name.grid(row=1, column=1, pady=5)

Label(form_frame, text='Mật khẩu:', bg='lightgray').grid(row=2, column=0, sticky=E, padx=5, pady=5)
entry_pass = Entry(form_frame, width=30, show='*')
entry_pass.grid(row=2, column=1, pady=5)

# --- Hàm mở trang trợ giúp ---
def open_help():
    webbrowser.open('https://docs.google.com/document/d/1IoizpBWvG78eF3vgWCGH8CZ0ZovLgAoGi67tmJg1bhw/edit?usp=sharing')

# --- Hàm mở cửa sổ chính ---
def open_main_window(user_name, role):
    new_window = Toplevel(root)
    new_window.title(f"Hệ Thống Quản Lý - {role}")
    new_window.geometry("800x600")
    new_window.configure(bg='#f0f0f0')

    Label(
        new_window,
        text=f"Xin chào {user_name} đến với giao diện {role}",
        font=('Cambria', 18, 'bold'),
        fg='green'
    ).pack(pady=20)

    btn_frame = Frame(new_window, bg='#f0f0f0')
    btn_frame.pack(pady=30)

    # --- Phân quyền tài khoản ---
    if role == "Admin":
        Button(btn_frame, text='👤 Quản Lý Tài Khoản Khách Hàng', width=22, height=2, font=('Cambria', 12)).grid(row=0, column=0, padx=15, pady=10)
        Button(btn_frame, text='📦 Quản Lý Hàng Hóa', width=22, height=2, font=('Cambria', 12)).grid(row=0, column=1, padx=15, pady=10)
        Button(btn_frame, text='📊 Quản lý doanh thu', width=22, height=2, font=('Cambria', 12)).grid(row=1, column=0, padx=15, pady=10)
        Button(btn_frame, text='⚙️ Quản lý nhân viên', width=22, height=2, font=('Cambria', 12)).grid(row=1, column=1, padx=15, pady=10)

    elif role == "Nhân viên bán hàng":
        Button(btn_frame, text='🖊️Chấm Công', width=20, height=2, font=('Cambria', 12)).grid(row=0, column=0, padx=15, pady=10)
        Button(btn_frame, text='💳 Thanh Toán', width=20, height=2, font=('Cambria', 12)).grid(row=0, column=1, padx=15, pady=10)
        Button(btn_frame, text='📋 Xem Danh Sách Đơn', width=20, height=2, font=('Cambria', 12)).grid(row=1, column=0, padx=15, pady=10)
        Button(btn_frame, text='📦Xem Hàng Hoá', width=20, height=2, font=('Cambria', 12)).grid(row=0, column=0, padx=15, pady=10)

    elif role == "Khách Hàng":
    # Đảm bảo file có cột DiaChi
        df_cus = pd.read_csv(customer_csv, dtype=str).fillna("0")
    if "DiaChi" not in df_cus.columns:
        df_cus["DiaChi"] = "Chưa cập nhật"
        df_cus.to_csv(customer_csv, index=False)

    cus_row = df_cus[df_cus["TenKH"] == user_name]
    if cus_row.empty:
        new_cus = pd.DataFrame([[f"KH{len(df_cus)+1:03}", user_name, "Chưa cập nhật", 0, "Chưa cập nhật"]],
                               columns=["MaKH", "TenKH", "SoDienThoai", "DiemTichLuy", "DiaChi"])
        df_cus = pd.concat([df_cus, new_cus], ignore_index=True)
        df_cus.to_csv(customer_csv, index=False)
        cus_id = f"KH{len(df_cus):03}"
        points = 0
        phone = "Chưa cập nhật"
        address = "Chưa cập nhật"
    else:
        cus_id = cus_row.iloc[0]["MaKH"]
        phone = cus_row.iloc[0]["SoDienThoai"]
        points = int(cus_row.iloc[0]["DiemTichLuy"])
        address = cus_row.iloc[0]["DiaChi"]

    new_window.configure(bg="white")
    Label(new_window, text="💎 THÔNG TIN KHÁCH HÀNG", font=('Cambria', 15, 'bold'),
          bg='white', fg='blue').pack(pady=15)

    info_frame = Frame(new_window, bg="white")
    info_frame.pack(pady=10)

    Label(info_frame, text=f"Mã KH: {cus_id}", font=('Cambria', 12), bg='white').pack(pady=5)
    Label(info_frame, text=f"Tên KH: {user_name}", font=('Cambria', 12), bg='white').pack(pady=5)
    Label(info_frame, text=f"Số điện thoại: {phone}", font=('Cambria', 12), bg='white').pack(pady=5)
    Label(info_frame, text=f"Địa chỉ: {address}", font=('Cambria', 12), bg='white').pack(pady=5)

    points_label = Label(new_window, text=f"⭐ Điểm hiện có: {points}", font=('Cambria', 14, 'bold'),
                         fg='green', bg='white')
    points_label.pack(pady=20)

    # --- Nút mở cửa sổ cập nhật thông tin ---
    def update_info():
        win = Toplevel(new_window)
        win.title("Cập nhật thông tin cá nhân")
        win.geometry("400x400")
        win.configure(bg="white")

        Label(win, text="📝 Cập nhật thông tin cá nhân", font=('Cambria', 14, 'bold'),
              fg='blue', bg='white').pack(pady=10)

        # --- Mật khẩu ---
        Label(win, text="Mật khẩu mới:", bg='white').pack()
        entry_pass = Entry(win, width=35, show='*')
        entry_pass.pack(pady=5)

        # --- Số điện thoại ---
        Label(win, text="Số điện thoại:", bg='white').pack()
        entry_phone = Entry(win, width=35)
        entry_phone.insert(0, phone)
        entry_phone.pack(pady=5)

        # --- Địa chỉ ---
        Label(win, text="Địa chỉ:", bg='white').pack()
        entry_address = Entry(win, width=35)
        entry_address.insert(0, address)
        entry_address.pack(pady=5)

        # --- Nút lưu ---
        def save_changes():
            new_pass = entry_pass.get().strip()
            new_phone = entry_phone.get().strip()
            new_address = entry_address.get().strip()

            # Cập nhật KhachHang.csv
            df_cus = pd.read_csv(customer_csv, dtype=str).fillna("")
            df_cus.loc[df_cus["MaKH"] == cus_id, "SoDienThoai"] = new_phone
            df_cus.loc[df_cus["MaKH"] == cus_id, "DiaChi"] = new_address
            df_cus.to_csv(customer_csv, index=False)

            # Cập nhật mật khẩu trong Taikhoan.csv (nếu có nhập)
            if new_pass != "":
                df_acc = pd.read_csv(csv_path, dtype=str).fillna("")
                df_acc.loc[df_acc["TenDangNhap"] == user_name, "MatKhau"] = new_pass
                df_acc.to_csv(csv_path, index=False)

            messagebox.showinfo("✅ Thành công", "Cập nhật thông tin thành công!")
            win.destroy()

        Button(win, text="Lưu thay đổi", command=save_changes,
               width=15, font=('Cambria', 12), bg="#4CAF50", fg="white").pack(pady=20)

    # --- Lưu file lịch sử điểm ---
    history_csv = "/Users/vuxuantruong/Documents/code/oop/LichSuDiem.csv"
    if not os.path.exists(history_csv):
        pd.DataFrame(columns=["MaKH", "HanhDong", "SoDiem", "ThoiGian"]).to_csv(history_csv, index=False)

    # --- Hàm xem lịch sử điểm ---
    def show_history():
        win = Toplevel(new_window)
        win.title("Lịch Sử Điểm")
        win.geometry("500x400")
        win.configure(bg='white')

        Label(win, text=f"Lịch sử điểm của {user_name}", font=('Cambria', 14, 'bold'), bg='white').pack(pady=10)
        frame = Frame(win, bg='white')
        frame.pack(pady=5)

        df_his = pd.read_csv(history_csv, dtype=str).fillna("0")
        df_user = df_his[df_his["MaKH"] == cus_id]

        if df_user.empty:
            Label(frame, text="(Chưa có lịch sử điểm)", bg='white', fg='gray').pack(pady=20)
        else:
            for _, row in df_user.iterrows():
                Label(frame, text=f"{row['ThoiGian']} - {row['HanhDong']}: {row['SoDiem']} điểm",
                      bg='white', font=('Cambria', 11)).pack(anchor='w', padx=20)

    # --- Hàm đổi voucher ---
    def redeem_voucher():
        pts_needed = 50
        if points < pts_needed:
            messagebox.showwarning("Không đủ điểm", f"Bạn cần ít nhất {pts_needed} điểm để đổi voucher!")
            return

        import random, datetime
        voucher_code = "VC" + str(random.randint(10000, 99999))
        new_points = points - pts_needed

        df_cus.loc[df_cus["MaKH"] == cus_id, "DiemTichLuy"] = new_points
        df_cus.to_csv(customer_csv, index=False)
        points_label.config(text=f"⭐ Điểm hiện có: {new_points}")

        df_his = pd.read_csv(history_csv, dtype=str).fillna("0")
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        new_row = pd.DataFrame([[cus_id, "Đổi voucher", f"-{pts_needed}", now]],
                               columns=["MaKH", "HanhDong", "SoDiem", "ThoiGian"])
        df_his = pd.concat([df_his, new_row], ignore_index=True)
        df_his.to_csv(history_csv, index=False)

        messagebox.showinfo("🎁 Voucher thành công",
                            f"Chúc mừng bạn đã đổi thành công!\n\nMã voucher của bạn là: {voucher_code}\nGiảm 50.000 VNĐ cho đơn hàng tiếp theo.")

    # --- Các nút chức năng ---
    btn_frame = Frame(new_window, bg='white')
    btn_frame.pack(pady=30)

    Button(btn_frame, text='🧾 Lịch sử điểm', command=show_history,
           width=18, height=2, font=('Cambria', 12)).grid(row=0, column=0, padx=10)
    Button(btn_frame, text='🎁 Đổi Voucher', command=redeem_voucher,
           width=18, height=2, font=('Cambria', 12)).grid(row=0, column=1, padx=10)
    Button(btn_frame, text='📝 Cập nhật thông tin', command=update_info,
           width=20, height=2, font=('Cambria', 12)).grid(row=1, column=0, columnspan=2, pady=10)

    bottom_frame = Frame(new_window)
    bottom_frame.pack(side=BOTTOM, pady=30)
    Button(bottom_frame, text='Đăng Xuất', width=15, height=2, font=('Cambria', 11),
           command=lambda: logout(new_window)).pack(side=LEFT, padx=15)
    Button(bottom_frame, text='Thoát', width=15, height=2, font=('Cambria', 11),
           command=root.quit).pack(side=LEFT, padx=15)



# --- Hàm đăng xuất ---
def logout(current_window):
    current_window.destroy()
    root.deiconify()

# --- Hàm đăng nhập ---
def login():
    name = entry_name.get().strip()
    password = entry_pass.get().strip()

    if name == "" or password == "":
        listbox.insert(END, "⚠️ Vui lòng nhập đầy đủ thông tin đăng nhập!")
        return

    try:
        df = pd.read_csv(csv_path, dtype=str).dropna()
        df = df.apply(lambda x: x.str.strip())
    except Exception as e:
        listbox.insert(END, f"⚠️ Lỗi khi đọc file: {e}")
        return

    user = df[
        (df['TenDangNhap'] == name) &
        (df['MatKhau'] == password)
    ]

    if not user.empty:
        role = user.iloc[0]['VaiTro']
        listbox.insert(END, f"✅ Đăng nhập thành công: {name} ({role})")
        root.withdraw()
        open_main_window(name, role)
    else:
        listbox.insert(END, "❌ Sai thông tin đăng nhập! Vui lòng thử lại.")




# --- Hàm tạo tài khoản ---
# --- Hàm tạo tài khoản ---
def create_account():
    new_win = Toplevel(root)
    new_win.title("Tạo tài khoản mới")
    new_win.geometry("400x350")

    Label(new_win, text="Tên đăng nhập:").grid(row=1, column=0, padx=10, pady=10)
    e_name = Entry(new_win, width=30)
    e_name.grid(row=1, column=1)

    Label(new_win, text="Mật khẩu:").grid(row=2, column=0, padx=10, pady=10)
    e_pass = Entry(new_win, width=30, show="*")
    e_pass.grid(row=2, column=1)

    Label(new_win, text="Vai trò:").grid(row=3, column=0, padx=10, pady=10)
    role_var = StringVar(value="Nhân viên bán hàng")
    roles = ["Admin", "Nhân viên bán hàng", "Khách Hàng"]
    OptionMenu(new_win, role_var, *roles).grid(row=3, column=1)

    def save_new_account():
        id_nv = e_id.get().strip()
        name_nv = e_name.get().strip()
        pass_nv = e_pass.get().strip()
        role_nv = role_var.get().strip()

        if id_nv == "" or name_nv == "" or pass_nv == "":
            listbox.insert(END, "⚠️ Vui lòng nhập đủ thông tin!")
            return

        # Đọc file tài khoản
        df = pd.read_csv(csv_path, dtype=str).fillna("")
        if not df[df['TenDangNhap'] == name_nv].empty:
            listbox.insert(END, "⚠️ Tên đăng nhập đã tồn tại!")
            return

        # --- Lưu vào Taikhoan.csv ---
        new_data = pd.DataFrame([[id_nv, name_nv, pass_nv, role_nv]],
                                columns=[ "TenDangNhap", "MatKhau", "VaiTro"])
        new_data.to_csv(csv_path, mode='a', header=False, index=False)
        listbox.insert(END, f"✅ Tạo tài khoản thành công cho {name_nv} ({role_nv})")

        # --- Nếu là khách hàng -> thêm vào file KhachHang.csv ---
        if role_nv == "Khách Hàng":
            if not os.path.exists(customer_csv):
                pd.DataFrame(columns=["MaKH", "TenKH", "SoDienThoai", "DiemTichLuy"]).to_csv(customer_csv, index=False)

            df_cus = pd.read_csv(customer_csv, dtype=str).fillna("0")
            new_id = f"KH{len(df_cus) + 1:03}"

            new_cus = pd.DataFrame([[new_id, name_nv, "Chưa cập nhật", 0]],
                                   columns=["MaKH", "TenKH", "SoDienThoai", "DiemTichLuy"])
            df_cus = pd.concat([df_cus, new_cus], ignore_index=True)
            df_cus.to_csv(customer_csv, index=False)

            listbox.insert(END, f"✅ Đồng bộ dữ liệu khách hàng: {new_id} ({name_nv})")

        new_win.destroy()

    Button(new_win, text="Lưu tài khoản", command=save_new_account, width=15).grid(row=4, column=1, pady=20)


# --- Các nút chức năng ---
button_frame = Frame(root, bg='lightgray')
button_frame.pack(pady=15)

Button(button_frame, text='Đăng Nhập', command=login, width=12).pack(side=LEFT, padx=5)
Button(button_frame, text='Thoát', command=root.quit, width=12).pack(side=LEFT, padx=5)
Button(button_frame, text='Quên Mật Khẩu', width=15).pack(side=LEFT, padx=5)
Button(button_frame, text='Trợ Giúp', command=open_help, width=12).pack(side=LEFT, padx=5)
Button(button_frame, text='Tạo Tài Khoản', command=create_account, width=15).pack(side=LEFT, padx=5)

root.mainloop()
