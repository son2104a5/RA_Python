import json
import os
import matplotlib.pyplot as plt

students = []


def displayMenu():
    print("============ MENU ============")
    print("1.Hiển thị danh sách sinh viên")
    print("2.Thêm mới sinh viên")
    print("3.Cập nhật thông tin sinh viên")
    print("4.Xoá sinh viên")
    print("5.Tìm kiếm sinh viên")
    print("6.Sắp xếp danh sách sinh viên")
    print("7.Thống kê điểm TB")
    print("8.Vẽ biểu đồ thống kê điểm TB")
    print("9.Lưu vào file CSV")
    print("0.Thoát")


def load_data_from_json():
    global students
    if os.path.exists("data.json"):
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            students = data.get("students", [])
        print("Đã nạp dữ liệu từ file data.json")
    else:
        print("Không tìm thấy file data.json")


def display_students():
    if not students:
        print("Danh sách sinh viên trống!")
        return

    print("\n===== DANH SÁCH SINH VIÊN =====")
    header = (f"{'ID':<8} {'Tên':<15} {'Toán':<8} "
              f"{'Lý':<8} {'Hóa':<8} {'TB':<8} {'Xếp loại':<10}")
    print(header)
    print("-" * 70)

    for sv in students:
        print(f"{sv['id']:<8} {sv['name']:<15} {sv['diem_toan']:<8} "
              f"{sv['diem_ly']:<8} {sv['diem_hoa']:<8} {sv['diem_tb']:<8} "
              f"{sv['xep_loai']:<10}")

    print("-" * 70)
    print(f"Tổng số sinh viên: {len(students)}\n")


def tinh_xep_loai(diem_tb):
    if diem_tb >= 8.0:
        return "Gioi"
    elif diem_tb >= 6.5:
        return "Kha"
    elif diem_tb >= 5.0:
        return "Trung binh"
    else:
        return "Yeu"


def add_student():
    global students

    print("\n===== THÊM MỚI SINH VIÊN =====")

    while True:
        ma = input("Nhập mã sinh viên: ").strip()
        if any(sv["id"] == ma for sv in students):
            print("Mã sinh viên đã tồn tại!")
        else:
            break

    ten = input("Nhập tên sinh viên: ").strip()

    def nhap_diem(mon):
        while True:
            try:
                d = float(input(f"Nhập điểm {mon}: "))
                if 0 <= d <= 10:
                    return d
                else:
                    print(" Điểm phải nằm trong khoảng 0–10!")
            except ValueError:
                print("Nhập số!")

    toan = nhap_diem("Toán")
    ly = nhap_diem("Lý")
    hoa = nhap_diem("Hóa")

    diem_tb = round((toan + ly + hoa) / 3, 2)

    xep_loai = tinh_xep_loai(diem_tb)

    new_sv = {
        "id": ma,
        "name": ten,
        "diem_toan": toan,
        "diem_ly": ly,
        "diem_hoa": hoa,
        "diem_tb": diem_tb,
        "xep_loai": xep_loai
    }

    students.append(new_sv)

    print("Đã thêm sinh viên thành công!")
    print(f"➡ Điểm TB: {diem_tb} | Xếp loại: {xep_loai}\n")


def update_student():
    global students
    print("\n===== CẬP NHẬT THÔNG TIN SINH VIÊN =====")

    ma = input("Nhập mã sinh viên cần sửa: ").strip()
    sv = next((s for s in students if s["id"] == ma), None)

    if sv is None:
        print("Không tìm thấy sinh viên!")
        return

    print(f"Đang sửa sinh viên: {sv['name']}")

    def nhap_diem(mon):
        while True:
            try:
                d = float(input(f"Nhập điểm {mon}: "))
                if 0 <= d <= 10:
                    return d
                else:
                    print("Điểm phải nằm trong khoảng 0–10!")
            except ValueError:
                print("Nhập số!")

    sv["diem_toan"] = nhap_diem("Toán")
    sv["diem_ly"] = nhap_diem("Lý")
    sv["diem_hoa"] = nhap_diem("Hóa")

    diem_sum = sv["diem_toan"] + sv["diem_ly"] + sv["diem_hoa"]
    sv["diem_tb"] = round(diem_sum / 3, 2)

    sv["xep_loai"] = tinh_xep_loai(sv["diem_tb"])

    print("Cập nhật thành công!")
    print(f"Điểm TB mới: {sv['diem_tb']} | Xếp loại: {sv['xep_loai']}\n")


