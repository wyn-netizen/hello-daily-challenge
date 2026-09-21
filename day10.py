try:
    num = int(input("请输入一个数字："))
    print(f"你输入的是{num}")
except ValueError:
    print("这不是数字！请重新运行并输入数字。")

try:
    a = int(input("被除数:"))
    b = int(input("除数："))
    print(a/b)
except ValueError:
    print("请输入数字！")
except ZeroDivisionError:
    print("除数不能为0！")

def safe_int(s):
    try:
        return int(s)
    except:
        return None
num = safe_int(input("请输入一个数字："))
if num is None:
    print("这不是数字")
else:
    print(f"你输入的是：{num}")
                    