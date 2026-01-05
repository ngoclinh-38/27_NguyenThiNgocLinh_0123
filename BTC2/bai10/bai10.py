import json
from collections import Counter

# -----------------------------
# Bước 1: Đọc dữ liệu từ file JSON
# -----------------------------
with open("BTVN/BTC2/bai10/nhanvien.json", "r", encoding="utf-8") as file:
    data = json.load(file)

company_name = data["company"]["name"]
company_address = data["company"]["address"]
employees = data["employees"]


# Dùng Counter để đếm số nhân viên từng đơn vị
unit_counts = Counter(emp["unit"] for emp in employees)


total_employees = len(employees)


print(f"Tên công ty: {company_name}")
print(f"Địa chỉ: {company_address}")
print(f"Tổng số nhân viên: {total_employees}")
print("\n- Thống kê nhân viên theo đơn vị -\n")

for i, (unit, count) in enumerate(unit_counts.items(), start=1):
    percent = (count / total_employees) * 100
    print(f"{i}/ Tên đơn vị: {unit}")
    print(f"   - Số nhân viên: {count}")
    print(f"   - Tỷ lệ: {percent:.2f}%\n")
