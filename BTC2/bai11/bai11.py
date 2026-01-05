import json
from datetime import datetime

transactions = []


while True:
    print("\n--- NHẬP GIAO DỊCH ---")
    loai = input("Nhập loại giao dịch (tiền/vàng): ").strip().lower()
    so_luong = float(input("Nhập số lượng: "))
    don_gia = float(input("Nhập đơn giá: "))

    # Tính thành tiền
    thanh_tien = so_luong * don_gia

    # Thêm vào danh sách giao dịch
    transactions.append({
        "loai_giao_dich": loai,
        "so_luong": so_luong,
        "don_gia": don_gia,
        "thanh_tien": thanh_tien
    })

    # Hỏi người dùng có muốn nhập thêm không
    tiep_tuc = input("Bạn có muốn nhập giao dịch khác không? (y/n): ").strip().lower()
    if tiep_tuc != "y":
        break


print("\nBạn có muốn ghi danh sách giao dịch vào file không?")
chon = input("Nhập 1 = Có, 0 = Không: ").strip()

if chon == "1":
    # Lấy thời gian hiện tại
    now = datetime.now()
    file_name = now.strftime("%Y-%m-%d-%H-%M-%S.json")

   
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(transactions, f, ensure_ascii=False, indent=4)

    print(f"\n Đã ghi dữ liệu giao dịch vào file: {file_name}")

else:
    print("\n Không ghi dữ liệu vào file.")
