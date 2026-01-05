import json

students = {
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


json_string = json.dumps(students, indent=4, ensure_ascii=False)


print(" Chuỗi JSON sau khi chuyển đổi:")
print(json_string)
print()


print(" Danh sách các giá trị:")
for sv in students["students"]:
    for key, value in sv.items():
        print(f"{key}: {value}")
    print("-" * 40)
