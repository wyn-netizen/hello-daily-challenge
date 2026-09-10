import random
import time
start = time.time()
target = random.randint(1, 10)
print("我想到一个1~10之间的数，你猜猜看！")
for i in range(5):
    guess = int(input("你的猜测："))
    if guess == target:
        print("猜对啦！")
        break
    elif guess < target:
        print("小了，再大点！")
    else:
        print("大了，再小点！")
else:
    print(f"机会用完了，答案是{target}")        
over = time.time()
print("你猜了", over - start, "秒")