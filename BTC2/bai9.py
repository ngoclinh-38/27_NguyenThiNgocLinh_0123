import json

student = {
    "name": "Nguyen Van A",
    "class": "CNTT1",
    "year": 2003,
    "gender": "Nam",
    "id": "SV001"
}


json_data = json.dumps(student, sort_keys=True, indent=4, ensure_ascii=False)


print("Chuỗi JSON sau khi sắp xếp và định dạng:")
print(json_data)
print()


print("Các thành viên của đối tượng:")
for key, value in student.items():
    print(f"{key}: {value}")
