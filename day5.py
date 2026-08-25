user = {"name":"王云诺","age": 18,"city": "青岛"}
print(user["name"])
print(user["age"])

user["age"] = 19
user["hobby"] = "写代码"
del user["city"]
print(user)
for key, value in user.items():
    print(f"{key} = {value}")

print(user.get("city"))
print(user.get("city","未知"))

users = [
    {"name": "王云诺", "age": 18},
    {"name": "斡芋泥", "age": 18},
    {"name": "wangyunnuo", "age": 18}
]
for u in users:
    print(f"{u['name']}今年{u['age']}岁")