def delete_student():
    global students
    print("\n===== XOÁ SINH VIÊN =====")

    ma = input("Nhập mã sinh viên cần xoá: ").strip()
    sv = next((s for s in students if s["id"] == ma), None)

    if sv is None:
        print("Không tìm thấy mã sinh viên!")
        return

    print(f"Bạn đang xoá sinh viên: {sv['name']}")
    confirm = input("Bạn có chắc muốn xoá? (y/n): ").lower()

    if confirm == "y":
        students.remove(sv)
        print("Đã xoá sinh viên.")
    else:
        print("Đã huỷ xoá.")


def search_student():
    global students
    print("\n===== TÌM KIẾM SINH VIÊN =====")

    keyword = input("Nhập tên hoặc mã sinh viên: ").strip().lower()

    results = [
        sv for sv in students
        if keyword in sv["id"].lower() or keyword in sv["name"].lower()
    ]

    if not results:
        print("Không tìm thấy kết quả!")
        return

    print("\nKẾT QUẢ TÌM KIẾM:")
    for sv in results:
        print(f"{sv['id']} - {sv['name']} | TB: {sv['diem_tb']} | "
              f"{sv['xep_loai']}")


def sort_students():
    global students
    print("\n===== SẮP XẾP DANH SÁCH =====")
    print("1. Sắp xếp theo điểm TB giảm dần")
    print("2. Sắp xếp theo tên A → Z")

    choice = input("Chọn kiểu sắp xếp: ")

    if choice == "1":
        students.sort(key=lambda s: s["diem_tb"], reverse=True)
        print("Đã sắp xếp theo điểm TB (giảm dần).")
    elif choice == "2":
        students.sort(key=lambda s: s["name"].lower())
        print("Đã sắp xếp theo tên (A → Z).")
    else:
        print("Lựa chọn không hợp lệ!")


def stats_ranking():
    global students
    print("\n===== THỐNG KÊ XẾP LOẠI =====")

    thong_ke = {"Gioi": 0, "Kha": 0, "Trung Binh": 0, "Yeu": 0}

    for sv in students:
        xl = sv["xep_loai"]
        if xl in thong_ke:
            thong_ke[xl] += 1

    for loai, so_luong in thong_ke.items():
        print(f"{loai}: {so_luong} sinh viên")

    return thong_ke


def plot_stats():
    print("\n===== VẼ BIỂU ĐỒ THỐNG KÊ =====")
    thong_ke = stats_ranking()

    labels = list(thong_ke.keys())
    values = list(thong_ke.values())

    if sum(values) == 0:
        print("Không có dữ liệu để vẽ biểu đồ!")
        return

    print("1. Biểu đồ tròn (Pie Chart)")
    print("2. Biểu đồ cột (Bar Chart)")
    opt = input("Chọn kiểu biểu đồ: ")

    if opt == "1":
        plt.pie(values, labels=labels, autopct="%1.1f%%")
        plt.title("Tỷ lệ xếp loại học lực")
        plt.show()

    elif opt == "2":
        plt.bar(labels, values, color=['green', 'blue', 'orange', 'red'])
        plt.title("Thống kê số lượng học lực")
        plt.xlabel("Xếp loại")
        plt.ylabel("Số lượng")
        plt.show()

    else:
        print("Lựa chọn không hợp lệ!")


def save_to_json():
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump({"students": students}, f, ensure_ascii=False, indent=4)
    print("💾 Đã lưu dữ liệu vào data.json")


while True:
    displayMenu()
    choice = int(input("Lựa chọn của bạn: "))
    if choice == 0:
        break
    elif choice == 1:
        load_data_from_json()
        display_students()
    elif choice == 2:
        add_student()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        search_student()
    elif choice == 6:
        sort_students()
    elif choice == 7:
        stats_ranking()
    elif choice == 8:
        plot_stats()
    elif choice == 9:
        save_to_json()
        