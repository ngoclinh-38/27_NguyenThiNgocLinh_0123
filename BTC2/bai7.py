import json

json_data = '''
{
    "students": [
        {
            "id": "SV001",
            "name": "Nguyen Van A",
            "year": 2003,
            "class": "CNTT1",
            "gender": "Nam"
        },
        {
            "id": "SV002",
            "name": "Tran Thi B",
            "year": 2004,
            "class": "KT2",
            "gender": "Nữ"
        }
    ]
}
'''


data = json.loads(json_data)


print(" Dữ liệu sau khi chuyển đổi (kiểu Python):")
print(data)
print()

# Kiểm tra kiểu dữ liệu
print("Kiểu dữ liệu của data:", type(data))
print("Kiểu của data['students']:", type(data["students"]))
print()


print(" Danh sách sinh viên:")
for sv in data["students"]:
    print(f"- Mã: {sv['id']}, Tên: {sv['name']}, Năm sinh: {sv['year']}, Lớp: {sv['class']}, Giới tính: {sv['gender']}")
